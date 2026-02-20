#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：捕获 print 输出（StringIO）
Author: Lambert

题目：
实现 `capture_print(*args, **kwargs) -> str`，要求：
- 内部使用 `io.StringIO()` 作为 `print(..., file=buf)`
- 返回最终字符串（包含 end 的内容，但不额外 strip）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/03_Printing/02_capture_print_output.py
"""

import io


def capture_print(*args: object, **kwargs: object) -> str:
    buf = io.StringIO()
    print(*args, file=buf, **kwargs)
    return buf.getvalue()


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    out = capture_print("a", "b", 123, sep="|", end=" END")
    check("capture", out, "a|b|123 END")


if __name__ == "__main__":
    main()
