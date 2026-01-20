#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：失败重试（retry until success）

题目：
实现函数 `retry(fn, max_attempts)`：
- 最多尝试 max_attempts 次调用 fn()
- 只要一次成功就返回结果
- 如果每次都失败：在最后一次失败时用 `raise` 重新抛出（保留 traceback）

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/10_retry_until_success.py
"""

from __future__ import annotations


def retry(fn, max_attempts: int) -> object:
    if max_attempts <= 0:
        raise ValueError("max_attempts must be >= 1")
    for attempt in range(1, max_attempts + 1):
        try:
            return fn()
        except Exception:
            if attempt == max_attempts:
                raise
    raise RuntimeError("unreachable")


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def check_raises(label: str, fn, exc_type: type[BaseException]) -> None:
    try:
        fn()
    except exc_type:
        print(f"[OK] {label}: raised {exc_type.__name__}")
    except Exception as exc:
        print(f"[FAIL] {label}: raised {type(exc).__name__}, expected {exc_type.__name__}")
    else:
        print(f"[FAIL] {label}: no exception, expected {exc_type.__name__}")


def make_flaky(success_after: int) -> callable:
    state = {"count": 0}

    def fn() -> int:
        state["count"] += 1
        if state["count"] < success_after:
            raise ValueError(f"fail #{state['count']}")
        return 42

    return fn


def main() -> None:
    check("retry success", retry(make_flaky(3), 3), 42)
    check_raises("retry fails", lambda: retry(make_flaky(3), 2), ValueError)
    check_raises("max_attempts=0", lambda: retry(lambda: 1, 0), ValueError)


if __name__ == "__main__":
    main()

