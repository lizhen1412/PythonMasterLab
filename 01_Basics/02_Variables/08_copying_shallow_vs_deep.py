#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：复制（copy）：浅拷贝 vs 深拷贝。

你会学到：
1) 直接赋值不会复制：b = a 只是“又多了一个名字”
2) 浅拷贝（shallow copy）：只复制最外层容器；内部对象仍共享
3) 深拷贝（deep copy）：递归复制内部对象；更独立，但可能更慢

运行：
    python3 01_Basics/02_Variables/08_copying_shallow_vs_deep.py
"""

import copy


def main() -> None:
    nested = [[1, 2], [3, 4]]
    alias = nested
    shallow = nested.copy()
    deep = copy.deepcopy(nested)

    print("nested  =", nested)
    print("alias   =", alias)
    print("shallow =", shallow)
    print("deep    =", deep)
    print("alias is nested   =", alias is nested)
    print("shallow is nested =", shallow is nested)

    print("\n修改 nested[0].append(99) 后：")
    nested[0].append(99)
    print("nested  =", nested)
    print("alias   =", alias, "  # 共享，受影响")
    print("shallow =", shallow, "# 浅拷贝仍共享内部列表，也受影响")
    print("deep    =", deep, "   # 深拷贝不共享内部列表，不受影响")


if __name__ == "__main__":
    main()

