#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：类型系统与“数据类型分类”快速总览。

你会学到：
1) `type(x)`：对象的实际类型；`x.__class__` 通常等价
2) `isinstance(x, T)`：推荐的类型判断方式（支持继承）
3) 真值测试（truthiness）：空容器/0/None/False 等在 if 中为 False
4) 可变 vs 不可变：list/dict/set/bytearray 通常可变；str/tuple/frozenset/bytes 通常不可变
5) 可哈希（hashable）：能否作为 dict key / set 元素（通常：不可变且内容不可变 -> 可哈希）

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/02_type_system_and_categories.py
"""

from __future__ import annotations


def try_hash(value: object) -> str:
    try:
        return hex(hash(value))
    except TypeError as exc:
        return f"TypeError({exc})"


def show_row(name: str, value: object) -> None:
    print(
        f"{name:<12}"
        f"type={type(value).__name__:<12} "
        f"bool={bool(value)!s:<5} "
        f"hash={try_hash(value)} "
        f"repr={value!r}"
    )


def main() -> None:
    print("1) type / isinstance：")
    x: object = 123
    print("type(x) =", type(x))
    print("isinstance(x, int) =", isinstance(x, int))
    print("isinstance(x, (int, str)) =", isinstance(x, (int, str)))
    print("bool 是 int 子类 ->", issubclass(bool, int))

    print("\n2) 真值测试 + 可哈希性（用 hash() 能否成功来判断）：")
    samples: list[tuple[str, object]] = [
        ("None", None),
        ("False", False),
        ("True", True),
        ("0", 0),
        ("1", 1),
        ("0.0", 0.0),
        ("'': str", ""),
        ("'hi': str", "hi"),
        ("[]", []),
        ("[1]", [1]),
        ("()", ()),
        ("(1,)", (1,)),
        ("{}", {}),
        ("{'a':1}", {"a": 1}),
        ("set()", set()),
        ("{1,2}", {1, 2}),
        ("frozenset()", frozenset()),
        ("b''", b""),
        ("b'hi'", b"hi"),
        ("bytearray()", bytearray()),
    ]
    for name, value in samples:
        show_row(name, value)

    print("\n3) 可变 vs 不可变（用别名现象理解）：")
    items = [1, 2]
    alias = items
    print("before:", items, alias, "items is alias ->", items is alias)
    items.append(3)
    print("after append:", items, alias, "（可变对象原地修改会影响别名）")

    text = "hi"
    text_alias = text
    print("\nstr before:", text, text_alias, "text is alias ->", text is text_alias)
    text += "!"
    print("str after text += '!':", text, text_alias, "（不可变对象通常是重新绑定新对象）")

    print("\n4) 一个重要规则：dict 的 key / set 的元素必须可哈希")
    ok_key = ("user", 1)
    mapping = {ok_key: "OK"}
    print("dict with tuple key ->", mapping)
    try:
        bad_key = ["user", 1]
        m2: dict[object, str] = {}
        m2[bad_key] = "NO"
    except TypeError as exc:
        print("list 不能当 dict key：", exc)


if __name__ == "__main__":
    main()
