#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：逐行计数（大文件不全量读）。
"""

from __future__ import annotations

from pathlib import Path


def count_lines(path: Path) -> int:
    count = 0
    with path.open("r", encoding="utf-8") as f:
        for _ in f:
            count += 1
    return count


def main() -> None:
    base = Path(__file__).resolve().parent
    sample = base / "sample.txt"
    sample.write_text("a\nb\nc\n", encoding="utf-8")
    print("行数 ->", count_lines(sample))
    sample.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
