"""Similarity scoring: pick the candidate that looks most like the query object."""

from pipeline.preprocess import crop_regions


def mean_brightness(crop):
    values = [v for row in crop for v in row]
    return sum(values) / len(values)


def similarity(crop, query_value):
    """1.0 = same mean brightness as the query, 0.0 = as different as possible."""
    return 1.0 - abs(mean_brightness(crop) - query_value) / 255


def select_best(image, boxes):
    """Return the most similar box, or None when there are no candidates."""
    if not boxes:
        return None
    crops = crop_regions(image, boxes)
    scores = [similarity(crop, image["query"]["value"]) for crop in crops]
    best_box, _best_score = max(zip(boxes, scores), key=lambda pair: pair[1])
    return best_box
