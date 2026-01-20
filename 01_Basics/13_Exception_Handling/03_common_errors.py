#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：异常处理——常见错误（Common Errors）

目标：
- 认识最常见的异常类型与触发方式
- 学会“捕获后打印类型/消息”，但不滥用 try/except 掩盖 bug

运行（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/03_common_errors.py
"""

from __future__ import annotations

from pathlib import Path


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def run_demo(label: str, fn) -> None:
    print(f"\n- {label}")
    try:
        result = fn()
    except Exception as exc:
        print("  捕获到：", type(exc).__name__, "-", exc)
    else:
        print("  OK ->", result)


def main() -> None:
    show("常见异常：触发方式与类型")

    run_demo("NameError：变量未定义", lambda: not_defined_name)  # type: ignore[name-defined]
    run_demo("TypeError：类型不匹配", lambda: 1 + "2")  # type: ignore[operator]
    run_demo("ValueError：值不合法", lambda: int("abc"))
    run_demo("ZeroDivisionError：除 0", lambda: 1 / 0)
    run_demo("IndexError：索引越界", lambda: [1, 2][99])
    run_demo("KeyError：字典 key 不存在", lambda: {"a": 1}["missing"])
    run_demo("AttributeError：对象没有该属性/方法", lambda: None.upper())  # type: ignore[union-attr]
    run_demo("FileNotFoundError：文件不存在", lambda: Path("no_such_file.txt").read_text(encoding="utf-8"))

    def import_missing():
        import importlib

        return importlib.import_module("no_such_module_abc123")

    run_demo("ModuleNotFoundError：导入失败", import_missing)

    show("小结：什么时候 catch？")
    print("- 当你能恢复（提供默认值/重试/提示用户）或需要清理资源时，catch 很有价值。")
    print("- 如果只是为了“程序不报错”，反而会隐藏 bug，后续更难排查。")


if __name__ == "__main__":
    main()

