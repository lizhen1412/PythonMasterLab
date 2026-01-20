#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：行尾注释规范、括号隐式换行、反斜杠续行陷阱。

要点：
1) 行尾注释推荐与语句之间留两个空格（PEP 8 习惯）。
2) 在 `()[]{}` 里可以“隐式换行”，并可在元素后写行尾注释。
3) 反斜杠 `\\` 做“显式续行”时：反斜杠必须是行末最后一个字符，
   因此 `\\  # comment` 会导致 SyntaxError（因为 # 前有空格/内容）。
"""

from __future__ import annotations


def demonstrate_implicit_line_joining() -> None:
    numbers = [
        1,  # 第一个元素
        2,  # 第二个元素
        3,
    ]

    config = {
        "host": "127.0.0.1",  # 本地回环
        "port": 8080,
    }

    total = (
        10
        + 20  # 在括号内，换行与注释都很自然
        + 30
    )

    print("numbers =", numbers)
    print("config  =", config)
    print("total   =", total)


def demonstrate_backslash_pitfall() -> None:
    bad_code = "x = 1 + \\\\  # 这里不能写注释\\n2\\n"
    print("\n尝试编译一段“反斜杠续行 + 行尾注释”的错误示例：")
    print(bad_code)

    try:
        compile(bad_code, "<bad_code>", "exec")
    except SyntaxError as exc:
        print("SyntaxError:", exc.msg)

    good_code = "x = (1 + 2 + 3)  # 推荐用括号隐式换行\\n"
    print("\n推荐写法（括号隐式换行/或不换行）：")
    print(good_code)
    compile(good_code, "<good_code>", "exec")
    print("编译通过。")


def main() -> None:
    demonstrate_implicit_line_joining()
    demonstrate_backslash_pitfall()


if __name__ == "__main__":
    main()
