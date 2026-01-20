#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：文件与 CSV 章节练习。

运行方式（在仓库根目录执行）：
    python3 01_Basics/19_Files_and_CSV/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_stream_count_lines.py", "逐行计数（大文件不全量读）"),
    ("03_binary_chunk_read.py", "二进制按块读取并统计长度"),
    ("04_dictreader_filter.py", "DictReader 过滤行并写出新文件"),
    ("05_handle_missing_columns.py", "处理缺失列/空行，容错输出"),
    ("06_sniffer_detect_dialect.py", "Sniffer 推断分隔符与是否有表头"),
    ("07_safe_overwrite.py", "安全写入：临时文件替换原文件"),
    ("08_permissions_error_handling.py", "捕获 FileNotFound/PermissionError"),
    ("09_bom_and_encoding.py", "读取带 BOM 的 CSV，并写回标准 UTF-8"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习题清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
