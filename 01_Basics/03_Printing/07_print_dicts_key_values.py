#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：一行打印 dict（结构化输出）
Author: Lambert

你会学到：
1) 直接 print(dict)：快速但不一定最“工程化”
2) 打印为 `k=v`：常见日志格式，适合一行多个字段
3) 一行 JSON：便于机器解析（日志/接口）
4) 一行 querystring：适合 URL 参数风格

运行：
    python3 01_Basics/03_Printing/07_print_dicts_key_values.py
"""

import json
from urllib.parse import urlencode


def format_as_kv(data: dict[str, object]) -> str:
    parts = [f"{k}={v!r}" for k, v in sorted(data.items())]
    return " ".join(parts)


def main() -> None:
    config: dict[str, object] = {"host": "127.0.0.1", "port": 8080, "debug": True}

    print("1) 直接打印 dict：")
    print(config)

    print("\n2) k=v（一行日志风格）：")
    print(format_as_kv(config))

    print("\n3) 一行 JSON（更适合机器读取）：")
    one_line_json = json.dumps(config, ensure_ascii=False, separators=(",", ":"))
    print(one_line_json)

    print("\n4) 一行 querystring：")
    # 注意：urlencode 会做 URL 编码，空格/中文等会变成 %xx 或 +
    query = urlencode(config)
    print(query)


if __name__ == "__main__":
    main()
