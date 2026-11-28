"""Candidate-region generation.

A box is a tuple (x1, y1, x2, y2): top-left corner inclusive, bottom-right exclusive.
"""


def generate_candidates(image):
    """Return one candidate box per blob in the image, sorted left-to-right (then top-to-bottom).

    The order is deterministic so that every later step sees the same list.
    Candidates may include regions smaller than 32 pixels on either side.
    """
    boxes = []
    for blob in image["blobs"]:
        x1, y1 = blob["x"], blob["y"]
        boxes.append((x1, y1, x1 + blob["w"], y1 + blob["h"]))
    return sorted(boxes)
