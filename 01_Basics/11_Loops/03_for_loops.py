#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：for 循环（for loops）
Author: Lambert

你会学到：
1) for 的本质：遍历“可迭代对象”（iterable），底层是 iter()/next()
2) range：`range(stop)` / `range(start, stop)` / `range(start, stop, step)`
3) enumerate：拿到索引 + 元素
4) zip：并行遍历（建议 `strict=True` 避免长度不一致悄悄丢数据）
5) dict 遍历：`for k in d`、`for k, v in d.items()`
6) for ... else：常用于“查找/验证”，未 break 时执行 else

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/03_for_loops.py
"""

from __future__ import annotations

from collections.abc import Iterable


def manual_for(iterable: Iterable[object]) -> list[object]:
    it = iter(iterable)
    out: list[object] = []
    while True:
        try:
            out.append(next(it))
        except StopIteration:
            break
    return out


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            break
    else:
        return True
    return False


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 遍历序列/字符串")
    for ch in "abc":
        print("ch =", ch)
    for x in [10, 20, 30]:
        print("x =", x)

    show("2) range：区间迭代（stop 不包含）")
    print("range(5) ->", list(range(5)))
    print("range(2, 8) ->", list(range(2, 8)))
    print("range(10, 0, -3) ->", list(range(10, 0, -3)))

    show("3) enumerate：拿到索引")
    names = ["Alice", "Bob", "Carol"]
    for i, name in enumerate(names, start=1):
        print(i, name)

    show("4) zip：并行遍历（strict=True 更安全）")
    a = [1, 2, 3]
    b = ["x", "y", "z"]
    for n, s in zip(a, b, strict=True):
        print(n, s)

    show("5) dict 遍历")
    m = {"a": 1, "b": 2}
    print("keys:")
    for k in m:
        print("-", k)
    print("items:")
    for k, v in m.items():
        print(f"- {k} -> {v}")

    show("6) for-else：素数判断（未 break 才算 prime）")
    for n in [1, 2, 3, 4, 9, 13]:
        print(n, "prime?", is_prime(n))

    show("7) for 的本质：iter/next")
    print("manual_for([1,2,3]) ->", manual_for([1, 2, 3]))

    show("8) for 的变量作用域：循环变量在循环后仍然存在")
    for x in [10, 20, 30]:
        pass
    print("after loop, x ->", x)

    show("9) 常见坑：遍历时修改列表会导致跳元素")
    items = [1, 2, 3, 4, 5]
    removed: list[int] = []
    for n in items:
        if n % 2 == 0:
            items.remove(n)  # 演示：不推荐
            removed.append(n)
    print("removed evens ->", removed)
    print("items after remove in-loop ->", items, "（注意：结果可能不符合直觉）")

    safe = [n for n in [1, 2, 3, 4, 5] if n % 2 != 0]
    print("safe filter (build new list) ->", safe)


if __name__ == "__main__":
    main()