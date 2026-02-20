#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: logging handlers and filters.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/06_logging_handlers_and_filters.py
"""

import logging


class KeywordFilter(logging.Filter):
    def __init__(self, blocked: str) -> None:
        super().__init__()
        self.blocked = blocked

    def filter(self, record: logging.LogRecord) -> bool:
        return self.blocked not in record.getMessage()


def main() -> None:
    logger = logging.getLogger("demo")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))
    handler.addFilter(KeywordFilter("skip"))

    logger.handlers.clear()
    logger.addHandler(handler)

    logger.info("hello")
    logger.info("this should be skipped")
    logger.warning("warn message")


if __name__ == "__main__":
    main()