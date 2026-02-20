#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：注释（Comments）练习索引（每题一个文件）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/08_Exercises/01_Comments/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_shebang_and_coding_cookie.py", "识别 shebang 与 encoding 声明（coding cookie）"),
    ("03_tokenize_extract_hash_comments.py", "用 tokenize 提取 # 注释（字符串里的 # 不算注释）"),
    ("04_ast_extract_docstrings.py", "用 AST 提取模块/函数 docstring（普通注释不会进入 AST）"),
    ("05_scan_tooling_directives.py", "扫描常见工具指令注释（noqa/fmt/pragma/type: ignore）"),
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
