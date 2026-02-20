#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：读取带 BOM 的 CSV，并写回标准 UTF-8。
Author: Lambert
"""

from __future__ import annotations

import csv
from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parent
    src = base / "bom.csv"
    dst = base / "clean.csv"
    data = "name,city\nAlice,北京\nBob,上海\n"
    src.write_bytes(data.encode("utf-8-sig"))

    rows: list[list[str]] = []
    with src.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]

    with dst.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("清理后内容 ->", dst.read_text(encoding="utf-8"))
    src.unlink(missing_ok=True)
    dst.unlink(missing_ok=True)


if __name__ == "__main__":
    main()