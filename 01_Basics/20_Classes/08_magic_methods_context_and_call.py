#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：上下文管理与可调用对象。

你会学到：
1) __enter__ / __exit__：with 语句协议
2) __call__：实例像函数一样被调用

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/08_magic_methods_context_and_call.py
"""

from __future__ import annotations

import time


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Timer:
    def __init__(self) -> None:
        self.start: float | None = None
        self.elapsed: float | None = None

    def __enter__(self) -> "Timer":
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        end = time.perf_counter()
        self.elapsed = end - (self.start or end)
        print(f"elapsed: {self.elapsed:.6f}s")
        return False


class Prefixer:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix

    def __call__(self, text: str) -> str:
        return f"{self.prefix}{text}"


def main() -> None:
    show("1) with + __enter__/__exit__")
    with Timer() as t:
        total = sum(range(10_000))
        print("sum ->", total)
    print("t.elapsed ->", t.elapsed)

    show("2) __call__ 让对象可调用")
    info = Prefixer("[INFO] ")
    print("callable(info) ->", callable(info))
    print("info('start') ->", info("start"))


if __name__ == "__main__":
    main()
