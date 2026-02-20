#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：设计带关键字仅限参数的 API。
Author: Lambert

要求：
- 定义一个函数，位置参数只接收核心数据，其他配置改为“关键字仅限”
- 演示正确与错误调用，观察错误信息
"""

from __future__ import annotations

from typing import Any


def send_email(to: str, subject: str, /, *, cc: list[str] | None = None, bcc: list[str] | None = None, urgent: bool = False) -> dict[str, Any]:
    """
    - to/subject 必须以位置传递，避免调用时漏写参数名导致歧义
    - cc/bcc/urgent 必须写成关键字，调用更可读且不易错位
    """
    return {
        "to": to,
        "subject": subject,
        "cc": cc or [],
        "bcc": bcc or [],
        "urgent": urgent,
    }


def show_calls() -> None:
    """展示合法与非法调用。"""
    ok = send_email("user@example.com", "Hello", cc=["boss@example.com"], urgent=True)
    print("合法调用 ->", ok)

    try:
        # 缺少关键字仅限参数写法，故意触发错误
        send_email("user@example.com", "Hi", ["boss@example.com"])  # type: ignore[arg-type]
    except TypeError as exc:
        print("错误调用 TypeError ->", exc)


def main() -> None:
    show_calls()


if __name__ == "__main__":
    main()