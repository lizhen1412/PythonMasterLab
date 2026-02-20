#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：结构化输出（更像“专业日志/调试输出”）。
Author: Lambert

你会学到：
1) `pprint.pformat`：把复杂结构格式化成多行可读文本
2) `json.dumps`：把数据格式化成 JSON（机器友好，常用于日志/接口）
3) `reprlib.repr`：把很长的对象缩短显示（避免刷屏）

运行：
    python3 01_Basics/04_Formatting/12_pprint_json_reprlib.py
"""

import json
import pprint
import reprlib


def main() -> None:
    data = {
        "user": {"name": "Alice", "age": 20},
        "scores": [98, 100, 87, 92],
        "tags": ["python", "formatting", "学习"],
        "active": True,
    }

    print("1) pprint（多行更可读）：")
    print(pprint.pformat(data, sort_dicts=True, width=60))

    print("\n2) JSON（机器友好；indent 让人也能读）：")
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))

    print("\n3) 一行 JSON（适合日志管道；更紧凑）：")
    one_line = json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    print(one_line)

    print("\n4) reprlib：缩短超长列表：")
    big_list = list(range(100))
    print(reprlib.repr(big_list))


if __name__ == "__main__":
    main()
