"""Candidate-region generation.

A box is a tuple (x1, y1, x2, y2): top-left corner inclusive, bottom-right exclusive.
"""


def generate_candidates(image):
    """Return boxes at least 32 pixels on both sides, in deterministic order."""
    min_side = 32
    boxes = []
    for blob in image["blobs"]:
        width, height = blob["w"], blob["h"]
        if width < min_side or height < min_side:
            continue
        x1, y1 = blob["x"], blob["y"]
        boxes.append((x1, y1, x1 + width, y1 + height))
    return sorted(boxes)
