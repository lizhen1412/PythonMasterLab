#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：变量修改（重新绑定 vs 原地修改）。
Author: Lambert

你会学到：
1) 不可变对象（int/str/tuple）：看起来“修改”其实常常是重新绑定新对象
2) 可变对象（list/dict/set）：很多操作会原地修改（id 不变）
3) 别名（alias）：多个名字指向同一个可变对象时，修改会“连带影响”
4) `+=` 可能是原地修改，也可能创建新对象（取决于类型）

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/03_variable_modification.py
"""

from __future__ import annotations


def show(label: str, value: object) -> None:
    print(f"{label:<18} value={value!r:<25} id=0x{id(value):x}")


def main() -> None:
    print("1) 不可变对象：int 的 “+=” 通常会生成新对象")
    x = 10
    show("x before", x)
    x += 1
    show("x after", x)

    print("\n2) 可变对象：list 的 append 是原地修改")
    items = [1, 2, 3]
    show("items before", items)
    items.append(4)
    show("items after", items)

    print("\n3) 别名（alias）：两个名字指向同一个 list")
    a = ["A"]
    b = a
    show("a before", a)
    show("b before", b)
    b.append("B")
    print("b.append('B') 后：")
    show("a after", a)
    show("b after", b)
    print("a is b ->", a is b)

    print("\n4) `+=` vs `a = a + ...`（对可变对象可能不一样）")
    left = [1, 2]
    alias = left
    show("left before", left)
    show("alias before", alias)
    left += [3]  # 通常是原地修改（list.__iadd__）
    print("left += [3] 后：")
    show("left after", left)
    show("alias after", alias)

    print("\n再对比 `left = left + [4]`：")
    show("left before", left)
    left = left + [4]  # 创建新 list
    show("left after", left)
    show("alias still", alias)


if __name__ == "__main__":
    main()
