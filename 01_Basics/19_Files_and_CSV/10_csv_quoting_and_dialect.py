#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：quoting/delimiter/quotechar，Sniffer。
Author: Lambert
"""

from __future__ import annotations

import csv
from pathlib import Path


def write_custom(path: Path) -> None:
    rows = [
        ["name", "note"],
        ["Alice", '喜欢, "苹果"'],
        ["Bob", "换行\n测试"],
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL, escapechar="\\")
        writer.writerows(rows)


def sniff_and_read(path: Path) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        sample = f.read(200)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample)
        has_header = csv.Sniffer().has_header(sample)
        print("sniff delimiter ->", dialect.delimiter, "has_header?", has_header)
        reader = csv.reader(f, dialect)
        for row in reader:
            print("row ->", row)


def main() -> None:
    base = Path(__file__).resolve().parent
    csv_path = base / "custom.csv"
    write_custom(csv_path)
    sniff_and_read(csv_path)
    csv_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()