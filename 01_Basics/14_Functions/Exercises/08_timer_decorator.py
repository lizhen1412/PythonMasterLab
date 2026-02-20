#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：计时装饰器。
Author: Lambert

要求：
- 编写一个装饰器，记录函数运行耗时
- 装饰器需要透传 *args/**kwargs，并返回原结果
"""

from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def timer(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):  # type: ignore[override]
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        print(f"[TIMER] {func.__name__} took {duration:.2f} ms")
        return result

    return wrapper  # type: ignore[return-value]


@timer
def slow_sum(numbers: list[int]) -> int:
    time.sleep(0.05)
    return sum(numbers)


def main() -> None:
    total = slow_sum([1, 2, 3, 4, 5])
    print("slow_sum result ->", total)


if __name__ == "__main__":
    main()