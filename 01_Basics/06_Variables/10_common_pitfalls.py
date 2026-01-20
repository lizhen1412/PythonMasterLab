#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：变量相关常见坑（尽量不让脚本崩：用 try/except 或安全写法演示）。

你会学到：
1) `is` vs `==`：is 比较“是否同一对象”，== 比较“值是否相等”
2) 链式赋值的别名陷阱：`a = b = []`
3) 可变默认参数：函数会“记住上一次结果”
4) 闭包晚绑定：循环里 lambda 捕获同一个变量
5) 避免遮蔽内置名：list/dict/type/id 等

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/10_common_pitfalls.py
"""

from __future__ import annotations

from collections.abc import Callable


def pitfall_is_vs_eq() -> None:
    print("1) is vs ==：")
    a = [1, 2]
    b = [1, 2]
    print("a == b ->", a == b)
    print("a is b ->", a is b)
    print("正确用法：比较值用 ==；判断 None 用 `is None`。")


def pitfall_chained_assignment() -> None:
    print("\n2) 链式赋值陷阱：a = b = []")
    a = b = []
    a.append(1)
    print("a =", a)
    print("b =", b)
    print("a is b ->", a is b)
    print("正确写法：a, b = [], []")


def append_bad(item: int, items: list[int] = []) -> list[int]:  # noqa: B006
    items.append(item)
    return items


def append_good(item: int, items: list[int] | None = None) -> list[int]:
    if items is None:
        items = []
    items.append(item)
    return items


def pitfall_mutable_default() -> None:
    print("\n3) 可变默认参数：")
    print("append_bad(1) ->", append_bad(1))
    print("append_bad(2) ->", append_bad(2))
    print("正确写法：默认值用 None，再在函数内创建新 list")
    print("append_good(1) ->", append_good(1))
    print("append_good(2) ->", append_good(2))


def pitfall_late_binding() -> None:
    print("\n4) 闭包晚绑定（late binding）：")
    funcs: list[Callable[[], int]] = []
    for i in range(3):
        funcs.append(lambda: i)  # i 会在调用时才查找，最终都是 2
    print("bad:", [f() for f in funcs])

    funcs2: list[Callable[[], int]] = []
    for j in range(3):
        funcs2.append(lambda j=j: j)  # 用默认参数“冻结”当前值
    print("good:", [f() for f in funcs2])


def pitfall_shadow_builtins() -> None:
    print("\n5) 遮蔽内置名：")
    print("不推荐：type = 123 / list = ...（会把内置 type/list 覆盖掉）")
    print("推荐：用更具体的名字，如 item_type / items / mapping 等")


def main() -> None:
    pitfall_is_vs_eq()
    pitfall_chained_assignment()
    pitfall_mutable_default()
    pitfall_late_binding()
    pitfall_shadow_builtins()


if __name__ == "__main__":
    main()

