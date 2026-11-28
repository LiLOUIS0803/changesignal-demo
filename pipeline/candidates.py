"""Candidate-region generation.

A box is a tuple (x1, y1, x2, y2): top-left corner inclusive, bottom-right exclusive.
"""


def generate_candidates(image):
    """Return one candidate box per blob in the image, in the order supplied by the data source.

    Keep the input order so the candidate list can be compared with the source rows.
    """
    boxes = []
    for blob in image["blobs"]:
        x1, y1 = blob["x"], blob["y"]
        boxes.append((x1, y1, x1 + blob["w"], y1 + blob["h"]))
    return boxes
