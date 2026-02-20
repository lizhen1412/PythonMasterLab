#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：条件判断——本章总结
Author: Lambert

运行（在仓库根目录执行）：
    python3 01_Basics/10_Conditionals/09_chapter_summary.py
"""

from __future__ import annotations


SUMMARY: list[str] = [
    "if/elif/else：按顺序命中第一个分支；顺序与覆盖范围决定正确性",
    "单分支 if 常用于 guard：不满足条件就提前 return/continue，减少嵌套",
    "条件表达式 a if cond else b：用于“产生一个值”，复杂逻辑不要嵌套",
    "真值测试：if x 看的是 bool(x)；区分 None 与 0/''/False 这类合法值",
    "and/or：短路且返回对象（不一定是 bool）；x or default 不是 None 合并",
    "长条件用括号换行，避免反斜杠，提升可读性",
    "match/case：结构化匹配，按从上到下第一个命中执行；case NAME 是捕获，不是常量",
    "优先级：not/and/or 与比较容易误判；不确定就加括号",
]


def main() -> None:
    print("本章总结（Conditionals）：")
    for i, line in enumerate(SUMMARY, start=1):
        print(f"{i}. {line}")
    print("\n下一步：运行练习题索引 -> python3 01_Basics/10_Conditionals/Exercises/01_overview.py")


if __name__ == "__main__":
    main()