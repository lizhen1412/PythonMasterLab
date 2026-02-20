#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：用 logging.exception 记录错误并返回默认值
Author: Lambert

题目：
实现函数 `run_with_logging(fn, default=None)`：
- 成功：返回 fn() 的结果
- 失败（捕获 Exception）：用 logger.exception(...) 记录带 traceback 的日志，然后返回 default

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/08_logging_exception_helper.py
"""

from __future__ import annotations

import logging


logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("exercise-logging")


def run_with_logging(fn, default: object | None = None) -> object | None:
    try:
        return fn()
    except Exception:
        logger.exception("task failed")
        return default


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("run_with_logging(ok)", run_with_logging(lambda: 123), 123)
    check("run_with_logging(fail, default=0)", run_with_logging(lambda: 1 / 0, 0), 0)


if __name__ == "__main__":
    main()
