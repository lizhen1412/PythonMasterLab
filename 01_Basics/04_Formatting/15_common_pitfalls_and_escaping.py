#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：格式化输出的常见坑（不会让脚本崩：我们用 try/except 演示）。

你会学到：
1) 忘写 f：`"{x}"` 不会插值
2) 大括号转义：`{{` / `}}`
3) format spec 不匹配类型：例如对 str 用 `:.2f`
4) format_map 缺字段：用 safe 的方式处理（或换 Template.safe_substitute）
5) 反例里用到 `typing.cast` 让静态类型检查器不告警（注意：cast 不会做运行时类型转换）

运行：
    python3 01_Basics/04_Formatting/15_common_pitfalls_and_escaping.py
"""

from typing import cast


def main() -> None:
    x = 3.1415926

    print("1) 忘写 f：")
    print('"{x}" ->', "{x}")
    print('f"{x}" ->', f"{x}")

    print("\n2) 大括号转义：")
    print("literal:", f"{{x}} means 'x', not value")

    print("\n3) format spec 不匹配类型：")
    try:
        s = "hello"
        print(f"{cast(float, s):.2f}")
    except ValueError as exc:
        print("ValueError:", exc)

    print("\n4) 缺字段：format_map 会 KeyError（捕获演示）：")
    tpl = "name={name} age={age}"
    try:
        print(tpl.format_map({"name": "Alice"}))
    except KeyError as exc:
        print("KeyError:", exc)
        print("解决思路：补齐字段 / 使用 Template.safe_substitute / 自己做默认值逻辑")

    print("\n5) 数值格式码错误（捕获演示）：")
    try:
        print(f"{x:unknown}")
    except ValueError as exc:
        print("ValueError:", exc)


if __name__ == "__main__":
    main()
