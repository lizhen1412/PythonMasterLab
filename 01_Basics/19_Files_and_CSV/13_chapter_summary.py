#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：本章总结与常见坑。
Author: Lambert
"""

from __future__ import annotations


RULES = [
    "使用 pathlib.Path 操作路径更直观；需要读取 CSV 记得 newline=\"\"",
    "文本文件指定 encoding（默认 UTF-8），错误处理可用 errors 参数",
    "大文件优先逐行/分块处理，避免一次性读入",
    "写文件建议 with 上下文确保关闭；必要时采用“临时文件+替换”减少损坏风险",
    "CSV 读写使用 csv 模块，DictReader/DictWriter 可按列名访问",
    "quoting/delimiter/quotechar 需与数据匹配；Sniffer 可尝试自动识别",
    "读取带 BOM 文件用 utf-8-sig；写回时可用纯 utf-8",
    "权限/缺失文件要捕获 PermissionError/FileNotFoundError，避免程序崩溃",
]


PITFALLS = [
    "忘记 newline=\"\" 写 CSV 会出现空行",
    "未捕获 UnicodeDecodeError/EncodeError 导致程序中断；errors 可选 ignore/replace",
    "一次 read() 读取大文件耗尽内存；应逐行或分块",
    "写文件异常中断导致半文件；可先写临时文件再 replace",
    "使用 dictwriter 时字段缺失导致 KeyError 或空值；应设默认/跳过",
    "使用 Path.glob('**') 在大目录可能很慢；可限制深度或数量",
]


def main() -> None:
    print("== 规则清单 ==")
    for idx, rule in enumerate(RULES, start=1):
        print(f"{idx:02d}. {rule}")

    print("\n== 常见坑 ==")
    for idx, pitfall in enumerate(PITFALLS, start=1):
        print(f"{idx:02d}. {pitfall}")


if __name__ == "__main__":
    main()