#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：Cookie 持久化。
Author: Lambert

题目：
实现 Cookie 的保存和加载，使用 LWPCookieJar。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/09_cookie_jar.py
"""

from __future__ import annotations

import requests
from http.cookiejar import LWPCookieJar
from pathlib import Path


def create_session_with_cookies(cookie_file: Path) -> requests.Session:
    """创建带 Cookie 持久化的 Session"""
    session = requests.Session()
    cookie_jar = LWPCookieJar(filename=cookie_file)

    # 加载已保存的 cookies
    if cookie_file.exists():
        cookie_jar.load(ignore_discard=True)

    session.cookies = cookie_jar
    return session


def main() -> None:
    cookie_file = Path("/tmp/cookies.txt")

    # 清理旧文件
    if cookie_file.exists():
        cookie_file.unlink()

    # 创建 Session
    session = create_session_with_cookies(cookie_file)

    # 设置 cookies
    session.get("https://httpbin.org/cookies/set?user=alice&session=abc123")
    print(f"Cookies after set: {session.cookies.get_dict()}")

    # 保存 cookies
    session.cookies.save(ignore_discard=True)
    print(f"[OK] cookies saved to {cookie_file}")

    # 创建新 Session 并加载 cookies
    session2 = create_session_with_cookies(cookie_file)
    print(f"Cokies after load: {session2.cookies.get_dict()}")

    # 验证 cookies 被正确加载
    assert session2.cookies.get_dict().get("user") == "alice"
    assert session2.cookies.get_dict().get("session") == "abc123"
    print("[OK] cookies loaded correctly")

    # 使用 cookies 发送请求
    response = session2.get("https://httpbin.org/cookies")
    cookies_sent = response.json()["cookies"]
    assert cookies_sent["user"] == "alice"
    print("[OK] cookies sent with request")

    # 清理
    session.close()
    session2.close()
    cookie_file.unlink()
    print("[OK] cleanup")


if __name__ == "__main__":
    main()