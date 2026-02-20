#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：把 dict 打印成 k=v / JSON / querystring（稳定顺序）
Author: Lambert

题目：
实现以下三个函数：
1) `dict_to_kv_line(d)`：把 dict 输出成一行 `k=v`（按 key 排序）
2) `dict_to_json_line(d)`：输出一行 JSON（ensure_ascii=False, sort_keys=True）
3) `dict_to_querystring(d)`：输出 `a=1&b=2`（按 key 排序；value 用 str）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/03_Printing/03_print_dict_formats.py
"""

import json


def dict_to_kv_line(d: dict[str, object]) -> str:
    parts = [f"{k}={d[k]!s}" for k in sorted(d)]
    return " ".join(parts)


def dict_to_json_line(d: dict[str, object]) -> str:
    return json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def dict_to_querystring(d: dict[str, object]) -> str:
    parts = [f"{k}={d[k]!s}" for k in sorted(d)]
    return "&".join(parts)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    payload: dict[str, object] = {"b": 1, "a": 2, "text": "你好"}
    check("kv", dict_to_kv_line(payload), "a=2 b=1 text=你好")
    check("query", dict_to_querystring(payload), "a=2&b=1&text=你好")
    check("json", dict_to_json_line(payload), "{\"a\":2,\"b\":1,\"text\":\"你好\"}")


if __name__ == "__main__":
    main()
