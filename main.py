#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

The entry is the newspaper front page in entry.png beside this file:
50 sourced stories from Thursday 19 November 2026, with the Shenzhen
summit as the lead, a drawn photo band, 12 illustrated briefs and 35
in-brief lines. The program copies it to the output directory the
grader provides (/output, or MAKEFUN_OUTPUT_DIR outside the container):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def copy_entry(out_dir):
    """Copy entry.png to out_dir and verify it landed whole."""
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    if not os.path.exists(src):
        raise SystemExit("entry.png missing beside main.py")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        head = fh.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        raise SystemExit("copied entry.png is not a PNG")
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy is incomplete")
    return dst


def main(argv):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if len(argv) > 1:
        out_dir = argv[1]
    dst = copy_entry(out_dir)
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
