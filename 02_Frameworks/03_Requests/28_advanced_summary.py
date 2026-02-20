#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 28：Requests 进阶内容总结。
Author: Lambert

本章涵盖 requests 的高级用法和最佳实践。

运行：
    python3 02_Frameworks/03_Requests/28_advanced_summary.py
"""

from __future__ import annotations


def main() -> None:
    print("=" * 60)
    print("Requests 进阶内容总结")
    print("=" * 60)

    topics = [
        ("HTTP 方法完整演示", [
            "PUT: 完整更新资源（幂等）",
            "PATCH: 部分更新资源",
            "DELETE: 删除资源",
            "HEAD: 只获取响应头（无 body）",
            "OPTIONS: 获取服务器支持的 HTTP 方法",
        ]),
        ("代理配置", [
            "proxies 参数设置 HTTP/HTTPS 代理",
            "带认证的代理: user:pass@host:port",
            "Session 级别的默认代理配置",
            "环境变量 HTTP_PROXY/HTTPS_PROXY",
        ]),
        ("SSL/TLS 证书验证", [
            "verify=True（默认）：验证 SSL 证书",
            "verify=False：关闭验证（仅测试）",
            "verify 指定自定义 CA bundle",
            "cert 参数：客户端证书认证",
        ]),
        ("扩展认证方式", [
            "Digest Auth: 摘要认证（HTTPDigestAuth）",
            "Bearer Token: OAuth 2.0 常用方式",
            "API Key: 通过 Header 或 Query 传递",
            "自定义 Header 认证",
        ]),
        ("事件钩子", [
            "hooks 参数监听请求/响应事件",
            "response 钩子：日志记录、性能监控",
            "多个钩子按顺序执行",
            "钩子可修改响应或触发副作用",
        ]),
        ("连接池配置", [
            "HTTPAdapter 控制 requests 连接池",
            "pool_connections: 连接池数量",
            "pool_maxsize: 每池最大连接数",
            "连接复用显著提升性能",
        ]),
        ("原始请求体", [
            "data 参数发送字符串/字节",
            "自定义 Content-Type 头",
            "发送 XML、纯文本、自定义格式",
            "json 参数自动设置 Content-Type",
        ]),
        ("URL 编码", [
            "requests 自动处理 params 编码",
            "quote/unquote: 手动 URL 编码/解码",
            "中文、空格、特殊字符自动编码",
            "quote(string, safe='/'): 保留安全字符",
        ]),
        ("Cookie 持久化", [
            "LWPCookieJar: 标准格式",
            "MozillaCookieJar: 浏览器兼容格式",
            "save()/load(): 保存/加载 Cookie",
            "跨会话保持登录状态",
        ]),
        ("Response.raw 底层流", [
            "raw 访问 urllib3 原始响应流",
            "stream=True 时 raw 可用",
            "read()/read1()/readinto() 方法",
            "与 iter_content() 的区别",
        ]),
        ("DNS 与连接复用", [
            "Session 复用 TCP 连接",
            "避免重复 DNS 解析和握手",
            "Keep-Alive 长连接机制",
            "连接池状态管理",
        ]),
        ("AsyncIO 集成", [
            "requests 是同步库",
            "run_in_executor() 在线程池中执行",
            "asyncio.gather() 并发请求",
            "推荐使用 aiohttp 实现真正异步",
        ]),
    ]

    for idx, (title, points) in enumerate(topics, 1):
        print(f"\n{idx}. {title}")
        print("-" * 60)
        for point in points:
            print(f"   • {point}")

    print("\n" + "=" * 60)
    print("学习建议")
    print("=" * 60)
    print("""
1. 基础优先
   - 熟练掌握 GET/POST/PUT/DELETE 等基础方法
   - 理解 Session 连接复用的重要性
   - 掌握异常处理和超时设置

2. 进阶技巧
   - 事件钩子用于日志和监控
   - 连接池配置提升高并发性能
   - Cookie 持久化实现免登录

3. 安全实践
   - 生产环境务必验证 SSL 证书
   - 敏感信息通过环境变量管理
   - API Key 放在 Header 中

4. 性能优化
   - 使用 Session 复用连接
   - 合理配置连接池大小
   - 大文件下载使用流式传输

5. 异步场景
   - 现有代码可用 run_in_executor 迁移
   - 新项目推荐使用 aiohttp
   - 理解同步和异步的性能差异

6. 调试技巧
   - PreparedRequest 查看最终请求
   - 响应钩子记录请求日志
   - httpbin.org 用于测试各种场景
    """)

    print("=" * 60)
    print("下一步学习")
    print("=" * 60)
    print("""
• aiohttp: 真正的异步 HTTP 客户端
• httpx: 现代化的 HTTP 客户端（同步/异步）
• urllib3: requests 底层库，更底层的控制
• websocket: WebSocket 协议支持
• pytest + requests: API 测试自动化
    """)


if __name__ == "__main__":
    main()