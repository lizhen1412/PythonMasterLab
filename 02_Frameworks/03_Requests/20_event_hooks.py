#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 20：事件钩子（Event Hooks）。

要点：
- hooks 参数：监听请求/响应生命周期事件
- response 钩子：在响应返回后执行，可修改响应或触发副作用
- 常见用途：日志记录、性能监控、错误处理、响应缓存

运行：
    python3 02_Frameworks/03_Requests/20_event_hooks.py
"""

from __future__ import annotations

import time
import requests


def demo_logging_hook() -> None:
    """演示日志记录钩子"""
    def log_response(response, *args, **kwargs):
        print(f"  [日志] 状态码: {response.status_code}")
        print(f"  [日志] URL: {response.url}")
        print(f"  [日志] 耗时: {response.elapsed.total_seconds()}s")
        return response

    session = requests.Session()
    session.hooks = {"response": log_response}

    print("=== 日志记录钩子 ===")
    session.get("https://httpbin.org/get", timeout=5)


def demo_error_handling_hook() -> None:
    """演示错误处理钩子"""
    def handle_error(response, *args, **kwargs):
        if response.status_code >= 400:
            print(f"  [错误] 请求失败: {response.status_code}")
            # 可以在这里触发告警、重试等逻辑
        return response

    session = requests.Session()
    session.hooks = {"response": handle_error}

    print("\n=== 错误处理钩子 ===")
    print("正常请求:")
    session.get("https://httpbin.org/get", timeout=5)

    print("\n错误请求:")
    session.get("https://httpbin.org/status/404", timeout=5)


def demo_multiple_hooks() -> None:
    """演示多个钩子组合"""
    def hook1(response, *args, **kwargs):
        response.hook1_called = True
        return response

    def hook2(response, *args, **kwargs):
        response.hook2_called = True
        return response

    def hook3(response, *args, **kwargs):
        response.hook3_called = True
        return response

    session = requests.Session()
    session.hooks = {"response": [hook1, hook2, hook3]}

    print("\n=== 多个钩子组合 ===")
    resp = session.get("https://httpbin.org/get", timeout=5)
    print(f"hook1 被调用: {getattr(resp, 'hook1_called', False)}")
    print(f"hook2 被调用: {getattr(resp, 'hook2_called', False)}")
    print(f"hook3 被调用: {getattr(resp, 'hook3_called', False)}")


def demo_modify_response() -> None:
    """演示修改响应内容"""
    def add_custom_header(response, *args, **kwargs):
        # 为响应添加自定义属性
        response.custom_field = "custom_value"
        return response

    session = requests.Session()
    session.hooks = {"response": add_custom_header}

    print("\n=== 修改响应内容 ===")
    resp = session.get("https://httpbin.org/get", timeout=5)
    print(f"自定义字段: {getattr(resp, 'custom_field', None)}")


def demo_timing_hook() -> None:
    """演示性能监控钩子"""
    timings: list[dict] = []

    def record_timing(response, *args, **kwargs):
        timings.append({
            "url": response.url,
            "status": response.status_code,
            "elapsed": response.elapsed.total_seconds(),
        })
        return response

    session = requests.Session()
    session.hooks = {"response": record_timing}

    print("\n=== 性能监控钩子 ===")
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/json",
    ]

    for url in urls:
        session.get(url, timeout=10)

    print("请求统计:")
    for t in timings:
        print(f"  {t['url']} -> {t['status']} ({t['elapsed']:.3f}s)")


def demo_hook_with_exception() -> None:
    """演示钩子中抛出异常"""
    def failing_hook(response, *args, **kwargs):
        if response.status_code == 500:
            raise ValueError("服务器错误！")
        return response

    session = requests.Session()
    session.hooks = {"response": failing_hook}

    print("\n=== 钩子异常处理 ===")
    print("正常请求:")
    session.get("https://httpbin.org/get", timeout=5)

    print("\n会触发异常的请求:")
    try:
        session.get("https://httpbin.org/status/500", timeout=5)
    except ValueError as e:
        print(f"  捕获异常: {e}")


def main() -> None:
    print("=== 事件钩子演示 ===\n")
    demo_logging_hook()
    demo_error_handling_hook()
    demo_multiple_hooks()
    demo_modify_response()
    demo_timing_hook()
    demo_hook_with_exception()

    print("\n使用建议:")
    print("  - 钩子按注册顺序执行")
    print("  - 钩子应返回 response 对象，否则可能影响后续处理")
    print("  - 钩子中抛出异常会中断请求链")
    print("  - 钩子适合做日志、监控、缓存等横切关注点")


if __name__ == "__main__":
    main()
