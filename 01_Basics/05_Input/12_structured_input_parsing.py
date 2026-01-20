#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：结构化输入（把一行字符串解析成 list/dict 等结构）。

你会学到：
1) JSON：`json.loads(text)`（最常见：接口、配置、日志）
2) Python 字面量：`ast.literal_eval(text)`（只解析安全的字面量：list/dict/str/int/...）
3) 解析失败要捕获异常（不要让程序崩）
4) 不要对用户输入用 `eval()`（安全风险很大）

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/12_structured_input_parsing.py
"""

from __future__ import annotations

import ast
import json


def main() -> None:
    print("1) JSON 输入（直接回车使用默认示例）：")
    try:
        raw_json = input("JSON> ").strip()
    except (EOFError, KeyboardInterrupt):
        raw_json = ""

    if not raw_json:
        raw_json = '{"name":"Alice","age":20,"scores":[98,100],"active":true}'
        print("使用默认 JSON：", raw_json)

    try:
        data = json.loads(raw_json)
        print("json.loads result type =", type(data).__name__)
        print("value =", data)
    except json.JSONDecodeError as exc:
        print("JSONDecodeError:", exc)

    print("\n2) Python 字面量输入（直接回车使用默认示例）：")
    try:
        raw_lit = input("LIT> ").strip()
    except (EOFError, KeyboardInterrupt):
        raw_lit = ""

    if not raw_lit:
        raw_lit = "{'name': 'Bob', 'age': 7, 'scores': [1, 2, 3], 'active': True}"
        print("使用默认字面量：", raw_lit)

    try:
        obj = ast.literal_eval(raw_lit)
        print("literal_eval result type =", type(obj).__name__)
        print("value =", obj)
    except (ValueError, SyntaxError) as exc:
        print("literal_eval failed:", exc)

    print("\n小结：")
    print("- JSON 更通用（跨语言），但 true/false/null 必须小写。")
    print("- Python 字面量更像 Python 写法（True/False/None），但不适合跨语言。")


if __name__ == "__main__":
    main()

