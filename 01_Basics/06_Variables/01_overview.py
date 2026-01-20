#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 变量（Variables）相关示例索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/06_Variables/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_variable_creation.py", "变量创建：赋值、解包、注解、名字绑定对象"),
    ("03_variable_modification.py", "变量修改：重新绑定 vs 原地修改（可变性与别名）"),
    ("04_variable_naming.py", "变量命名：合法标识符、关键字、命名约定、避免遮蔽"),
    ("05_variable_types_runtime.py", "变量类型：type/isinstance、动态类型、bool 是 int 子类等"),
    ("06_type_conversions.py", "类型转换：int/float/str/Decimal/bool（含安全解析）"),
    ("07_type_annotations.py", "类型注解：注解语法、__annotations__、get_type_hints、cast"),
    ("08_scope_and_lifetime.py", "作用域与生命周期：LEGB、global/nonlocal、del、locals/globals"),
    ("09_assignment_targets.py", "赋值目标：属性/下标/切片/解包目标（更像“写到哪里”）"),
    ("10_common_pitfalls.py", "常见坑：is vs ==、链式赋值、可变默认参数、闭包晚绑定"),
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

