#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 类与对象（Classes）示例索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/20_Classes/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_class_basics_init.py", "class 与 __init__：实例、属性、方法"),
    ("03_class_attributes_and_methods.py", "类属性/实例属性、classmethod/staticmethod、@property"),
    ("04_inheritance_and_polymorphism.py", "继承与多态：重写、super、isinstance"),
    ("05_dataclass_basics.py", "dataclass：自动生成 __init__/__repr__/__eq__"),
    ("06_magic_methods_text_and_compare.py", "常见魔法方法：__repr__/__str__/__format__/__eq__/__lt__/__hash__"),
    ("07_magic_methods_container_and_iter.py", "容器与迭代：__len__/__bool__/__getitem__/__iter__/__next__/__contains__"),
    ("08_magic_methods_context_and_call.py", "上下文与可调用：__enter__/__exit__/__call__"),
    ("09_magic_methods_attribute_and_slots.py", "属性访问与限制：__getattr__/__setattr__/__delattr__/__slots__"),
    ("11_magic_methods_numeric_and_conversion.py", "数值与转换：__add__/__sub__/__mul__/__truediv__/__index__/__bytes__/__fspath__"),
    ("12_magic_methods_object_lifecycle_and_attribute.py", "生命周期与访问：__new__/__del__/__getattribute__"),
    ("13_magic_methods_container_advanced.py", "容器进阶：__delitem__/__reversed__"),
    ("14_magic_methods_async_context.py", "异步上下文：__aenter__/__aexit__"),
    ("15_magic_methods_copy_and_pickle.py", "拷贝与序列化：__copy__/__deepcopy__/__getstate__/__reduce__"),
    ("16_magic_methods_descriptor_and_match.py", "描述符与模式匹配：__get__/__set__/__delete__/__match_args__"),
    ("10_chapter_summary.py", "本章总结：关键规则 + 常见误区（可最后回顾）"),
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