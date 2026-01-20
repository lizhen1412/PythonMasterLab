#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：本章总结与常见坑。
"""

from __future__ import annotations


RULES = [
    "async/await 适合并发 I/O；CPU 密集不提速，需 to_thread/多进程/扩展",
    "创建任务后要监控/await；未处理异常可能被忽略或只在日志出现",
    "取消是正常控制流：捕获 CancelledError 后应清理并重新抛出（或明确吞掉）",
    "超时可用 wait_for 或 asyncio.timeout；注意内层任务可能被取消",
    "阻塞调用请用 asyncio.to_thread 或线程/进程池，不要阻塞事件循环",
    "使用 asyncio.Queue/Lock/Semaphore/Event 的 async 版本，避免混用阻塞原语",
    "TaskGroup 提供结构化并发：任一任务失败会取消其他并抛出异常组",
    "fire-and-forget 风险高，至少添加 done 回调捕获异常",
]


PITFALLS = [
    "在已运行的事件循环里调用 asyncio.run：会报错；应直接 await 或用 loop.run_until_complete",
    "忘记 await 协程：只创建协程对象不执行；或 create_task 后丢失引用",
    "阻塞 I/O/CPU 直接写在协程里，卡住整个事件循环",
    "gather 默认遇到异常会立即抛出并取消其它任务；需要收集全部异常请用 return_exceptions",
    "取消后吞掉 CancelledError，导致上层以为任务完成，资源未清理",
    "混用线程锁/Queue 与 asyncio 任务，可能造成死锁或阻塞",
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
