"""Copy downscaled HCCI SEM micrographs into the deck and record their provenance.

The images come from the open HCCI SEM dataset on Zenodo
(https://doi.org/10.5281/zenodo.21931379, CC BY 4.0; one high-chromium cast
iron specimen per material state). Each micrograph output is a grayscale JPEG,
either centre-cropped to the aspect ratio of its slot on the slides or, for a
full-frame output, uncropped, so that positions inside it, such as the detail
area within the overview, stay where the dataset README gives them. A mask
output is an area's annotation in the colours stored in the dataset, softened
toward white. The provenance CSV lists the source file and the workbook
metadata of every output.

Usage (from the presentation folder):
    python -I tools/prepare_hcci_images.py <path/to/HCCI_Dataset_FIN> --out assets/hcci
"""
import argparse
import csv
from pathlib import Path

import pandas as pd
from PIL import Image

# output name -> (dataset image ID, width/height of the slot on the slide; None keeps the full frame)
SELECTION = {
    # one detail micrograph per specimen, Vilella etching, Helios G4 PFIB CXe, BSE, 10 kV, long
    # dwell; no slide shows them at present
    "spec-ascast": (21, 1.6),          # AsCast
    "spec-q980-0h": (57, 1.6),         # Q980_0h_WC
    "spec-q980-9h": (93, 1.6),         # Q980_9h_AC
    # slide 3: the Q980_0h_WC overview area and the detail area inside it, Vilella etching,
    # Helios G4 PFIB CXe, 10 kV, long dwell
    "overview-se": (49, None),
    "overview-bse": (51, None),
    "overview-inlens": (53, None),
    "detail-se": (55, None),
    "detail-bse": (57, None),
    "detail-inlens": (59, None),
}
# output name -> image ID whose mask is copied; every image of an area has the same mask
MASKS = {
    "detail-mask": 57,                 # Q980_0h_WC, Vilella, detail area (slide 3)
}
COLUMNS = ["File Name", "Sample", "Kind", "Etching", "SEM", "Detector", "Voltage", "Dwell Time cat", "Pixel Size"]
AREA_COLUMNS = ["File Name", "Sample", "Kind", "Etching"]  # a mask belongs to its area, not to one acquisition
FULL_FRAME_WIDTH = 1000
MASK_SOFTEN = 0.25  # share of white blended into the stored mask colours


def centre_crop(img, aspect):
    """Largest centred crop of img with width/height == aspect."""
    w, h = img.size
    if w / h > aspect:
        cw, ch = round(h * aspect), h
    else:
        cw, ch = w, round(w / aspect)
    left, top = (w - cw) // 2, (h - ch) // 2
    return img.crop((left, top, left + cw, top + ch))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("dataset", type=Path, help="HCCI_Dataset_FIN folder")
    parser.add_argument("--out", type=Path, default=Path("assets/hcci"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    meta = pd.read_excel(args.dataset / "Metadata" / "Metadata_All_Samples_Dwell_cat.xlsx")
    meta = meta.set_index("File Name", drop=False)

    rows = []
    for name, (image_id, aspect) in SELECTION.items():
        source = f"Images/{image_id}.png"
        img = Image.open(args.dataset / source).convert("L")
        if aspect is None:
            aspect = img.width / img.height
            img.thumbnail((FULL_FRAME_WIDTH, FULL_FRAME_WIDTH))
        else:
            img = centre_crop(img, aspect)
            img.thumbnail((900, 900))
        assert abs(img.width / img.height - aspect) < 0.01, (name, img.size)
        img.save(args.out / f"{name}.jpg", quality=86)
        rows.append({"output": f"{name}.jpg", "aspect": round(aspect, 4), "source": source,
                     **meta.loc[image_id, COLUMNS].to_dict()})

    for name, image_id in MASKS.items():
        source = f"Masks/{image_id}_Mask.png"
        mask = Image.open(args.dataset / source).convert("RGB")
        aspect = mask.width / mask.height
        # nearest neighbour keeps every pixel one of the stored class colours before softening
        mask = mask.resize((FULL_FRAME_WIDTH, round(FULL_FRAME_WIDTH / aspect)), Image.NEAREST)
        mask = Image.blend(mask, Image.new("RGB", mask.size, "white"), MASK_SOFTEN)
        mask.save(args.out / f"{name}.png", optimize=True)
        area = meta.loc[image_id, AREA_COLUMNS].to_dict()
        rows.append({"output": f"{name}.png", "aspect": round(aspect, 4), "source": source,
                     **{c: area.get(c, "") for c in COLUMNS}})

    with open(args.out / "provenance.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} images written to {args.out}")


if __name__ == "__main__":
    main()
