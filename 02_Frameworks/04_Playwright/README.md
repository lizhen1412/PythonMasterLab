# Playwright 1.58.0 学习笔记（04_Playwright）

本章是"可直接运行"的 Playwright Python 教程，结构对齐 `01_Basics`：
- 主课：`01_overview.py` 里按编号顺序学习
- 练习：`Exercises/01_overview.py` 里按编号实操

目标：
- 对齐官网入门主线（Installation / Writing tests / Running and debugging / Trace viewer / Library）
- 对照 `third_party_refs/playwright-python`，补齐核心到高级 API 知识点
- 保持小白可读：每个脚本独立、可单跑、尽量减少外网依赖

---

## 1) 快速开始

在仓库根目录运行：

- 索引：`python3 02_Frameworks/04_Playwright/01_overview.py`
- 先跑 02（安装检查）：`python3 02_Frameworks/04_Playwright/02_install_and_version.py`
- 练习索引：`python3 02_Frameworks/04_Playwright/Exercises/01_overview.py`

---

## 2) 环境准备

- 安装指定版本：`python3 -m pip install playwright==1.58.0`
- 安装浏览器：`python3 -m playwright install`

---

## 3) 官网主线覆盖（文件映射）

- Intro / Installation：
  - `02_install_and_version.py`（安装与版本检查）
  - `03_persistent_context_and_cdp_intro.py`（持久化上下文与 CDP 连接）
- Library（sync / async）：
  - `04_sync_playwright_start.py`
  - `14_async_api_basics.py`
  - `21_api_request_context.py`
- Writing tests（角色定位、动作、断言）：
  - `33_writing_tests_official_flow.py`
  - `34_locator_actions_all.py`
  - `35_expect_assertions_all.py`
- Running and debugging：
  - `07_wait_for_and_timeouts.py`
  - `11_error_handling_and_retries.py`
  - `29_pytest_plugin_basics.py`
  - `30_codegen_and_debug_commands.py`
- Trace viewer：
  - `09_screenshot_and_trace.py`
- 高级事件与 context：
  - `42_advanced_events_and_context.py`

---

## 4) 方法级覆盖（高频 API）

已覆盖的入门高频方法示例：

- 页面与定位：
  - `page.goto`、`page.locator`、`page.get_by_role`、`page.frame_locator`
- locator 动作：
  - `fill`、`click`、`check`、`uncheck`、`hover`、`focus`、`press`、`set_input_files`、`select_option`
- expect 断言：
  - `to_have_title`、`to_have_url`
  - `to_be_visible`、`to_be_checked`、`to_be_enabled`
  - `to_contain_text`、`to_have_attribute`、`to_have_count`、`to_have_text`、`to_have_value`
- 网络与等待：
  - `page.route`、`route.fulfill`、`route.abort`、`route.continue_`、`route.fallback`
  - `page.expect_request`、`page.expect_response`、`page.wait_for_url`、`page.wait_for_function`
- 兼容旧写法（读 third_party 老代码）：
  - `page.query_selector`、`page.query_selector_all`
  - `page.eval_on_selector`、`page.eval_on_selector_all`
- context 与隔离：
  - `browser.new_context`、`context.route`、`context.unroute`、`context.clear_cookies`、`context.storage_state`
- 设备输入：
  - `page.keyboard`（`type/press/down/up/insert_text`）
  - `page.mouse`（`move/click/dblclick/wheel`）
- 稀有高级 API 总览：
  - `99_api_surface_full_catalog.py`

---

## 5) 与 third_party_refs 对照

`third_party_refs/playwright-python/tests` 是工程级 API 全集。
本章采用"双层覆盖"：
- 可运行示例：覆盖官网主线 + 高频实战
- 静态目录示例：`99_api_surface_full_catalog.py` 覆盖稀有高级方法入口（便于查漏补缺）

可执行覆盖检查脚本查看差异：

- `python3 02_Frameworks/04_Playwright/90_method_coverage_check.py`
- 关注 `[2] third_party 严格方法集合覆盖`：
  - 当前目标：`169/169`（方法名维度）
  - `[3]` 的缺口是"接收者变量名粒度"的粗统计，不代表真实遗漏

---

## 6) 学习路径建议（新手）

1. `02` -> `09`：先跑通最基础流程
2. `14` -> `20`：补齐 async、frame、下载、视频
3. `33` -> `42`：专门练"方法级"核心 API
4. `43` -> `46`：高级参数配置（生产环境必备）
5. `47` -> `49`：真实项目场景（电商爬虫、自动化测试、网站监控）
6. `99`：回看全 API 知识点目录，按需补高级场景
7. `Exercises/02` -> `Exercises/18`：每个练习至少手改一次参数/选择器

---

## 7) 高级参数配置（43-46 号）

