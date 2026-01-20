#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：变量（入门，06_Variables）练习索引（每题一个文件）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/08_Exercises/06_Variables/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_is_vs_eq_identity.py", "is vs ==：身份与值的区别"),
    ("03_variable_name_validation.py", "变量名合法性：isidentifier + keyword + 避免遮蔽 builtins"),
    ("04_type_checks_and_bool_is_int.py", "type/isinstance：bool 是 int 子类（判断顺序很关键）"),
    ("05_type_annotations_introspection.py", "类型注解：__annotations__ 与 get_type_hints"),
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

