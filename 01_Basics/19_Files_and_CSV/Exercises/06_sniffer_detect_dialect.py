#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：Sniffer 推断分隔符与是否有表头。
"""

from __future__ import annotations

import csv
from pathlib import Path


def sniff(path: Path) -> None:
    with path.open("r", encoding="utf-8", newline="") as f:
        sample = f.read(200)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample)
        has_header = csv.Sniffer().has_header(sample)
        print("delimiter:", dialect.delimiter, "has_header:", has_header)
        reader = csv.reader(f, dialect)
        for row in reader:
            print("row ->", row)


def main() -> None:
    base = Path(__file__).resolve().parent
    path = base / "mixed.txt"
    path.write_text("name|age\nAlice|30\nBob|25\n", encoding="utf-8")
    sniff(path)
    path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
