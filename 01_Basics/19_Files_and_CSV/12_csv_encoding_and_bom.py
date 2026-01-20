#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：编码/BOM，空行处理。
"""

from __future__ import annotations

import csv
from pathlib import Path


def write_with_bom(path: Path) -> None:
    data = "name,城市\nAlice,北京\nBob,上海\n"
    path.write_bytes(data.encode("utf-8-sig"))


def read_utf8_sig(path: Path) -> None:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            print("row ->", row)


def write_without_bom(path: Path) -> None:
    rows = [["name", "city"], ["Charlie", "Shenzhen"]]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def main() -> None:
    base = Path(__file__).resolve().parent
    bom_path = base / "with_bom.csv"
    write_with_bom(bom_path)
    print("读取带 BOM 文件（utf-8-sig）")
    read_utf8_sig(bom_path)

    clean_path = base / "clean.csv"
    write_without_bom(clean_path)
    print("写入无 BOM UTF-8 文件 ->", clean_path)

    bom_path.unlink(missing_ok=True)
    clean_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
