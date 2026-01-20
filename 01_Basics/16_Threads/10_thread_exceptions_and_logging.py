#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：线程异常与日志（excepthook）。
"""

from __future__ import annotations

import logging
import threading
import time


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(threadName)s: %(message)s",
    )


def faulty_task() -> None:
    time.sleep(0.1)
    raise RuntimeError("something went wrong")


def safe_task() -> None:
    logging.info("safe task running")


def demo_excepthook() -> None:
    def handler(args: threading.ExceptHookArgs) -> None:
        print(f"[excepthook] thread={args.thread.name} exception={args.exc_type.__name__}: {args.exc_value}")

    threading.excepthook = handler  # type: ignore[assignment]

    t = threading.Thread(target=faulty_task, name="faulty-thread")
    t.start()
    t.join()


def main() -> None:
    configure_logging()
    logging.info("main thread start")

    t1 = threading.Thread(target=safe_task, name="worker-1")
    t1.start()
    t1.join()

    print("\n== excepthook 演示 ==")
    demo_excepthook()
    logging.info("main thread end")


if __name__ == "__main__":
    main()
