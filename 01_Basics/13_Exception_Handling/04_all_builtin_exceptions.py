#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：全部（内置）异常类一览（builtins）

说明：
- Python 的异常类很多，“全部列举”最可靠的方式是：从 `builtins` 里扫描所有 `BaseException` 的子类
- 这不包含标准库/第三方库自定义的异常（例如 socket/requests 等）

你会学到：
1) 如何列出所有内置异常类（按名字排序）
2) 如何以树形结构展示异常继承体系（BaseException -> Exception -> ...）
3) Python 3.11+ 的 ExceptionGroup/except* 在体系里的位置

运行（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/04_all_builtin_exceptions.py
"""

from __future__ import annotations

import builtins
import inspect


def is_builtin_exception_class(obj: object) -> bool:
    return inspect.isclass(obj) and issubclass(obj, BaseException) and getattr(obj, "__module__", None) == "builtins"


def list_builtin_exceptions_by_name() -> list[type[BaseException]]:
    classes: list[type[BaseException]] = []
    for _, obj in vars(builtins).items():
        if is_builtin_exception_class(obj):
            classes.append(obj)
    classes.sort(key=lambda c: c.__name__.lower())
    return classes


def print_exception_tree(root: type[BaseException], indent: str = "") -> None:
    children = [c for c in root.__subclasses__() if getattr(c, "__module__", None) == "builtins"]
    children.sort(key=lambda c: c.__name__.lower())
    for child in children:
        print(f"{indent}- {child.__name__}")
        print_exception_tree(child, indent + "  ")


def main() -> None:
    classes = list_builtin_exceptions_by_name()
    print(f"builtins 中异常类数量: {len(classes)}")
    print()

    print("1) 按名称列出（节选展示 bases）：")
    for cls in classes:
        bases = ", ".join(b.__name__ for b in cls.__bases__)
        print(f"- {cls.__name__} (bases: {bases})")

    print()
    print("2) 继承体系（BaseException 子类树）：")
    print("- BaseException")
    print_exception_tree(BaseException, indent="  ")


if __name__ == "__main__":
    main()

