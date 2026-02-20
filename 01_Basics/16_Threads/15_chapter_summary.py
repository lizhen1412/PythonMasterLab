#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：本章总结与常见坑。
Author: Lambert
"""

from __future__ import annotations


RULES = [
    "线程适合 I/O 密集；CPU 密集不要期待提速（GIL），可用 multiprocessing",
    "共享可变状态必须用同步原语或队列；尽量减少共享",
    "锁获取后记得释放，优先使用 with/try-finally；避免死锁，锁顺序一致、可设超时",
    "daemon 线程不会做清理，退出时会被强制终止；重要资源请在非 daemon 线程释放",
    "用 Event/Flag 控制线程退出，不要强杀线程",
    "线程池 Future 的异常会在 result()/迭代时抛出，记得捕获",
    "日志里打印线程名便于调试；可自定义 threading.excepthook 观察未捕获异常",
    "Timer 不精确；周期任务可用 while+sleep+Event，复杂调度用专用工具",
    "Queue 是线程安全的生产者-消费者首选；哨兵值配合 task_done/join 优雅退出",
]


PITFALLS = [
    "竞态：未加锁修改共享变量导致结果不一致",
    "死锁：多个锁交叉获取；解决：一致顺序/超时/RLock 或重新设计",
    "线程泄漏：缺少退出条件/未 join；daemon 线程被强行终止导致资源未释放",
    "误以为线程异常会终止主线程；必须检查 Future 或使用 excepthook/日志",
    "用线程提升 CPU 密集性能；效果微弱且增加上下文切换开销",
    "Timer/睡眠依赖精度：受调度影响，不适合实时性需求",
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