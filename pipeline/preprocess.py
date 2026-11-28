"""Shared pre-processing used by more than one stage of the pipeline."""


def pixel(image, x, y):
    """Brightness (0-255) of one pixel: the blob covering (x, y), else the background."""
    for blob in image["blobs"]:
        if blob["x"] <= x < blob["x"] + blob["w"] and blob["y"] <= y < blob["y"] + blob["h"]:
            return blob["value"]
    return image["background"]


def crop_regions(image, boxes):
    """Cut each box out of the image.

    Returns a list of crops (each crop is a 2D list of pixel values, rows first),
    one crop per box, in the same order as `boxes`.
    """
    crops = []
    for x1, y1, x2, y2 in boxes:
        if x2 - x1 < 32 or y2 - y1 < 32:
            continue
        crop = [[pixel(image, x, y) for x in range(x1, x2)] for y in range(y1, y2)]
        crops.append(crop)
    return crops
