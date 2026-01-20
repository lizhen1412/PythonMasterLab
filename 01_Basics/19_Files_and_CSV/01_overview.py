#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：文件与 CSV 章节索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/19_Files_and_CSV/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_paths_and_traversal.py", "Path 基础、遍历、stat 元数据"),
    ("03_open_modes_and_context.py", "打开模式/编码/newline/buffering，with/seek/tell"),
    ("04_text_read_write_patterns.py", "文本读写：逐行/分块/错误处理"),
    ("05_binary_files_and_seek.py", "二进制读写、偏移读取、seek"),
    ("06_temp_files_and_safe_write.py", "tempfile、临时写后替换"),
    ("07_permissions_and_errors.py", "权限/错误处理：stat、chmod、异常捕获"),
    ("08_csv_reader_writer_basics.py", "csv.reader/writer 基础，newline=\"\""),
    ("09_csv_dictreader_dictwriter.py", "DictReader/DictWriter，writeheader、缺字段"),
    ("10_csv_quoting_and_dialect.py", "quoting/delimiter/quotechar，Sniffer"),
    ("11_csv_streaming_and_filter.py", "CSV 流式过滤/聚合，不全量加载"),
    ("12_csv_encoding_and_bom.py", "编码/BOM，空行处理"),
    ("13_chapter_summary.py", "本章总结：规则清单与常见坑"),
    ("Exercises/01_overview.py", "练习题索引（每题一个文件）"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
