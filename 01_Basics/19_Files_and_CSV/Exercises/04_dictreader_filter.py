#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：DictReader 过滤行并写出新文件。
Author: Lambert
"""

from __future__ import annotations

import csv
from pathlib import Path


def filter_csv(src: Path, dst: Path, min_score: int = 60) -> None:
    with src.open("r", encoding="utf-8", newline="") as fin, dst.open("w", encoding="utf-8", newline="") as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=reader.fieldnames or [])
        writer.writeheader()
        for row in reader:
            if int(row.get("score", 0)) >= min_score:
                writer.writerow(row)


def main() -> None:
    base = Path(__file__).resolve().parent
    src = base / "scores.csv"
    dst = base / "filtered.csv"
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(
            [
                {"name": "Alice", "score": 80},
                {"name": "Bob", "score": 50},
                {"name": "Charlie", "score": 90},
            ]
        )
    filter_csv(src, dst)
    print("过滤后内容 ->", dst.read_text(encoding="utf-8"))
    src.unlink(missing_ok=True)
    dst.unlink(missing_ok=True)


if __name__ == "__main__":
    main()