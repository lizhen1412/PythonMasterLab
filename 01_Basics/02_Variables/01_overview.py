#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 变量（Variables）相关示例索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/02_Variables/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_variable_basics.py", "变量是什么：名字绑定对象、id/type、重新绑定"),
    ("03_identifiers_and_naming.py", "标识符规则与命名约定（PEP 8 风格）"),
    ("04_assignment_unpacking.py", "赋值与解包：多重赋值、星号解包、交换变量"),
    ("05_assignment_targets.py", "赋值目标：变量名/属性/下标/切片"),
    ("06_chained_assignment_and_aliasing.py", "链式赋值与别名陷阱：a = b = []"),
    ("07_augmented_assignment_and_mutability.py", "增强赋值：+= 的“原地修改”与新对象"),
    ("08_copying_shallow_vs_deep.py", "复制：浅拷贝 vs 深拷贝"),
    ("09_scopes_LEGB_global_nonlocal.py", "作用域：LEGB、global、nonlocal（含安全演示）"),
    ("10_loop_and_comprehension_scope.py", "循环/推导式的变量作用域差异"),
    ("11_walrus_operator.py", "海象运算符 :=（赋值表达式）与作用域细节"),
    ("12_type_annotations_and_constants.py", "变量类型注解、__annotations__、Final/ClassVar"),
    ("13_print_basics.py", "print 基础：sep/end/file/flush"),
    ("14_string_formatting_fstrings.py", "格式化输出：f-string、repr/str、格式化规格"),
    ("15_common_pitfalls.py", "常见坑：可变默认参数、闭包晚绑定等"),
    ("16_match_case_and_as_binding.py", "进阶绑定：match/case、with/except 的 as 绑定"),
    ("17_globals_locals_and_del.py", "globals/locals 与 del：名字删除 vs 对象是否还在"),
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