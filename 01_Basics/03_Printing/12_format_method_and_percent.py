#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：历史格式化方式（为了“看懂旧代码”也必须会）

现代 Python 最推荐 f-string（见 05），但你在真实项目里仍会看到：
1) `str.format()` / `format_map()`
2) `%`（printf 风格格式化）

本示例只做一件事：把多个变量**格式化成一行字符串**并输出。

运行：
    python3 01_Basics/03_Printing/12_format_method_and_percent.py
"""


def main() -> None:
    name = "Alice"
    age = 20
    score = 98.5

    print("1) str.format()：按位置填充：")
    print("name={} age={} score={:.1f}".format(name, age, score))

    print("\n2) str.format()：按名字填充（更可读）：")
    print("name={name} age={age} score={score:.1f}".format(name=name, age=age, score=score))

    print("\n3) format_map：用 dict 一次性喂进去：")
    data = {"name": name, "age": age, "score": score}
    print("name={name} age={age} score={score:.1f}".format_map(data))

    print("\n4) % 格式化：你会在更老的代码里见到：")
    print("name=%s age=%d score=%.1f" % (name, age, score))

    print("\n5) %r vs %s：调试时 %r 更接近 repr：")
    text = "hello\n"
    print("text=%s" % text)
    print("text=%r" % text)

    print("\n6) 输出字面量花括号/百分号：")
    print("format: {{ and }} -> {}".format("{", "}"))
    print("percent: 100%% done")


if __name__ == "__main__":
    main()

