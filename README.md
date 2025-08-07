Download Link:
https://doi.org/10.34740/kaggle/dsv/12702937

```markdown
# Iranian Carpet Dataset: Lechak-Toranj & Afshan Patterns

## Overview
This dataset contains **Iranian carpet** images focused on two prominent patterns: **Lechak-Toranj** (Corner-Medallion) and **Afshan** (Scattered) designs. The dataset has been augmented using specialized image processing techniques to improve machine learning classification performance.

## Dataset Details
- **Total Images**: 984 (4x augmented from 284 original images)
- **Classes**: 2 (Lechak-Toranj: 572 images, Afshan: 564 images)
- **Image Size**: Original resolution (not resized to 128×128)
- **Format**: JPG

## Data Augmentation (4x)
The dataset includes three types of processed images for each original:
1. **Grayscale**: Removes color influence to focus on structural patterns
2. **Laplacian Filter**: Enhances edges and geometric details of carpet designs
3. **Gabor Filter**: Extracts texture features specific to carpet patterns

Each original image is augmented using these three filters, resulting in a 4x expansion of the dataset (original + 3 processed versions).

The Python implementation for these filters is provided in the file: `augmentation_filters.py`.

## Pattern Descriptions

### Lechak-Toranj (لچک ترنج)
Structured design featuring a central medallion (Toranj) - circular, oval, or diamond-shaped - surrounded by four corner elements (Lechak). This pattern maintains its classification even when some elements are removed.

### Afshan (افشان)
Scattered pattern design where motifs and decorations move in a specific direction across the carpet surface, with no repetitive pattern visible in other areas.

## Authors
**Prepared by:**
- Siamak Sarbazi - M.Sc. Student in Carpet Design, Tabriz Islamic Art University
- Mahdi Sarbazi - Ph.D. Student in Computer engineering, Sanandaj Branch (Kurdistan), Islamic Azad University

## Citation
If you use this dataset, please cite:
```

Iranian Carpet Dataset: Lechak-Toranj & Afshan Patterns Authors: Siamak Sarbazi, Mahdi Sarbazi Year: 2025, https://doi.org/10.34740/kaggle/dsv/12702937

```

## Usage
This dataset is designed for:
- Iranian carpet pattern classification
- Traditional art pattern recognition
- Lightweight machine learning model development
- Computer vision research on cultural heritage

## License
Use of this dataset is permitted with citation.

**Suggested GitHub practice:**
You may include a `LICENSE` file in the repository and reference [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), without adding its full legal text to this file.

```
