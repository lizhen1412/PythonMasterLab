#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 24：Cookie 持久化。

要点：
- LWPCookieJar/MozillaCookieJar：Cookie 文件格式
- save()：将 Cookie 保存到文件
- load()：从文件加载 Cookie
- 跨会话保持登录状态
- Cookie 过期时间、域名、路径限制

运行：
    python3 02_Frameworks/03_Requests/24_cookiejar_and_persistence.py
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import requests
from http.cookiejar import LWPCookieJar, MozillaCookieJar


def demo_lwp_cookiejar() -> None:
    """演示 LWPCookieJar 的保存与加载"""
    print("=== LWPCookieJar 持久化 ===")

    # 创建临时文件
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        cookie_file = f.name

    try:
        # 创建 CookieJar 并设置 Cookie
        jar = LWPCookieJar()
        session = requests.Session()
        session.cookies = jar

        # 设置一些 Cookie
        session.get("https://httpbin.org/cookies/set/session/abc123", timeout=5)
        session.get("https://httpbin.org/cookies/set/user/alice", timeout=5)

        print(f"当前 Cookies: {dict(session.cookies)}")

        # 保存到文件
        jar.save(cookie_file)
        print(f"Cookie 已保存到: {cookie_file}")

        # 读取文件内容
        content = Path(cookie_file).read_text()
        print(f"\nCookie 文件内容预览:")
        print(content[:300])

        # 创建新 Session 并加载 Cookie
        new_jar = LWPCookieJar()
        new_jar.load(cookie_file)
        new_session = requests.Session()
        new_session.cookies = new_jar

        print(f"\n加载后的 Cookies: {dict(new_session.cookies)}")

        # 验证 Cookie 是否生效
        resp = new_session.get("https://httpbin.org/cookies", timeout=5)
        print(f"服务器收到的 Cookies: {resp.json()['cookies']}")

    finally:
        # 清理临时文件
        Path(cookie_file).unlink(missing_ok=True)


def demo_mozilla_cookiejar() -> None:
    """演示 MozillaCookieJar (浏览器格式)"""
    print("\n=== MozillaCookieJar (浏览器格式) ===")

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        cookie_file = f.name

    try:
        jar = MozillaCookieJar()
        session = requests.Session()
        session.cookies = jar

        session.get("https://httpbin.org/cookies/set/name/value", timeout=5)

        # 保存为 Mozilla 格式（与浏览器兼容）
        jar.save(cookie_file, ignore_discard=True, ignore_expires=True)
        print(f"已保存为 Mozilla 格式: {cookie_file}")

        # 文件内容
        content = Path(cookie_file).read_text()
        print(f"\n文件内容:")
        print(content)

    finally:
        Path(cookie_file).unlink(missing_ok=True)


def demo_cookie_attributes() -> None:
    """演示 Cookie 属性（域名、路径、过期）"""
    print("\n=== Cookie 属性 ===")

    jar = LWPCookieJar()
    session = requests.Session()
    session.cookies = jar

    # httpbin 的 /cookies/set 端点设置 Cookie
    session.get("https://httpbin.org/cookies/set/session/abc123", timeout=5)

    # 查看每个 Cookie 的详细属性
    for cookie in session.cookies:
        print(f"\nCookie: {cookie.name}")
        print(f"  值: {cookie.value}")
        print(f"  域名: {cookie.domain}")
        print(f"  路径: {cookie.path}")
        print(f"  过期时间: {cookie.expires}")
        print(f"  安全标志: {cookie.secure}")
        print(f"  HttpOnly: {cookie.has_nonstandard_attr('HttpOnly')}")


def demo_cross_session_persistence() -> None:
    """演示跨会话 Cookie 持久化"""
    print("\n=== 跨会话 Cookie 持久化 ===")

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        cookie_file = f.name

    try:
        # 会话1：登录并保存 Cookie
        print("会话1：模拟登录")
        session1 = requests.Session()
        session1.cookies = LWPCookieJar()

        session1.get("https://httpbin.org/cookies/set/user/alice", timeout=5)
        session1.get("https://httpbin.org/cookies/set/token/xyz789", timeout=5)

        session1.cookies.save(cookie_file)
        print(f"登录后 Cookie 已保存")

        # 会话2：加载 Cookie 并访问
        print("\n会话2：加载已保存的 Cookie")
        session2 = requests.Session()
        session2.cookies = LWPCookieJar()
        session2.cookies.load(cookie_file)

        resp = session2.get("https://httpbin.org/cookies", timeout=5)
        print(f"服务器收到的 Cookies: {resp.json()['cookies']}")
        print("Cookie 持久化成功！")

    finally:
        Path(cookie_file).unlink(missing_ok=True)


def demo_manual_cookie_setting() -> None:
    """演示手动设置 Cookie"""
    print("\n=== 手动设置 Cookie ===")

    session = requests.Session()

    # 方式1：使用 set() 方法
    session.cookies.set("name1", "value1")
    session.cookies.set("name2", "value2", domain="httpbin.org", path="/")

    # 方式2：使用字典
    session.cookies.update({"name3": "value3", "name4": "value4"})

    print(f"手动设置的 Cookies: {dict(session.cookies)}")

    # 验证
    resp = session.get("https://httpbin.org/cookies", timeout=5)
    print(f"服务器收到的: {resp.json()['cookies']}")


def demo_cookie_expiration() -> None:
    """演示 Cookie 过期处理"""
    print("\n=== Cookie 过期处理 ===")

    jar = LWPCookieJar()
    session = requests.Session()
    session.cookies = jar

    # 设置一个过期的 Cookie（手动演示）
    from datetime import datetime, timedelta

    # httpbin 的 /cookies/set/{name}/{value} 会设置会话 Cookie（浏览器关闭后过期）
    session.get("https://httpbin.org/cookies/set/temp/temp123", timeout=5)

    print(f"会话 Cookies（过期=None）:")
    for cookie in session.cookies:
        if cookie.expires is None:
            print(f"  {cookie.name}: 会话 Cookie")

    # 保存时会忽略过期的 Cookie（如果有）
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        cookie_file = f.name

    try:
        # ignore_discard=True 会保存会话 Cookie
        # ignore_expires=True 会保存过期的 Cookie
        jar.save(cookie_file, ignore_discard=True, ignore_expires=True)
        print(f"\nCookie 已保存（包含会话 Cookie）")

    finally:
        Path(cookie_file).unlink(missing_ok=True)


def main() -> None:
    print("=== Cookie 持久化演示 ===\n")
    demo_lwp_cookiejar()
    demo_mozilla_cookiejar()
    demo_cookie_attributes()
    demo_cross_session_persistence()
    demo_manual_cookie_setting()
    demo_cookie_expiration()

    print("\n使用建议:")
    print("  - LWPCookieJar：标准的 libwww-perl 格式，推荐使用")
    print("  - MozillaCookieJar：与浏览器兼容，便于调试")
    print("  - save() 时使用 ignore_discard=True 保存会话 Cookie")
    print("  - load() 前确保文件存在，否则会抛出异常")
    print("  - Cookie 文件包含敏感信息，注意权限保护")


if __name__ == "__main__":
    main()
