#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: shutil + tempfile basics.

Run:
    python3 01_Basics/25_System_Debug_Testing/03_shutil_tempfile_basics.py
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        src = base / "src.txt"
        dst = base / "dst.txt"

        src.write_text("hello", encoding="utf-8")
        shutil.copy2(src, dst)

        print("src ->", src.read_text(encoding="utf-8"))
        print("dst ->", dst.read_text(encoding="utf-8"))
        print("files ->", [p.name for p in base.iterdir()])


if __name__ == "__main__":
    main()
