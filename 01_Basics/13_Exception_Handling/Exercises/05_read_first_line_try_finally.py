#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：try/finally 做资源清理（read first line）
Author: Lambert

题目：
实现函数 `read_first_line(path)`：
- 返回文件的第一行（去掉末尾换行符）
- 要求：用 try/finally 保证文件一定被关闭（即使中途 return）

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]），并在最后清理临时文件。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/05_read_first_line_try_finally.py
"""

from __future__ import annotations

from pathlib import Path


def read_first_line(path: Path) -> str:
    f = path.open("r", encoding="utf-8")
    try:
        return f.readline().rstrip("\n")
    finally:
        f.close()


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def check_raises(label: str, fn, exc_type: type[BaseException]) -> None:
    try:
        fn()
    except exc_type:
        print(f"[OK] {label}: raised {exc_type.__name__}")
    except Exception as exc:
        print(f"[FAIL] {label}: raised {type(exc).__name__}, expected {exc_type.__name__}")
    else:
        print(f"[FAIL] {label}: no exception, expected {exc_type.__name__}")


def main() -> None:
    tmp = Path(__file__).with_name("_tmp_first_line.txt")
    tmp.write_text("hello\\nworld\\n", encoding="utf-8")
    try:
        check("read_first_line(tmp)", read_first_line(tmp), "hello")
        check_raises("read_first_line(missing)", lambda: read_first_line(tmp.with_name("no_such.txt")), FileNotFoundError)
    finally:
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
