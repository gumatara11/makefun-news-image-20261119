#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a front page summing up
the world's news of Thursday 19 November 2026. The program copies it to
/output/entry.png. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst = os.path.join(out_dir, "entry.png")
shutil.copyfile(src, dst)
# The entry must be byte-identical on every run: confirm the copy landed whole.
assert os.path.getsize(dst) == os.path.getsize(src), "entry.png copy is incomplete"
print("wrote", dst, os.path.getsize(dst), "bytes")
