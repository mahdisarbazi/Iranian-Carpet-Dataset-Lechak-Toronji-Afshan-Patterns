import cv2
import os
from tkinter import filedialog, messagebox
import numpy as np

def imread_unicode(filename):
    """خواندن تصویر با پشتیبانی از مسیرهای فارسی"""
    return cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_COLOR)

def imwrite_unicode(filename, img):
    """ذخیره تصویر با پشتیبانی از مسیرهای فارسی"""
    ext = os.path.splitext(filename)[1]
    is_success, buffer = cv2.imencode(ext, img)
    if is_success:
        buffer.tofile(filename)
    return is_success

def process_images():
    # انتخاب پوشه تصاویر
    folder_path = filedialog.askdirectory(title="انتخاب پوشه حاوی تصاویر")
    if not folder_path:
        return
    
    # فرمت‌های پشتیبانی شده
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')
    
    # پیدا کردن تصاویر در پوشه
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_formats)]
    
    if not image_files:
        messagebox.showwarning("هشدار", "هیچ تصویری در پوشه انتخاب شده یافت نشد!")
        return
    
    processed_count = 0
    
    for filename in image_files:
        try:
            # خواندن تصویر اصلی با پشتیبانی از مسیر فارسی
            img_path = os.path.join(folder_path, filename)
            img = imread_unicode(img_path)
            
            if img is None:
                continue
                
            # تجزیه نام فایل
            name, ext = os.path.splitext(filename)
            
            # 1. تصویر خاکستری
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_path = os.path.join(folder_path, f"{name}g{ext}")
            imwrite_unicode(gray_path, gray_img)
            
            # 2. فیلتر لاپلاسین روی تصویر رنگی (حفظ کانال‌های رنگی)
            laplacian_color = cv2.Laplacian(img, cv2.CV_8U, ksize=3)
            laplacian_color_path = os.path.join(folder_path, f"{name}l{ext}")
            imwrite_unicode(laplacian_color_path, laplacian_color)
            
            # 3. فیلتر تشخیص بافت فرش (Gabor Filter)
            # فیلتر گابور برای تشخیص الگوها و بافت فرش
            kernel = cv2.getGaborKernel((15, 15), 3, np.pi/4, 2*np.pi/3, 0.8, 0, ktype=cv2.CV_32F)
            gabor_img = cv2.filter2D(img, cv2.CV_8UC3, kernel)
            
            # ترکیب نرم با تصویر اصلی برای حفظ وضوح
            gabor_enhanced = cv2.addWeighted(img, 0.7, gabor_img, 0.3, 0)
            
            gabor_path = os.path.join(folder_path, f"{name}t{ext}")  # t برای texture
            imwrite_unicode(gabor_path, gabor_enhanced)
            
            processed_count += 1
            
        except Exception as e:
            print(f"خطا در پردازش {filename}: {str(e)}")
            continue
    
    messagebox.showinfo("اتمام", f"پردازش کامل شد!\n{processed_count} تصویر پردازش شد.")

if __name__ == "__main__":
    process_images()