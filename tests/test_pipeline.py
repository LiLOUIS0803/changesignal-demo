"""Smoke tests for the pipeline. Run with:  python -m pytest -q   (or  python -m unittest discover -s tests)"""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pipeline.candidates import generate_candidates  # noqa: E402
from pipeline.preprocess import crop_regions  # noqa: E402
from pipeline.scoring import select_best  # noqa: E402


def load_sample():
    return json.loads((ROOT / "data" / "sample.json").read_text(encoding="utf-8"))


class PipelineSmokeTest(unittest.TestCase):
    def test_candidates_are_boxes(self):
        boxes = generate_candidates(load_sample())
        self.assertTrue(boxes)
        for box in boxes:
            self.assertEqual(len(box), 4)

    def test_crops_are_2d(self):
        image = load_sample()
        crops = crop_regions(image, generate_candidates(image))
        self.assertTrue(crops)
        for crop in crops:
            self.assertTrue(crop and crop[0])

    def test_select_best_returns_a_box(self):
        image = load_sample()
        best = select_best(image, generate_candidates(image))
        self.assertEqual(len(best), 4)
        self.assertTrue(all(isinstance(v, int) for v in best))


if __name__ == "__main__":
    unittest.main()
