#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 格式化输出（Formatting）相关示例索引。

本章节目标：把“所有常见输出格式化方式”一次讲清楚，并给出可运行的学习案例。

运行方式（在仓库根目录执行）：
    python3 01_Basics/04_Formatting/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_str_repr_ascii.py", "str/repr/ascii：人读 vs 调试读"),
    ("03_fstrings_basics.py", "f-string：表达式、{var=}、!r/!s/!a、转义大括号"),
    ("04_format_spec_integers.py", "格式化规格：整数（进制/对齐/填充/分组/符号）"),
    ("05_format_spec_floats_and_decimal.py", "格式化规格：浮点/Decimal（精度/科学计数/百分比）"),
    ("06_format_spec_strings.py", "格式化规格：字符串（宽度/对齐/截断）"),
    ("07_format_and___format__.py", "format() 与 __format__：自定义对象格式化"),
    ("08_str_format_and_format_map.py", "str.format/format_map：位置/命名/属性/索引字段"),
    ("09_percent_formatting.py", "旧式 % 格式化：tuple/dict 两种风格"),
    ("10_string_template.py", "string.Template：$name 替换与 safe_substitute"),
    ("11_datetime_formatting.py", "datetime：strftime、f\"{dt:%Y-%m-%d}\"、isoformat"),
    ("12_pprint_json_reprlib.py", "结构化输出：pprint/json/reprlib（可读/可机器解析）"),
    ("13_textwrap_and_layout.py", "文本排版：textwrap 换行/缩进 + 简单列布局"),
    ("14_logging_formatting.py", "日志格式化：logging 的 Formatter 与推荐写法"),
    ("15_common_pitfalls_and_escaping.py", "常见坑：转义、类型不匹配、格式码错误等（安全演示）"),
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
