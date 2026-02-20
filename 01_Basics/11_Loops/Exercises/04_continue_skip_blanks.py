#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：continue（过滤空白并规范化）
Author: Lambert

题目：
实现 `normalize_lines(lines)`，要求：
- 输入：list[str]
- 对每一行做 strip
- strip 后为空字符串的行要跳过（用 continue）
- 返回：规范化后的非空行列表

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/11_Loops/Exercises/04_continue_skip_blanks.py
"""

from __future__ import annotations


def normalize_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        out.append(s)
    return out


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    lines = ["", "  ", "Alice", "  Bob  ", "\n", "Carol"]
    check("normalize", normalize_lines(lines), ["Alice", "Bob", "Carol"])


if __name__ == "__main__":
    main()
