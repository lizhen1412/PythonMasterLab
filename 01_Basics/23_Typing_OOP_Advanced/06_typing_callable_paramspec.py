#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: Callable and ParamSpec.
Author: Lambert

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/06_typing_callable_paramspec.py
"""

from __future__ import annotations

from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log_call(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"calling {func.__name__} args={args} kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def add(a: int, b: int) -> int:
    return a + b


@log_call
def greet(name: str, *, upper: bool = False) -> str:
    text = f"hello {name}"
    return text.upper() if upper else text


def main() -> None:
    print("add ->", add(2, 3))
    print("greet ->", greet("bob"))
    print("greet upper ->", greet("bob", upper=True))


if __name__ == "__main__":
    main()