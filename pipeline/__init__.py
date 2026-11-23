"""Tiny image pipeline: candidate regions -> shared pre-processing -> similarity scoring.

An "image" here is a small fake: a dict with a size, a background value and a list of
rectangular blobs (each with a brightness value). No real image library is needed.
"""
