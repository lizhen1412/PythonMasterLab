#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: ContextVar set/reset.
Author: Lambert

Task:
Implement toggle_context(value) -> tuple[str, str].

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/Exercises/05_contextvar_token.py
"""

from contextvars import ContextVar

current: ContextVar[str] = ContextVar("current", default="default")


def toggle_context(value: str) -> tuple[str, str]:
    before = current.get()
    token = current.set(value)
    after = current.get()
    current.reset(token)
    return before, after


def main() -> None:
    print("toggle ->", toggle_context("x"))


if __name__ == "__main__":
    main()