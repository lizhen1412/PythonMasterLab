#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：增强赋值（+= 等）与可变性（mutability）。

关键结论（很重要）：
1) 对可变对象（list/dict 等），`+=` 可能是“原地修改”（in-place），对象 id 不变
2) 对不可变对象（int/str/tuple 等），`+=` 一般会创建新对象，id 改变
3) 当存在别名（多个变量指向同一对象）时，是否原地修改会直接影响其它变量

运行：
    python3 01_Basics/02_Variables/07_augmented_assignment_and_mutability.py
"""


def main() -> None:
    print("1) list += ... 通常原地修改")
    lst = [1, 2]
    lst_id_before = id(lst)
    lst += [3]
    print("lst =", lst)
    print("id unchanged =", id(lst) == lst_id_before)

    print("\n2) tuple += ... 会创建新元组")
    t = (1, 2)
    t_id_before = id(t)
    t += (3,)
    print("t =", t)
    print("id changed =", id(t) != t_id_before)

    print("\n3) 存在别名时：a = a + ... 与 a += ... 结果不同")
    a = [1, 2]
    b = a
    a = a + [3]  # 创建了新列表；b 仍指向旧列表
    print("a =", a)
    print("b =", b)
    print("a is b =", a is b)

    a2 = [1, 2]
    b2 = a2
    a2 += [3]  # 原地修改；b2 也能看到变化
    print("\na2 =", a2)
    print("b2 =", b2)
    print("a2 is b2 =", a2 is b2)


if __name__ == "__main__":
    main()