生产环境的爬虫和自动化项目通常需要精细的参数配置：

### `43_advanced_launch_parameters.py` - launch_persistent_context 参数大全

```python
# 持久化上下文完整配置示例
context = p.chromium.launch_persistent_context(
    user_data_dir="/path/to/profile",
    headless=True,

    # 视口和显示
    viewport={"width": 1920, "height": 1080},
    device_scale_factor=1.0,
    color_scheme="light",

    # 网络配置
    proxy={"server": "http://proxy.com:8080"},
    ignore_https_errors=True,
    offline=False,

    # 用户代理和语言
    user_agent="Custom User Agent",
    locale="zh-CN",
    timezone_id="Asia/Shanghai",

    # 性能
    slow_mo=100,  # 减慢操作速度
    timeout=30000,

    # 录制
    record_har_path="/path/to/file.har",
    record_video_dir="/path/to/videos",
)
```

### `44_advanced_page_navigation.py` - page.goto 参数大全

```python
# 导航完整配置示例
page.goto(
    "https://example.com",
    wait_until="load",  # 'load' | 'domcontentloaded' | 'networkidle' | 'commit'
    timeout=60000,
    headers={"X-Custom": "value"},
)
```

### `45_advanced_new_context_parameters.py` - new_context 参数大全

```python
# 上下文完整配置示例
context = browser.new_context(
    viewport={"width": 1920, "height": 1080},
    user_agent="Custom UA",
    locale="zh-CN",
    timezone_id="Asia/Shanghai",
    permissions=["geolocation"],
    storage_state_path="/path/to/state.json",
    record_har_path="/path/to/file.har",
    ignore_https_errors=True,
)
```

### `46_advanced_locator_usage.py` - locator 高级用法

```python
# locator 选项参数
locator.click(
    button="left",
    position={"x": 10, "y": 10},
    delay=100,
    force=False,
    timeout=30000,
)

# locator 过滤器
items.filter(has_text="text")
items.filter(has=page.locator(".active"))
items.nth(1)
items.first
items.last
```

---

## 8) 真实项目场景（47-49 号）

生产环境级别的综合示例，展示如何组合使用各种 API 解决实际问题。

### `47_real_ecommerce_crawler.py` - 电商网站爬虫系统

**业务场景：**
- 模拟用户登录并保持会话（持久化上下文）
- 轮换代理 IP（反反爬虫）
- 翻页采集商品信息（处理懒加载）
- 下载商品图片（并发控制）
- 数据保存到 JSON/CSV

**涉及 API：**
- `launch_persistent_context` - 持久化登录状态
- `proxy` - 代理配置
- `storage_state` - 保存/恢复登录状态
- `wait_for_load_state` - 等待网络空闲
- `locator.filter` - 过滤商品元素
- `screenshot` - 保存截图
- `route` - 请求拦截
- `tracing` - 追踪记录

```python
# 持久化上下文 + 代理配置
context = p.chromium.launch_persistent_context(
    user_data_dir="/path/to/profile",
    headless=True,
    proxy={"server": "http://proxy.com:8080"},
    storage_state="storage_state.json",
)

# 采集商品
products_locator = page.locator(".product-item")
for i in range(products_locator.count()):
    product = extract_product_info(products_locator.nth(i))
```

### `48_real_test_suite.py` - Web 自动化测试套件

**业务场景：**
- 用户注册/登录流程测试
- 表单验证测试
- 文件上传测试
- 弹窗处理测试
- 多浏览器兼容性测试
- 移动端设备模拟测试
- 测试报告生成（HTML/JSON）

**涉及 API：**
- `browser.new_context` - 创建隔离测试环境
- `expect` 断言 - 各种验证方法
- `set_input_files` - 文件上传
- `expect_dialog` - 处理弹窗
- `tracing.start/stop` - 记录测试 trace
- `devices` - 模拟移动设备
- `locator` - 元素定位和操作

```python
# 移动端测试
context = browser.new_context(**p.devices["iPhone 13"])
page = context.new_page()

# 文件上传测试
page.set_input_files("#file-upload", "/path/to/file.pdf")
page.click("#upload-btn")

# 断言验证
expect(page.locator("#success-message")).to_be_visible()
```

### `49_real_monitoring.py` - 网站健康监控系统

**业务场景：**
- 定期检查多个 URL 的可用性
- 视觉回归测试（截图对比）
- 性能监控（响应时间、资源加载）
- API 健康检查
- 关键字内容验证
- 错误告警（截图 + Trace 记录）

**涉及 API：**
- `APIRequestContext` - 快速 API 检查
- `page.evaluate` - 获取性能指标
- `screenshot` - 视觉回归
- `wait_for_load_state` - 等待加载状态
- `timeout` - 超时控制
- `tracing` - 错误追踪

