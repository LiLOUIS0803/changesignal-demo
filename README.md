# changesignal-demo

A tiny, pure-Python (3.11, standard library only) image pipeline used to try out
ChangeSignal in a user test.

## What the pipeline does

```
data/sample.json ──> candidates.py ──> preprocess.py (shared) ──> scoring.py ──> selected box
                     generate_candidates   crop_regions             select_best
```

1. `pipeline/candidates.py` turns a fake "image" (a dict of rectangular blobs) into candidate boxes `(x1, y1, x2, y2)`.
2. `pipeline/preprocess.py` is **shared** code: `crop_regions(image, boxes)` returns one crop per box, in the same order.
3. `pipeline/scoring.py` scores every crop against the query object and returns the best box.

## How to run

```
python run.py                        # prints the selected box for data/sample.json
python -m pytest -q                  # or: python -m unittest discover -s tests
```

Expected output of `python run.py` ends with `Selected box: (120, 10, 156, 50) -> cup`.

## Roles (who owns what)

Ownership is declared in `.changesignal/modules.yml`.

| Role | Owns | In the test |
|------|------|-------------|
| Author | `pipeline/candidates.py` | Makes a change to the shared pre-processing and opens a PR. |
| Owner | `pipeline/preprocess.py`, `pipeline/scoring.py` | Is asked to review the PR and decides whether to approve. |

When a PR touches files owned by someone else, ChangeSignal posts an impact card on the PR,
requests the owner as reviewer, and keeps the `changesignal/owner-ack` status pending until
the owner approves the current commit.
