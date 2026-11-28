"""Run the pipeline on data/sample.json and print which box was selected.

Usage:  python run.py
"""

import json
from pathlib import Path

from pipeline.candidates import generate_candidates
from pipeline.scoring import select_best

SAMPLE = Path(__file__).parent / "data" / "sample.json"


def label_of(image, box):
    """Name of the blob that exactly matches `box` (for humans only; the pipeline never uses labels)."""
    x1, y1, x2, y2 = box
    for blob in image["blobs"]:
        if (blob["x"], blob["y"], blob["x"] + blob["w"], blob["y"] + blob["h"]) == (x1, y1, x2, y2):
            return blob["label"]
    return "?"


def main():
    image = json.loads(SAMPLE.read_text(encoding="utf-8"))
    boxes = generate_candidates(image)
    best = select_best(image, boxes)
    print(f"Candidates: {len(boxes)}")
    print(f"Looking for: {image['query']['label']}")
    if best is None:
        print("No eligible candidate box.")
        return
    print(f"Selected box: {best} -> {label_of(image, best)}")


if __name__ == "__main__":
    main()
