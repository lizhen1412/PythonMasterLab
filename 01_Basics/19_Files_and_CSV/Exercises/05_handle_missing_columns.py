#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：处理缺失列/空行，容错输出。
Author: Lambert
"""

from __future__ import annotations

import csv
from pathlib import Path


def clean_csv(src: Path, dst: Path) -> None:
    with src.open("r", encoding="utf-8", newline="") as fin, dst.open("w", encoding="utf-8", newline="") as fout:
        reader = csv.DictReader(fin)
        fieldnames = reader.fieldnames or []
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if not any(row.values()):
                continue
            cleaned = {k: (v or "").strip() for k, v in row.items()}
            writer.writerow(cleaned)


def main() -> None:
    base = Path(__file__).resolve().parent
    src = base / "raw.csv"
    dst = base / "clean.csv"
    src.write_text("name,score\nAlice,80\n, \nBob,\n", encoding="utf-8")
    clean_csv(src, dst)
    print("cleaned ->", dst.read_text(encoding="utf-8"))
    src.unlink(missing_ok=True)
    dst.unlink(missing_ok=True)


if __name__ == "__main__":
    main()