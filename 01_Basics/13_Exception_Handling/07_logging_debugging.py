#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：代码调试（日志 logging）

你会学到：
1) logging 分级：DEBUG/INFO/WARNING/ERROR
2) logger.exception(...)：在 except 里打印带 traceback 的错误日志
3) 为什么在“可复用代码”里更推荐 logging 而不是 print

运行（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/07_logging_debugging.py
"""

from __future__ import annotations

import logging


def configure_logging(level: int = logging.DEBUG) -> None:
    logging.basicConfig(
        level=level,
        format="%(levelname)s %(name)s: %(message)s",
    )


logger = logging.getLogger("exception-demo")


def divide(a: float, b: float) -> float:
    logger.debug("divide called: a=%s b=%s", a, b)
    return a / b


def main() -> None:
    configure_logging(logging.DEBUG)

    logger.info("start demo")
    logger.debug("this is a debug message")

    try:
        divide(1, 0)
    except ZeroDivisionError:
        logger.exception("divide failed")

    logger.warning("end demo (warning is visible at INFO level and above)")


if __name__ == "__main__":
    main()

