#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：拼接一行字符串：join vs sep

你会学到：
1) `print(*items, sep=", ")`：print 自己会对每个元素做 str()，很省心
2) `", ".join(items)`：join 要求元素必须全是 str（否则 TypeError）
3) 非字符串元素用 `map(str, items)` 转换
4) 在需要“得到字符串”而不是“直接打印”时，join 更合适
5) 反例里用到 `typing.cast` 让静态类型检查器不告警（注意：cast 不会做运行时类型转换）

运行：
    python3 01_Basics/03_Printing/04_join_vs_sep.py
"""

from typing import cast


def main() -> None:
    nums = [1, 2, 3]

    print("1) 用 print + sep：")
    print(*nums, sep=", ")

    print("\n2) join（需要先把元素变成 str）：")
    line = ", ".join(map(str, nums))
    print(line)

    print("\n3) join 的常见坑：元素不是 str 会报错（这里捕获演示）：")
    try:
        _ = ", ".join(cast(list[str], nums))
    except TypeError as exc:
        print("TypeError:", exc)

    print("\n4) 想得到一行字符串（后续写日志/写文件/网络发送）时：")
    name = "Alice"
    age = 20
    msg = " ".join([f"name={name}", f"age={age}"])
    print("msg =", msg)


if __name__ == "__main__":
    main()
