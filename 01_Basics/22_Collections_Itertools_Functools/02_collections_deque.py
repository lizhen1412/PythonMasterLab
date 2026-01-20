#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：collections.deque。

你会学到：
1) deque 是双端队列，头尾插入/弹出都是 O(1)
2) maxlen 可实现滑动窗口
3) rotate 让队列旋转

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/02_collections_deque.py
"""

from collections import deque


def main() -> None:
    dq = deque([1, 2, 3])
    dq.append(4)
    dq.appendleft(0)
    print("deque ->", dq)
    print("popleft ->", dq.popleft())
    print("pop ->", dq.pop())
    print("after pop ->", dq)

    dq.rotate(1)
    print("rotate(1) ->", dq)

    print("\n滑动窗口 (maxlen=3):")
    window = deque(maxlen=3)
    for n in range(5):
        window.append(n)
        print(list(window))


if __name__ == "__main__":
    main()
