#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：装饰器与 `functools.partial`。
Author: Lambert

- 最小装饰器：包裹函数前后打印；`functools.wraps` 复制元数据
- 带参数装饰器：外层接收配置，返回真正装饰器
- `functools.partial`：预填参数，生成新函数
"""

from __future__ import annotations

import time
from functools import partial, wraps
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log_calls(func: F) -> F:
    """最小可用装饰器，打印调用次数与参数。"""
    calls = 0

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):  # type: ignore[override]
        nonlocal calls
        calls += 1
        print(f"[LOG] {func.__name__} call #{calls} args={args} kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]


def with_prefix(prefix: str) -> Callable[[F], F]:
    """带参数装饰器：外层接收 prefix，返回真正的装饰器。"""

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):  # type: ignore[override]
            print(f"{prefix} -> {func.__name__}")
            return func(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator


@log_calls
def slow_add(a: int, b: int) -> int:
    """模拟一个慢函数，便于观察装饰器输出。"""
    time.sleep(0.1)
    return a + b


@with_prefix("[GREETING]")
def greet(name: str) -> str:
    return f"Hello, {name}"


def demo_partial() -> None:
    """使用 partial 预填参数，生成新函数。"""
    power_of_two = partial(pow, 2)
    print("pow(2, 5) ->", power_of_two(5))

    multiply = partial(lambda x, y, z: x * y * z, 2, z=10)
    print("partial 预填（2, z=10） -> multiply(3) =", multiply(3))


def main() -> None:
    print("== 最小装饰器 ==")
    print("slow_add(1, 2) ->", slow_add(1, 2))
    print("slow_add(3, 4) ->", slow_add(3, 4))
    print("slow_add.__name__ ->", slow_add.__name__)

    print("\n== 带参数装饰器 ==")
    print(greet("Alice"))

    print("\n== functools.partial ==")
    demo_partial()


if __name__ == "__main__":
    main()