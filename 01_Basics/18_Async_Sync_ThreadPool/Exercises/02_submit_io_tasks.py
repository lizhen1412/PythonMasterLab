#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：线程池并发假 I/O，收集结果。
"""

from __future__ import annotations

import concurrent.futures as cf
import time


def fake_io(x: int) -> str:
    time.sleep(0.1)
    return f"io-{x}"


def main() -> None:
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(fake_io, i) for i in range(5)]
        results = [fut.result() for fut in futures]
    print("results ->", results)


if __name__ == "__main__":
    main()
