#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：变量相关的常见坑（Pitfalls）。

这类“坑”通常不会让代码立刻报错，但会产生非常隐蔽的 bug。

本文件包含两类高频问题：
1) **可变默认参数**：默认参数只在函数定义时求值一次（不是每次调用都新建）
2) **闭包晚绑定**：循环里创建 lambda/内层函数时，捕获的变量会在调用时才取值

为了让示例更“专业”和更友好（不触发静态检查器对反例的告警），我们把反例放进字符串里执行；
你重点关注输出对比即可。

运行：
    python3 01_Basics/02_Variables/15_common_pitfalls.py
"""


def demonstrate_mutable_default_arg() -> None:
    bad = """
def append_item(x, items=[]):
    items.append(x)
    return items

print("bad:", append_item(1))
print("bad:", append_item(2))
"""

    good = """
def append_item(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

print("good:", append_item(1))
print("good:", append_item(2))
"""

    print("1) 可变默认参数：")
    exec(bad, {})
    exec(good, {})


def demonstrate_late_binding_in_closure() -> None:
    bad = """
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print("bad:", [f() for f in funcs])  # 期望 [0,1,2]，实际 [2,2,2]
"""

    good = """
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)  # 把当前 i 作为默认参数“固定住”

print("good:", [f() for f in funcs])  # [0,1,2]
"""

    print("\n2) 闭包晚绑定（for 循环 + lambda）：")
    exec(bad, {})
    exec(good, {})


def main() -> None:
    demonstrate_mutable_default_arg()
    demonstrate_late_binding_in_closure()


if __name__ == "__main__":
    main()

