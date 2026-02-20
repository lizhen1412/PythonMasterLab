#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：真值测试 + 组合条件（truthiness / and-or-not / in / is / 优先级）
Author: Lambert

你会学到：
1) `if x:` 等价于 `if bool(x):`；哪些值是 falsy
2) `and/or` 会短路，并且返回的是对象（不一定是 bool）
3) `x or default` 不是 None 合并（0/""/False 会误触发）
4) `in` 在 dict 上检查的是 key；`is None` 是判断 None 的推荐写法
5) 条件里最容易误判的优先级：not/and/or 与比较

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/06_truthiness_and_condition_building.py
"""

from __future__ import annotations

import re


class Box:
    def __init__(self, n: int) -> None:
        self.n = n

    def __len__(self) -> int:  # truthiness fallback: __bool__ -> __len__
        return self.n


def probe(name: str, value: object) -> object:
    print(f"probe({name}) called")
    return value


def coalesce_none(value: object, default: object) -> object:
    return default if value is None else value


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) falsy 清单（常见）")
    samples: list[object] = [None, False, 0, 0.0, "", [], {}, set(), (), Box(0), Box(3)]
    for s in samples:
        print(f"{type(s).__name__:<8} {s!r:<12} -> bool={bool(s)}")

    show("2) 短路：and/or 不一定会执行右侧")
    print("False and probe('R', 123) ->", False and probe("R", 123))
    print("True  or  probe('R', 123) ->", True or probe("R", 123))
    print("True and probe('R', 123) ->", True and probe("R", 123))
    print("False or  probe('R', 123) ->", False or probe("R", 123))

    show("3) 返回值：and/or 返回的是对象")
    print("0 or 99 ->", 0 or 99)
    print("'' or 'fallback' ->", "" or "fallback")
    print("'hi' and 123 ->", "hi" and 123)
    print("[] and 123 ->", [] and 123)

    show("4) 常见坑：or 不是 None 合并")
    print("0 or 10 ->", 0 or 10, "（0 被当成 False）")
    print("coalesce_none(0, 10) ->", coalesce_none(0, 10))
    print("coalesce_none(None, 10) ->", coalesce_none(None, 10))

    show("5) in / is 的常见用法")
    m = {"a": 1, "b": 2}
    print("'a' in m ->", "a" in m)
    print("1 in m ->", 1 in m, "（不会检查 value）")
    x = None
    print("x is None ->", x is None)

    show("6) 优先级：not/and/or 与比较")
    print("not 1 == 2 ->", not 1 == 2, "（等价于 not (1 == 2)）")
    print("False or True and False ->", False or True and False, "（等价于 False or (True and False)）")

    show("7) := 在条件里（常见：先绑定再判断）")
    text = "User: alice"
    if (m := re.search(r"User:\\s*(\\w+)", text)):
        print("matched user ->", m.group(1))
    else:
        print("no match")

    show("8) any/all：把多个条件组合成一个判断")
    nums = [1, 2, 3]
    nums2 = [1, 0, 3]
    print("nums =", nums, "all(n > 0) ->", all(n > 0 for n in nums))
    print("nums2 =", nums2, "all(n > 0) ->", all(n > 0 for n in nums2))
    print("nums2 any(n == 0) ->", any(n == 0 for n in nums2))


if __name__ == "__main__":
    main()