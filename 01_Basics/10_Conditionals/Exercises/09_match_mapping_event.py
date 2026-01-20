#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：match（映射模式：event dict）

题目：
实现 `describe_event(event)`，支持以下输入：
1) {"type": "user_created", "id": <int>, "name": <str>, ...}
2) {"type": "error", "code": <int>, "message": <str>, ...}
3) 其他 dict -> 返回 "unknown event"
4) 非 dict -> 返回 "not a mapping"

要求：
- 使用 match/case 的映射模式：
  - `case {"type": "user_created", "id": int() as user_id, "name": str() as name, **rest}:`
  - `case {"type": "error", "code": int() as code, "message": str() as msg, **rest}:`
- `rest` 仅用于演示，可不参与输出

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/10_Conditionals/Exercises/09_match_mapping_event.py
"""

from __future__ import annotations


def describe_event(event: object) -> str:
    match event:
        case {"type": "user_created", "id": int() as user_id, "name": str() as name, **_rest}:
            return f"user_created(id={user_id}, name={name})"
        case {"type": "error", "code": int() as code, "message": str() as msg, **_rest}:
            return f"error(code={code}, message={msg})"
        case dict():
            return "unknown event"
        case _:
            return "not a mapping"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check(
        "user_created",
        describe_event({"type": "user_created", "id": 7, "name": "Alice", "extra": True}),
        "user_created(id=7, name=Alice)",
    )
    check(
        "error",
        describe_event({"type": "error", "code": 500, "message": "boom"}),
        "error(code=500, message=boom)",
    )
    check("unknown_dict", describe_event({"type": "other"}), "unknown event")
    check("not_dict", describe_event(["x"]), "not a mapping")


if __name__ == "__main__":
    main()

