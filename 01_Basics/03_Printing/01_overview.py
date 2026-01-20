#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 打印（Printing）相关示例索引。

本章节聚焦一个目标：**在一行里输出多个内容**（多变量、多对象、结构化数据、格式化输出）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/03_Printing/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_print_multiple_objects.py", "print 基础：一次打印多个对象、sep/end/flush"),
    ("03_unpacking_iterables.py", "打印可迭代对象：print(*items) 与顺序/稳定输出"),
    ("04_join_vs_sep.py", "拼接一行字符串：join vs sep（含非字符串元素）"),
    ("05_fstring_and_debug.py", "f-string：一行输出多个变量、{var=}、!r"),
    ("06_format_spec_mini_language.py", "格式化规格：对齐/宽度/精度/千分位/百分比"),
    ("07_print_dicts_key_values.py", "打印 dict：k=v、一行 JSON、一行 querystring"),
    ("08_repr_str_and_custom_objects.py", "str vs repr：对象如何决定打印效果"),
    ("09_same_line_update.py", "同一行刷新输出：进度条、\\r 与 flush"),
    ("10_print_to_file_and_capture.py", "打印到文件/缓冲区：file 参数与捕获输出"),
    ("11_common_mistakes.py", "常见错误：+ 拼接、join 非字符串、sep 类型错误等"),
    ("12_format_method_and_percent.py", "旧格式化：str.format / format_map / %（为了看懂旧代码）"),
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
