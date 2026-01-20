# Requests 2.32.3 学习笔记（03_Requests）

本章覆盖 `requests` 2.32.3 的完整能力：从基础到进阶，包括构建与发送请求、查询参数与头、表单与 JSON、响应解析、超时与异常、`raise_for_status`、会话与 Cookie、重定向、流式下载、文件上传、认证与重试、代理配置、SSL 验证、事件钩子、连接池、URL 编码、Cookie 持久化、底层流访问、DNS 与连接复用、AsyncIO 集成等。示例使用 httpbin.org 公共接口（无需自己启动本地服务）。

版本要求：`requests==2.32.3`
安装方式：项目已配置，使用 `uv sync` 或 `pip install requests`

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 02_Frameworks/03_Requests/01_overview.py`
- 跑单个示例：`python3 02_Frameworks/03_Requests/04_get_httpbin_json.py`

---

## 2) 知识点全景清单

### 基础内容 (02-15)
- 安装与版本检查、`PreparedRequest` 观察最终 URL/头
- GET：查询参数、定制头、构建但不发送
- 响应解析：`status_code/headers/text/content/json/encoding`
- POST：表单 vs JSON、服务器端看到的区别
- 超时与异常：`Timeout`、`ConnectionError`、`HTTPError`
- `raise_for_status` 与状态码判断
- `Session`：连接复用、默认头、Cookie 持久化
- 重定向与历史：`allow_redirects`、`response.history`
- 流式下载：`stream=True`、`iter_content` 与保存文件
- 文件上传：`files` 参数、服务器如何看到 multipart
- 认证：Basic Auth、定制头
- 重试：`HTTPAdapter` + `urllib3.Retry`、限制重试条件

### 进阶内容 (16-28)
- **HTTP 方法完整演示**：PUT/PATCH/DELETE/HEAD/OPTIONS
- **代理配置**：HTTP/HTTPS 代理、带认证代理、环境变量
- **SSL/TLS 证书验证**：证书验证控制、自定义 CA、客户端证书
- **扩展认证**：Digest Auth、Bearer Token、API Key
- **事件钩子**：请求/响应生命周期监听、日志记录、性能监控
- **连接池配置**：pool_connections、pool_maxsize、连接复用优化
- **原始请求体**：手动构建请求体、自定义 Content-Type
- **URL 编码**：quote/unquote、特殊字符处理、中文编码
- **Cookie 持久化**：LWPCookieJar、MozillaCookieJar、跨会话保存
- **底层流访问**：Response.raw、read/read1/readinto、与 iter_content 区别
- **DNS 与连接复用**：连接复用原理、Keep-Alive、性能对比
- **AsyncIO 集成**：run_in_executor、asyncio.gather、与 aiohttp 对比

---

## 3) 文件总览

### 基础部分 (02-15)

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引 |
| 02 | [`02_install_and_version.py`](02_install_and_version.py) | 安装与版本检查 |
| 03 | [`03_prepare_get_and_params.py`](03_prepare_get_and_params.py) | 构建 GET/参数/头，不发送 |
| 04 | [`04_get_httpbin_json.py`](04_get_httpbin_json.py) | GET + JSON 解析（httpbin） |
| 05 | [`05_post_form_vs_json.py`](05_post_form_vs_json.py) | 表单 vs JSON 请求体 |
| 06 | [`06_response_attributes.py`](06_response_attributes.py) | 响应属性：text/content/json/encoding |
| 07 | [`07_timeouts_and_errors.py`](07_timeouts_and_errors.py) | 超时、连接错误、异常捕获 |
| 08 | [`08_raise_for_status.py`](08_raise_for_status.py) | `raise_for_status` 与状态码 |
| 09 | [`09_session_and_cookies.py`](09_session_and_cookies.py) | Session 复用与 Cookie 持久化 |
| 10 | [`10_redirects_and_history.py`](10_redirects_and_history.py) | 重定向处理与历史记录 |
| 11 | [`11_streaming_download.py`](11_streaming_download.py) | 流式下载与 chunk 迭代 |
| 12 | [`12_upload_files_multipart.py`](12_upload_files_multipart.py) | 文件上传 multipart |
| 13 | [`13_basic_auth.py`](13_basic_auth.py) | Basic Auth 示例 |
| 14 | [`14_retries_and_adapter.py`](14_retries_and_adapter.py) | 连接池与重试策略 |
| 15 | [`15_chapter_summary.py`](15_chapter_summary.py) | 基础章节总结 |

### 进阶部分 (16-28)

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 16 | [`16_http_methods.py`](16_http_methods.py) | HTTP 方法完整演示：PUT/PATCH/DELETE/HEAD/OPTIONS |
| 17 | [`17_proxies.py`](17_proxies.py) | 代理配置：HTTP/HTTPS 代理、带认证代理 |
| 18 | [`18_ssl_verification.py`](18_ssl_verification.py) | SSL/TLS 证书验证控制、客户端证书 |
| 19 | [`19_auth_extended.py`](19_auth_extended.py) | 扩展认证：Digest Auth、Bearer Token、API Key |
| 20 | [`20_event_hooks.py`](20_event_hooks.py) | 事件钩子：请求/响应生命周期监听 |
| 21 | [`21_connection_pool.py`](21_connection_pool.py) | 连接池配置与性能优化 |
| 22 | [`22_raw_request_body.py`](22_raw_request_body.py) | 原始请求体与自定义 Content-Type |
| 23 | [`23_url_encoding.py`](23_url_encoding.py) | URL 编码与解码、特殊字符处理 |
| 24 | [`24_cookiejar_and_persistence.py`](24_cookiejar_and_persistence.py) | Cookie 持久化与文件保存 |
| 25 | [`25_response_raw_stream.py`](25_response_raw_stream.py) | Response.raw 底层流访问 |
| 26 | [`26_dns_and_connection_reuse.py`](26_dns_and_connection_reuse.py) | DNS 缓存与连接复用原理 |
| 27 | [`27_asyncio_integration.py`](27_asyncio_integration.py) | 在 AsyncIO 中使用 requests |
| 28 | [`28_advanced_summary.py`](28_advanced_summary.py) | 进阶内容总结 |

---

## 4) 运行提示

- 示例依赖 httpbin.org 公共接口，运行时需要可访问外网。
- 如未安装 `requests`，请先 `uv sync` 或 `pip install requests`。
- Mac/Linux 默认可直接使用 `python3 <脚本路径>` 运行。

---

## 5) 学习路径建议

1. **基础入门** (02-15)：从安装开始，依次学习 GET/POST、响应处理、异常、Session、重定向、流式下载、文件上传、认证和重试。

2. **进阶提升** (16-28)：学习完整的 HTTP 方法、代理、SSL、高级认证、事件钩子、连接池优化、URL 编码、Cookie 持久化、底层流访问和 AsyncIO 集成。

3. **实践建议**：
   - 每个示例都可直接运行，建议按顺序学习
   - 结合 httpbin.org 观察请求/响应细节
   - 务必使用 Session 复用连接提升性能
   - 生产环境注意 SSL 证书验证和错误处理
