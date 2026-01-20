#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：线程 vs asyncio 选择指南（简述）。

本示例以打印对比为主，不包含 asyncio 代码细节。
"""

from __future__ import annotations


def main() -> None:
    print("== 何时选线程 ==")
    print("- 需要并发执行阻塞 I/O 库（文件、网络、数据库驱动非 async 版本）")
    print("- 现有同步代码，改造成本高，适合用线程池并发")
    print("- 要并行等待多个阻塞操作，但数量不算极端")

    print("\n== 何时选 asyncio ==")
    print("- 大量并发 I/O，库本身提供 async 接口（httpx/asyncpg 等）")
    print("- 需要跨平台高并发，愿意采用事件循环模型")
    print("- 想避免线程切换开销/锁，接受协程风格编程")

    print("\n== 何时不用线程 ==")
    print("- CPU 密集运算希望提速（应选 multiprocessing/原生扩展）")
    print("- 需要严格实时/精确定时（线程调度不可控）")
    print("- 容易出现共享状态竞态且难以管理")


if __name__ == "__main__":
    main()
