#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：CSV 流式过滤/聚合，不全量加载。
Author: Lambert
"""

from __future__ import annotations

import csv
from pathlib import Path


def write_big(path: Path) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "score"])
        for i in range(1, 6):
            writer.writerow([f"user{i}", i * 10])


def filter_scores(path: Path) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        high = [row for row in reader if int(row["score"]) >= 30]
    print("分数>=30 ->", high)


def stream_sum(path: Path) -> None:
    total = 0
    count = 0
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += int(row["score"])
            count += 1
    print("平均分 ->", total / count if count else 0)


def main() -> None:
    base = Path(__file__).resolve().parent
    csv_path = base / "scores.csv"
    write_big(csv_path)
    filter_scores(csv_path)
    stream_sum(csv_path)
    csv_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()