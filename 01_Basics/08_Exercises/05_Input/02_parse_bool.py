#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：解析 bool（自定义规则）
Author: Lambert

题目：
实现 `parse_bool(text)`，要求：
- 接收任意字符串，忽略前后空白与大小写
- 支持以下输入：
  - True: y/yes/true/1/on
  - False: n/no/false/0/off
- 其他输入返回 None

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/05_Input/02_parse_bool.py
"""


def parse_bool(text: str) -> bool | None:
    t = text.strip().lower()
    if t in {"y", "yes", "true", "1", "on"}:
        return True
    if t in {"n", "no", "false", "0", "off"}:
        return False
    return None


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("yes", parse_bool(" YES "), True)
    check("no", parse_bool("no"), False)
    check("unknown", parse_bool("maybe"), None)


if __name__ == "__main__":
    main()
