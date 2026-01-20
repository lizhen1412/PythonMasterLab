#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：字典 dict（映射：key -> value）

你会学到：
1) 创建：字面量/dict()/推导式/dict(zip())
2) 访问：[] vs get
3) 更新：赋值/update/合并 | 与 |=（Py 3.9+）
4) 删除：del/pop/popitem/clear
5) 遍历：keys/values/items（in 检查的是 key）
6) 常见套路：计数与分组（get/setdefault）

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/09_dict_basics.py
"""

from __future__ import annotations


def count_words(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for w in words:
        key = w[:1]
        groups.setdefault(key, []).append(w)
    return groups


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) 创建")
    a = {"a": 1, "b": 2}
    b = dict(a=1, b=2)
    c = {k: k.upper() for k in ["a", "b"]}
    d = dict(zip(["x", "y"], [10, 20], strict=True))
    print("a ->", a)
    print("b ->", b)
    print("c ->", c)
    print("d ->", d)

    show("2) 访问：[] vs get")
    print("a['a'] ->", a["a"])
    print("a.get('missing', 0) ->", a.get("missing", 0))

    show("3) 更新：赋值/update/合并")
    a["c"] = 3
    a.update({"d": 4})
    merged = a | {"e": 5}
    a |= {"f": 6}
    print("a after update ->", a)
    print("merged ->", merged)

    show("4) 删除：pop/popitem")
    x = a.pop("a")
    print("pop('a') ->", x, "remaining ->", a)
    k, v = a.popitem()
    print("popitem() ->", (k, v), "remaining ->", a)

    show("5) 遍历：in 检查 key")
    m = {"a": 1, "b": 2}
    print("'a' in m ->", "a" in m)
    print("1 in m ->", 1 in m, "（不会检查 value）")
    for k, v in m.items():
        print(f"- {k} -> {v}")

    show("6) 常见套路：计数/分组")
    words = ["apple", "ape", "banana", "book", "apple"]
    print("count_words ->", count_words(words))
    print("group_by_first_letter ->", group_by_first_letter(words))


if __name__ == "__main__":
    main()

