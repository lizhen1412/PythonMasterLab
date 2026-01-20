#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：本章总结（类与对象）。

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/10_chapter_summary.py
"""

from __future__ import annotations


SUMMARY = [
    "class 定义类型，实例保存状态；__init__ 负责初始化属性",
    "类属性共享，实例属性会遮蔽同名类属性",
    "@classmethod 操作类本身；@staticmethod 只是放在类里的函数",
    "@property 用来封装校验与派生属性（读写像属性）",
    "继承可复用逻辑；重写方法 + super() 是常见模式",
    "dataclass 自动生成 __init__/__repr__/__eq__，默认值用 default_factory",
    "__repr__/__str__/__format__ 控制展示；__eq__/__lt__/__hash__ 影响比较与集合行为",
    "__len__/__bool__/__getitem__/__iter__/__next__/__contains__ 让对象表现得像容器/迭代器",
    "__enter__/__exit__ 支持 with；__call__ 让对象可调用",
    "__getattr__/__setattr__/__delattr__/__slots__ 控制属性访问与约束",
    "__new__/__del__/__getattribute__ 影响对象创建与属性访问",
    "__delitem__/__reversed__ 是容器协议的补充能力",
    "算术与转换协议：__add__/__sub__/__mul__/__truediv__/__floordiv__/__mod__/__pow__",
    "类型转换：__int__/__float__/__complex__/__index__/__bytes__/__fspath__",
    "异步上下文：__aenter__/__aexit__ 支持 async with",
    "拷贝与序列化：__copy__/__deepcopy__/__getstate__/__setstate__/__reduce__",
    "描述符与模式匹配：__get__/__set__/__delete__/__match_args__",
]


def main() -> None:
    print("类与对象：关键规则清单")
    for item in SUMMARY:
        print("-", item)


if __name__ == "__main__":
    main()
