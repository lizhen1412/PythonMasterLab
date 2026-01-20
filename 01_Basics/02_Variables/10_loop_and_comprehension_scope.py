#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：循环与推导式的变量作用域差异。

你会学到：
1) `for` 循环的循环变量，在循环结束后仍然存在（在同一作用域内）
2) 列表/集合/字典推导式的循环变量，在 Python 3 中不会“泄漏”到外层作用域

运行：
    python3 01_Basics/02_Variables/10_loop_and_comprehension_scope.py
"""


def main() -> None:
    for i in range(3):
        pass
    print("for 循环结束后，i 仍然可用：i =", i)

    before = set(locals().keys())
    squares = [j * j for j in range(3)]
    after = set(locals().keys())

    print("squares =", squares)
    print("推导式结束后，j 是否出现在 locals() 里？", "j" in locals())
    print("locals() 变化（新增的名字）=", sorted(after - before))


if __name__ == "__main__":
    main()
