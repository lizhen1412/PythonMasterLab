#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：集合类方法参数与边界案例（list/tuple/dict/set）
Author: Lambert

你会学到：
1) list/tuple 的 index 支持 start/stop；list.pop 可传索引
2) list.sort 的 key/reverse 与“就地排序返回 None”
3) dict 的 get/pop/setdefault/update/fromkeys 的参数与坑
4) dict 视图（keys/values/items）是动态的
5) set 的 union/intersection/difference 支持多个 iterable；remove vs discard
6) frozenset 的运算返回新对象

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/17_collection_method_variants.py
"""

from __future__ import annotations

from collections.abc import Callable


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo(label: str, value: object) -> None:
    print(f"{label:<36} -> {value!r}")


def try_demo(label: str, func: Callable[[], object]) -> None:
    try:
        value = func()
    except Exception as exc:
        print(f"{label:<36} -> {type(exc).__name__}: {exc}")
        return
    demo(label, value)


def main() -> None:
    show("1) list：参数与边界")
    items = [10, 20, 30, 20, 40]
    demo("index(20)", items.index(20))
    demo("index(20, 2)", items.index(20, 2))
    try_demo("index(20, 4)", lambda: items.index(20, 4))
    try_demo("index(20, 0, 2)", lambda: items.index(20, 0, 2))

    tmp = items.copy()
    demo("pop()", tmp.pop())
    tmp = items.copy()
    demo("pop(1)", tmp.pop(1))
    tmp = items.copy()
    try_demo("remove(999)", lambda: tmp.remove(999))
    demo("after failed remove", tmp)

    tmp = [3, 1, 4, 1, 5]
    demo("sorted(tmp)", sorted(tmp))
    demo("sort() return", tmp.sort())
    demo("after sort()", tmp)

    names = ["bob", "Alice", "charlie"]
    tmp = names.copy()
    tmp.sort(key=str.lower)
    demo("sort(key=str.lower)", tmp)
    tmp = names.copy()
    tmp.sort(key=len, reverse=True)
    demo("sort(key=len, reverse=True)", tmp)

    tmp = [1, 2]
    tmp.extend((3, 4))
    tmp.extend(range(2))
    demo("extend(tuple/range)", tmp)

    tmp = [1, 2, 3]
    tmp.insert(100, 9)
    tmp.insert(-100, 0)
    demo("insert out of range", tmp)

    nested = [[1], [2]]
    copied = nested.copy()
    copied[0].append(99)
    demo("shallow copy", nested)

    show("2) tuple：index 的 start/stop")
    t = ("a", "b", "a", "c")
    demo("count('a')", t.count("a"))
    demo("index('a')", t.index("a"))
    demo("index('a', 1)", t.index("a", 1))
    demo("index('a', 1, 3)", t.index("a", 1, 3))
    try_demo("index('x')", lambda: t.index("x"))

    show("3) dict：参数与坑")
    data = {"a": 1, "b": 2}
    demo("get('missing')", data.get("missing"))
    demo("get('missing', 0)", data.get("missing", 0))

    tmp = data.copy()
    demo("pop('a')", tmp.pop("a"))
    demo("pop('missing', 0)", tmp.pop("missing", 0))
    try_demo("pop('missing')", lambda: tmp.pop("missing"))

    tmp = {"a": 1}
    tmp.update({"b": 2})
    tmp.update([("c", 3), ("d", 4)])
    tmp.update(e=5)
    demo("update(mapping/iter/kwargs)", tmp)

    groups = dict.fromkeys(["x", "y"], [])
    groups["x"].append(1)
    demo("fromkeys with list", groups)
    safe_groups = {k: [] for k in ["x", "y"]}
    safe_groups["x"].append(1)
    demo("comprehension instead", safe_groups)

    tmp = {"k1": 1, "k2": 2}
    view = tmp.keys()
    tmp["k3"] = 3
    demo("keys view after update", list(view))

    tmp = {"a": 1, "b": 2, "c": 3}
    demo("popitem()", tmp.popitem())
    demo("after popitem", tmp)

    show("4) set：多参数 + remove/discard")
    a = {1, 2, 3}
    b = {3, 4}
    c = {3, 5}
    demo("union(b, c)", a.union(b, c))
    demo("intersection(b, c)", a.intersection(b, c))
    demo("difference(b, c)", a.difference(b, c))

    tmp = {1}
    tmp.update([2], {3, 4})
    demo("update(multiple)", tmp)

    tmp = {1, 2}
    tmp.discard(999)
    demo("discard missing", tmp)
    try_demo("remove missing", lambda: tmp.remove(999))

    single = {42}
    demo("pop() arbitrary", single.pop())

    demo("isdisjoint({7})", a.isdisjoint({7}))

    show("5) frozenset：返回新对象")
    fs = frozenset({1, 2})
    demo("union({2,3})", fs.union({2, 3}))
    demo("type of union", type(fs.union({2, 3})).__name__)
    demo("intersection({2,3})", fs.intersection({2, 3}))


if __name__ == "__main__":
    main()