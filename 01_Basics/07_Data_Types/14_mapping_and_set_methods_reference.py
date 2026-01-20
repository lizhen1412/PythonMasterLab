#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：映射与集合方法全覆盖（dict / set / frozenset）。

你会学到：
1) dict 的全部常用方法
2) set 的全部常用方法（含集合运算）
3) frozenset 的常用方法

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/14_mapping_and_set_methods_reference.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo(label: str, value: object) -> None:
    print(f"{label:<32} -> {value!r}")


def main() -> None:
    show("1) dict 方法")
    data = {"a": 1, "b": 2}
    demo("keys()", list(data.keys()))
    demo("values()", list(data.values()))
    demo("items()", list(data.items()))
    demo("get('a')", data.get("a"))
    demo("get('missing', 0)", data.get("missing", 0))
    demo("fromkeys(['x','y'], 0)", dict.fromkeys(["x", "y"], 0))
    demo("copy()", data.copy())

    tmp = data.copy()
    demo("setdefault('c', 3)", tmp.setdefault("c", 3))
    tmp.update({"d": 4})
    demo("after update", tmp)
    demo("pop('a')", tmp.pop("a"))
    demo("popitem()", tmp.popitem())
    tmp.clear()
    demo("clear()", tmp)

    show("2) set 方法")
    a = {1, 2, 3}
    b = {3, 4}
    demo("union(b)", a.union(b))
    demo("intersection(b)", a.intersection(b))
    demo("difference(b)", a.difference(b))
    demo("symmetric_difference(b)", a.symmetric_difference(b))
    demo("isdisjoint({5})", a.isdisjoint({5}))
    demo("issubset({1,2,3,4})", a.issubset({1, 2, 3, 4}))
    demo("issuperset({1,2})", a.issuperset({1, 2}))
    demo("copy()", a.copy())

    tmp = a.copy()
    tmp.add(9)
    demo("add(9)", tmp)
    tmp = a.copy()
    tmp.update([5, 6])
    demo("update([5,6])", tmp)
    tmp = a.copy()
    tmp.remove(2)
    demo("remove(2)", tmp)
    tmp = a.copy()
    tmp.discard(999)
    demo("discard(999)", tmp)
    tmp = a.copy()
    popped = tmp.pop()
    demo("pop()", popped)
    demo("after pop", tmp)
    tmp = a.copy()
    tmp.difference_update(b)
    demo("difference_update(b)", tmp)
    tmp = a.copy()
    tmp.intersection_update(b)
    demo("intersection_update(b)", tmp)
    tmp = a.copy()
    tmp.symmetric_difference_update(b)
    demo("symmetric_difference_update(b)", tmp)
    tmp = a.copy()
    tmp.clear()
    demo("clear()", tmp)

    show("3) frozenset 方法")
    fs = frozenset({1, 2, 3})
    demo("union({3,4})", fs.union({3, 4}))
    demo("intersection({3,4})", fs.intersection({3, 4}))
    demo("difference({3,4})", fs.difference({3, 4}))
    demo("symmetric_difference({3,4})", fs.symmetric_difference({3, 4}))
    demo("isdisjoint({5})", fs.isdisjoint({5}))
    demo("issubset({1,2,3,4})", fs.issubset({1, 2, 3, 4}))
    demo("issuperset({1,2})", fs.issuperset({1, 2}))
    demo("copy()", fs.copy())


if __name__ == "__main__":
    main()
