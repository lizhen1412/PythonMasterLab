#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：DictReader/DictWriter，writeheader、缺字段处理。
Author: Lambert
"""

from __future__ import annotations

import csv
from pathlib import Path


def write_dicts(path: Path) -> None:
    rows = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "city": "Shanghai"},  # 缺 age
    ]
    fieldnames = ["name", "age", "city"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_dicts(path: Path) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print("dict row ->", row)


def main() -> None:
    base = Path(__file__).resolve().parent
    csv_path = base / "dicts.csv"
    write_dicts(csv_path)
    read_dicts(csv_path)
    csv_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()