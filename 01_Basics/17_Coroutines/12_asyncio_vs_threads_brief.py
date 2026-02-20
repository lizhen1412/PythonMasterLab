#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：协程 vs 线程选择指南（简述）。
Author: Lambert
"""

from __future__ import annotations


def main() -> None:
    print("== 何时选 asyncio ==")
    print("- 大量并发 I/O，库提供 async 接口（httpx/asyncpg 等）")
    print("- 想减少线程切换/锁管理，接受协程风格")
    print("- 需要结构化并发（TaskGroup 等）")

    print("\n== 何时选线程 ==")
    print("- 需要并发执行阻塞 I/O 库/驱动（无 async 版本）")
    print("- 现有同步代码，改造成本高，可用线程池")

    print("\n== 何时不用协程 ==")
    print("- CPU 密集求加速（应选多进程/C 扩展）")
    print("- 需要调用阻塞接口且无法转 to_thread/线程池")


if __name__ == "__main__":
    main()