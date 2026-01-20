#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：字典（dict，映射类型）。

你会学到：
1) 创建：字面量 / dict() / fromkeys / 推导式
2) 访问：`d[key]` vs `d.get(key, default)`（KeyError vs 默认值）
3) 遍历：keys/values/items
4) 更新：赋值、update、合并（`|` / `|=`）
5) 常见小技巧：计数、setdefault

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/07_dict_mapping.py
"""

from __future__ import annotations


def main() -> None:
    print("1) 创建：")
    d1 = {"name": "Alice", "age": 20}
    d2 = dict(name="Bob", age=7)
    d3 = dict([("x", 1), ("y", 2)])
    d4 = dict.fromkeys(["a", "b", "c"], 0)
    d5 = {k: k * k for k in range(3)}
    print("d1 =", d1)
    print("d2 =", d2)
    print("d3 =", d3)
    print("d4 =", d4)
    print("d5 =", d5)

    print("\n2) 访问：[] vs get：")
    print("d1['name'] ->", d1["name"])
    print("d1.get('missing') ->", d1.get("missing"))
    print("d1.get('missing', 0) ->", d1.get("missing", 0))
    try:
        _ = d1["missing"]
    except KeyError as exc:
        print("d1['missing'] -> KeyError:", exc)

    print("\n3) 遍历：")
    for k in d1.keys():
        print("key ->", k)
    for v in d1.values():
        print("value ->", v)
    for k, v in d1.items():
        print(f"item -> {k}={v}")

    print("\n4) 更新与合并：")
    d = {"a": 1}
    d["b"] = 2
    print("assign ->", d)
    d.update({"b": 20, "c": 3})
    print("update ->", d)
    merged = d | {"c": 30, "d": 4}
    print("merged with | ->", merged)
    d |= {"e": 5}
    print("in-place |= ->", d)

    print("\n5) 计数：")
    text = "aabccc"
    counter: dict[str, int] = {}
    for ch in text:
        counter[ch] = counter.get(ch, 0) + 1
    print("counter =", counter)

    print("\n6) setdefault（不常用但要看得懂）：")
    groups: dict[str, list[int]] = {}
    for n in [1, 2, 3, 4, 5]:
        key = "odd" if n % 2 else "even"
        groups.setdefault(key, []).append(n)
    print("groups =", groups)


if __name__ == "__main__":
    main()

