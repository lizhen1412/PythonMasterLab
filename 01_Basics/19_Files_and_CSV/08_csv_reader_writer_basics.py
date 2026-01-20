#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：csv.reader/writer 基础，newline=""。
"""

from __future__ import annotations

import csv
from pathlib import Path


def write_csv(path: Path) -> None:
    rows = [
        ["name", "age", "city"],
        ["Alice", "30", "Beijing"],
        ["Bob", "25", "Shanghai"],
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def read_csv(path: Path) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print("row ->", row)


def main() -> None:
    base = Path(__file__).resolve().parent
    csv_path = base / "people.csv"
    write_csv(csv_path)
    read_csv(csv_path)
    csv_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
