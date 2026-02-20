#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：f-string：一行输出多个变量（推荐方式）
Author: Lambert

你会学到：
1) f-string 最直观：`f\"{name} {age}\"`
2) 调试利器：`f\"{var=}\"`（自动输出 var 的名字和值）
3) `!r`：强制使用 repr（更适合调试/日志）
4) 在一行里打印结构化信息（key=value 风格）

运行：
    python3 01_Basics/03_Printing/05_fstring_and_debug.py
"""


def main() -> None:
    name = "Alice"
    age = 20
    score = 98.5

    print("1) 基础拼接：")
    print(f"name={name} age={age} score={score}")

    print("\n2) {var=} 调试输出：")
    print(f"{name=} {age=} {score=}")

    print("\n3) !r：更“原始”的可读形式（字符串会带引号/转义）：")
    text = "hello\n"
    print(f"{text=}")
    print(f"{text=!r}")

    print("\n4) 格式化规格也能写在 f-string 里：")
    pi = 3.1415926
    print(f"pi={pi:.2f} score={score:6.2f}")


if __name__ == "__main__":
    main()
