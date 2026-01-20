#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：print(*items) vs join

题目：
实现 `join_csv(items)`，要求：
- 接收任意对象列表
- 把每个元素转换成 str
- 用 `,` 连接成一行（不带结尾换行）

提示：
- `",".join(items)` 只接受字符串序列；需要先做 `map(str, items)`。

参考答案：
- 本文件函数实现即参考答案；`main()` 会对比 `join_csv` 与 `print(*items, sep=",")` 的效果。

运行：
    python3 01_Basics/08_Exercises/03_Printing/04_unpacking_and_join.py
"""

import io


def join_csv(items: list[object]) -> str:
    return ",".join(map(str, items))


def capture_print_items(items: list[object], sep: str) -> str:
    buf = io.StringIO()
    print(*items, sep=sep, file=buf, end="")
    return buf.getvalue()


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    items: list[object] = ["a", 1, 2.5]
    check("join_csv", join_csv(items), "a,1,2.5")
    check("print_sep", capture_print_items(items, sep=","), "a,1,2.5")


if __name__ == "__main__":
    main()