```python
# 快速健康检查
api_context = p.request.new_context()
response = api_context.get("https://example.com", timeout=5000)

# 完整监控
page.goto("https://example.com", wait_until="networkidle")
metrics = page.evaluate("() => performance.timing")

# 截图对比
page.screenshot(path="screenshot.png")
hash = calculate_screenshot_hash("screenshot.png")
```

---

## 9) 高级 API 完整覆盖（50-52 号）

通过分析 third_party_refs/playwright-python，新增三个高级 API 示例文件，覆盖之前未涉及的高级功能。

### `50_websocket_worker_advanced.py` - WebSocket 和 Worker

**WebSocket API：**
- `page.expect_websocket()` - 等待 WebSocket 创建
- `ws.on("framesent/framereceived/close")` - WebSocket 事件监听
- `ws.wait_for_event()` - 等待特定事件
- `ws.url` / `ws.is_closed()` - WebSocket 属性
- `page.route_web_socket()` - WebSocket 拦截和 Mock

**Worker API：**
- `page.expect_worker()` - 等待 Worker 创建
- `page.workers` - 获取所有 Worker
- `worker.evaluate()` - 在 Worker 中执行代码
- `context.service_workers` - Service Worker 列表
- `context.new_cdp_session(worker)` - CDP 与 Worker 交互

```python
# WebSocket 连接和事件监听
ws = page.expect_websocket()
ws.on("framereceived", lambda payload: print(f"收到: {payload}"))

# Worker 代码执行
worker = page.expect_worker()
result = worker.evaluate("() => self.location.href")
```

### `51_har_cdp_advanced.py` - HAR 和 CDP

**HAR (HTTP Archive)：**
- `record_har_path` - HAR 录制路径
- `record_har_content` - "omit" / "embed" / "attach"
- `record_har_mode` - "full" / "minimal"
- `route_from_har()` - 从 HAR 回放请求
- HAR ZIP 格式支持（外部内容）

**CDP (Chrome DevTools Protocol)：**
- `context.new_cdp_session(page)` - 创建 CDP 会话
- `cdpsession.send()` - 发送 CDP 命令
- `cdpsession.on()` - 监听 CDP 事件
- `browser_type.connect_over_cdp()` - 通过 CDP 连接浏览器

```python
# HAR 录制
context = browser.new_context(
    record_har_path="network.har",
    record_har_content="embed",
    record_har_mode="full",
)

# CDP 命令
cdp = context.new_cdp_session(page)
cdp.send("Performance.enable")
metrics = cdp.send("Performance.getMetrics")
```

### `52_accessibility_other_advanced.py` - Accessibility、Coverage 等

**Accessibility（无障碍）：**
- `page.accessibility.snapshot()` - 获取无障碍树
- `locator.aria_snapshot()` - ARIA 快照
- `expect(locator).to_match_aria_snapshot()` - 匹配快照
- AXNode 属性：role, name, value, checked, expanded

**Code Coverage（代码覆盖率）：**
- `page.start_js_coverage()` / `stop_js_coverage()` - JS 覆盖率
- `page.start_css_coverage()` / `stop_css_coverage()` - CSS 覆盖率

**PDF 生成：**
- `page.pdf()` - 生成 PDF
- 格式、页边距、页眉页脚配置
- 选择器转 PDF

**Video 录制：**
- `record_video_dir` - 视频录制目录
- `page.video.path()` - 视频文件路径

**Locator 高级选择器：**
- `page.get_by_text()` / `locator.get_by_text()`
- `page.get_by_role()` / `locator.get_by_role()`
- `page.get_by_label()` / `locator.get_by_label()`
- `page.get_by_placeholder()` / `locator.get_by_placeholder()`
- `page.get_by_alt_text()` / `locator.get_by_alt_text()`
- `page.get_by_title()` / `locator.get_by_title()`
- `page.get_by_test_id()` / `locator.get_by_test_id()`

```python
# Accessibility 快照
snapshot = page.accessibility.snapshot()
aria = page.locator("nav").aria_snapshot()

# 覆盖率收集
page.start_js_coverage()
# ... 执行代码 ...
coverage = page.stop_js_coverage()

# PDF 生成
page.pdf(path="output.pdf", format="A4", print_background=True)

# 高级选择器
btn = page.get_by_role("button", name="Submit")
input = page.get_by_label("Username")
img = page.get_by_alt_text("Logo")
```

---

## 10) 学习路径更新

1. `02` -> `09`：基础流程
2. `14` -> `20`：async、frame、下载、视频
3. `33` -> `42`：核心 API
4. `43` -> `46`：高级参数配置
5. `47` -> `49`：真实项目场景
6. `50` -> `52`：高级 API 完整覆盖（WebSocket、Worker、HAR、CDP、Accessibility、Coverage）
7. `99`：全 API 目录
8. `Exercises/`：练习
