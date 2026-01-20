#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：用正则提取邮箱。

要求：
- 从一段文本提取所有邮箱地址，去重后输出
"""

from __future__ import annotations

import re


def extract_emails(text: str) -> list[str]:
    pattern = re.compile(r"[\\w.]+@[\\w.-]+")
    return sorted(set(pattern.findall(text)))


def main() -> None:
    text = """
    请联系 alice@example.com 或 bob@test.cn，
    也可以抄送 alice@example.com 和 dev@company.co.uk。
    """
    emails = extract_emails(text)
    print("提取到 ->", emails)


if __name__ == "__main__":
    main()
