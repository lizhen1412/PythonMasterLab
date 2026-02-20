#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: ContextVar basics.
Author: Lambert

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/06_contextvars_basics.py
"""

from contextvars import ContextVar, copy_context

request_id: ContextVar[str] = ContextVar("request_id", default="none")


def worker(label: str) -> None:
    print(label, "->", request_id.get())


def main() -> None:
    worker("default")

    token = request_id.set("req-1")
    worker("set")
    request_id.reset(token)
    worker("reset")

    ctx = copy_context()
    ctx.run(request_id.set, "req-2")
    ctx.run(worker, "copy_context")


if __name__ == "__main__":
    main()