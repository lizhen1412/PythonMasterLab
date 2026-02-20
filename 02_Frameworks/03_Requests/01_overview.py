#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：requests 2.32.3 学习索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/03_Requests/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_install_and_version.py", "安装与版本检查"),
    ("03_prepare_get_and_params.py", "构建 GET/参数/头，不发送"),
    ("04_get_httpbin_json.py", "GET + JSON 解析（httpbin）"),
    ("05_post_form_vs_json.py", "表单 vs JSON 请求体"),
    ("06_response_attributes.py", "响应属性 text/content/json/encoding"),
    ("07_timeouts_and_errors.py", "超时、连接错误、异常捕获"),
    ("08_raise_for_status.py", "raise_for_status 与状态码"),
    ("09_session_and_cookies.py", "Session 复用与 Cookie"),
    ("10_redirects_and_history.py", "重定向与 history"),
    ("11_streaming_download.py", "流式下载与 iter_content"),
    ("12_upload_files_multipart.py", "文件上传 multipart"),
    ("13_basic_auth.py", "Basic Auth 示例"),
    ("14_retries_and_adapter.py", "连接池与重试策略"),
    ("15_chapter_summary.py", "基础章节总结"),
    # 进阶内容 (16-28)
    ("16_http_methods.py", "HTTP 方法完整演示：PUT/PATCH/DELETE/HEAD/OPTIONS"),
    ("17_proxies.py", "代理配置：HTTP/HTTPS 代理、带认证代理"),
    ("18_ssl_verification.py", "SSL/TLS 证书验证控制、客户端证书"),
    ("19_auth_extended.py", "扩展认证：Digest Auth、Bearer Token、API Key"),
    ("20_event_hooks.py", "事件钩子：请求/响应生命周期监听"),
    ("21_connection_pool.py", "连接池配置与性能优化"),
    ("22_raw_request_body.py", "原始请求体与自定义 Content-Type"),
    ("23_url_encoding.py", "URL 编码与解码、特殊字符处理"),
    ("24_cookiejar_and_persistence.py", "Cookie 持久化与文件保存"),
    ("25_response_raw_stream.py", "Response.raw 底层流访问"),
    ("26_dns_and_connection_reuse.py", "DNS 缓存与连接复用原理"),
    ("27_asyncio_integration.py", "在 AsyncIO 中使用 requests"),
    ("28_advanced_summary.py", "进阶内容总结"),
    ("Exercises/01_overview.py", "练习索引"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()