#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：旧式 % 格式化（printf 风格）。

你会学到：
1) tuple 风格：`"x=%d y=%s" % (x, y)`
2) dict 风格：`"%(name)s" % {"name": "Alice"}`
3) `%r` 更接近 repr，`%s` 更接近 str
4) 输出字面量 %：写成 `%%`

运行：
    python3 01_Basics/04_Formatting/09_percent_formatting.py
"""


def main() -> None:
    name = "Alice"
    age = 20
    score = 98.5

    print("1) tuple 风格：")
    print("name=%s age=%d score=%.1f" % (name, age, score))

    print("\n2) dict 风格：")
    mapping = {"name": name, "age": age, "score": score}
    print("name=%(name)s age=%(age)d score=%(score).1f" % mapping)

    print("\n3) %r vs %s：")
    text = "hi\n"
    print("as %%s -> %s" % text)
    print("as %%r -> %r" % text)

    print("\n4) 输出字面量 %：")
    print("progress=100%% done")

    print("\n5) 错误示例（捕获异常演示）：")
    try:
        print("age=%d" % "not int")
    except TypeError as exc:
        print("TypeError:", exc)


if __name__ == "__main__":
    main()

