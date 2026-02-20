#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 函数（Functions）章节索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/14_Functions/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_function_basics_def_call_return.py", "函数定义/调用/返回值，docstring 与类型注解"),
    ("03_parameters_and_default_values.py", "参数与默认值：求值时机、可变默认值陷阱与防御"),
    ("04_parameter_kinds_pos_only_kw_only.py", "参数五类：位置/关键字/变参/pos-only/kw-only 的匹配规则"),
    ("05_varargs_kwargs_and_unpacking.py", "`*args/**kwargs` 收集与解包，参数转发与覆盖规则"),
    ("06_scope_and_closure.py", "作用域、`UnboundLocalError`、`global/nonlocal`、闭包与延迟绑定"),
    ("07_lambda_and_first_class_functions.py", "`lambda` 适用场景，函数作为值/参数/返回值"),
    ("08_decorators_and_partial.py", "装饰器最小用法、`functools.wraps`、带参数装饰器、`partial`"),
    ("09_common_builtin_functions.py", "常用内置函数分类：聚合/迭代/数值/函数式，易错点提示"),
    ("13_builtin_functions_reference.py", "内置函数全覆盖：完整清单 + 关键用法示例"),
    ("10_recursive_functions.py", "递归：基线与收敛、调用栈限制、阶乘/斐波那契/树深度"),
    ("11_chapter_summary.py", "本章总结：规则清单与常见误区"),
    ("12_card_management_system.py", "综合示例：函数化的名片管理（增删改查、格式化输出）"),
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