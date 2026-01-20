#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：多行输入直到 END（模拟）

题目：
实现 `read_until_end(lines, sentinel="END")`，要求：
- 逐行读取字符串
- strip 后等于 sentinel 就停止（不包含 sentinel 这一行）
- 返回去掉末尾换行后的行列表

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/05_Input/05_multiline_until_end.py
"""


def read_until_end(lines: list[str], sentinel: str = "END") -> list[str]:
    out: list[str] = []
    for line in lines:
        if line.strip() == sentinel:
            break
        out.append(line.rstrip("\n"))
    return out


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    text = read_until_end(["hello\n", "world\n", "END\n", "ignored\n"])
    check("multiline", text, ["hello", "world"])


if __name__ == "__main__":
    main()

