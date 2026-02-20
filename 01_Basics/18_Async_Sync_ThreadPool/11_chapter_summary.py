#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：本章总结与常见坑。
Author: Lambert
"""

from __future__ import annotations


RULES = [
    "线程池适合阻塞 I/O，不提升 CPU 密集性能；CPU 密集用多进程/扩展",
    "在协程里调用阻塞函数必须用 to_thread/run_in_executor，否则会卡住事件循环",
    "控制并发：限制线程池大小或用 Semaphore，避免任务爆炸",
    "超时/取消后要清理资源；CancelledError/TimeoutError 是正常控制流",
    "shutdown(cancel_futures=True) 可取消未开始任务；已运行的需要自行检查停机信号",
    "不要在线程池任务里调用 asyncio.run；如需在新线程用 asyncio，应显式创建/管理事件循环",
    "日志里打印线程名/任务信息，便于排查混合场景问题",
]


PITFALLS = [
    "把 CPU 密集任务塞进线程池期望提速：GIL 限制且增加上下文切换",
    "协程里直接调用阻塞 I/O/CPU 导致事件循环卡死",
    "无限制创建任务或提交到线程池，导致内存/队列爆炸",
    "忽视任务异常：未监控的线程池/协程任务抛错被静默忽略",
    "取消/超时后不做清理，遗留锁/文件句柄等资源",
    "混用阻塞队列/锁与 asyncio 原语，导致死锁或阻塞",
]


def main() -> None:
    print("== 规则清单 ==")
    for idx, rule in enumerate(RULES, start=1):
        print(f"{idx:02d}. {rule}")

    print("\n== 常见坑 ==")
    for idx, pitfall in enumerate(PITFALLS, start=1):
        print(f"{idx:02d}. {pitfall}")


if __name__ == "__main__":
    main()