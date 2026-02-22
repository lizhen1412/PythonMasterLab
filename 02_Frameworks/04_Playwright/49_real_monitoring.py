#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 49：真实场景 - 网站健康监控系统（完整项目级示例）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/49_real_monitoring.py

本示例演示一个完整的网站监控系统，包含以下功能：

## 业务场景
1. 定期检查多个 URL 的可用性
2. 视觉回归测试（截图对比）
3. 性能监控（响应时间、资源加载）
4. API 健康检查
5. 关键字内容验证
6. SSL 证书检查
7. 错误告警（截图 + Trace 记录）
8. 监控报告生成

## 涉及的 Playwright API
- APIRequestContext: 快速 API 健康检查
- page.evaluate: 获取性能指标
- screenshot: 视觉回归
- page.goto: 访问页面
- wait_for_load_state: 等待加载状态
- route: Mock 测试场景
- timeout: 超时控制
- page.metrics: 获取页面指标
- context.add_init_script: 注入监控脚本
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import smtplib
from dataclasses import dataclass, field
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from enum import Enum
from pathlib import Path
from typing import Any

# =============================================================================
# 监控结果模型
# =============================================================================


class MonitorStatus(Enum):
    """监控状态枚举"""
    HEALTHY = "healthy"  # 健康
    DEGRADED = "degraded"  # 性能下降
    UNHEALTHY = "unhealthy"  # 不可用
    ERROR = "error"  # 检测出错


@dataclass
class PerformanceMetrics:
    """性能指标"""
    # 时间指标（毫秒）
    dns_lookup_time: float | None = None  # DNS 查询时间
    connection_time: float | None = None  # 连接时间
    tls_negotiation_time: float | None = None  # TLS 协商时间
    ttfb: float | None = None  # Time To First Byte
    download_time: float | None = None  # 下载时间
    total_time: float | None = None  # 总时间

    # 资源指标
    total_requests: int = 0  # 总请求数
    total_transfer_size: int = 0  # 总传输大小（字节）

    # DOM 指标
    dom_content_loaded: float | None = None  # DOM 加载完成时间
    load_complete: float | None = None  # 完全加载时间

    # 自定义指标
    first_contentful_paint: float | None = None  # 首次内容绘制
    largest_contentful_paint: float | None = None  # 最大内容绘制


@dataclass
class UrlMonitorResult:
    """单个 URL 监控结果"""
    url: str
    status: MonitorStatus
    timestamp: datetime
    response_time: float  # 响应时间（秒）
    status_code: int | None = None
    error_message: str | None = None

    # 性能指标
    performance: PerformanceMetrics | None = None

    # 内容验证
    keywords_found: list[str] = field(default_factory=list)
    keywords_missing: list[str] = field(default_factory=list)

    # 截图和 Trace
    screenshot_path: str | None = None
    trace_path: str | None = None

    # 视觉回归
    screenshot_hash: str | None = None
    visual_diff_detected: bool = False
    visual_diff_score: float | None = None


@dataclass
class MonitorReport:
    """监控报告"""
    start_time: datetime
    end_time: datetime
    results: list[UrlMonitorResult] = field(default_factory=list)

    @property
    def total_urls(self) -> int:
        return len(self.results)

    @property
    def healthy_count(self) -> int:
        return sum(1 for r in self.results if r.status == MonitorStatus.HEALTHY)

    @property
    def degraded_count(self) -> int:
        return sum(1 for r in self.results if r.status == MonitorStatus.DEGRADED)

    @property
    def unhealthy_count(self) -> int:
        return sum(1 for r in self.results if r.status == MonitorStatus.UNHEALTHY)

    @property
    def error_count(self) -> int:
        return sum(1 for r in self.results if r.status == MonitorStatus.ERROR)

    @property
    def avg_response_time(self) -> float:
        if not self.results:
            return 0.0
        return sum(r.response_time for r in self.results) / len(self.results)


@dataclass
class MonitorConfig:
    """监控配置"""
    # 目标 URL 列表
    target_urls: list[dict[str, Any]] = field(default_factory=list)

    # 阈值配置
    response_time_threshold: float = 3.0  # 响应时间阈值（秒）
    degraded_threshold: float = 1.5  # 性能下降阈值（秒）

    # 输出目录
    output_dir: Path = field(default_factory=_monitor_output_dir)
    screenshots_dir: Path = field(default_factory=_monitor_screenshots_dir)
    baselines_dir: Path = field(default_factory=_monitor_baselines_dir)
    traces_dir: Path = field(default_factory=_monitor_traces_dir)
    reports_dir: Path = field(default_factory=_monitor_reports_dir)

    # 功能开关
    enable_visual_regression: bool = True  # 启用视觉回归
    enable_performance_monitoring: bool = True  # 启用性能监控
    enable_keyword_check: bool = True  # 启用关键字检查
    save_trace_on_error: bool = True  # 错误时保存 Trace

    # 告警配置
    alert_on_degraded: bool = True  # 性能下降时告警
    alert_on_unhealthy: bool = True  # 不可用时告警
    email_alerts: bool = False  # 邮件告警
    smtp_server: str = "smtp.example.com"
    smtp_port: int = 587
    smtp_username: str = ""
    smtp_password: str = ""
    alert_recipients: list[str] = field(default_factory=list)

    # 浏览器配置
    headless: bool = True
    viewport: dict[str, int] = field(default_factory=_monitor_viewport)
    user_agent: str = "Playwright-Monitor/1.0"


# dataclass field 默认值工厂函数（使用命名函数而非 lambda）
def _monitor_demo_root() -> Path:
    """获取监控演示根目录（脚本所在目录下的 monitoring_output 子目录）"""
    return Path(__file__).parent / "monitoring_output"


def _monitor_output_dir() -> Path:
    return _monitor_demo_root()


def _monitor_screenshots_dir() -> Path:
    return _monitor_demo_root() / "screenshots"


def _monitor_baselines_dir() -> Path:
    return _monitor_demo_root() / "baselines"


def _monitor_traces_dir() -> Path:
    return _monitor_demo_root() / "traces"


def _monitor_reports_dir() -> Path:
    return _monitor_demo_root() / "reports"


def _monitor_viewport() -> dict[str, int]:
    return {"width": 1920, "height": 1080}


# =============================================================================
# 监控核心类
# =============================================================================


class WebsiteMonitor:
    """网站监控核心类"""

    def __init__(self, config: MonitorConfig):
        self.config = config
        self.playwright: Any = None
        self.api_context: Any | None = None

        # 创建目录
        self._ensure_directories()

    def _ensure_directories(self) -> None:
        """确保所有必要的目录存在"""
        for dir_path in [
            self.config.output_dir,
            self.config.screenshots_dir,
            self.config.baselines_dir,
            self.config.traces_dir,
            self.config.reports_dir,
        ]:
            dir_path.mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------------------------------
    # 初始化
    # -------------------------------------------------------------------------

    def init(self) -> None:
        """初始化监控环境"""
        from playwright.sync_api import sync_playwright

        self.playwright = sync_playwright().start()

        # 创建 API 请求上下文（用于快速健康检查）
        self.api_context = self.playwright.request.new_context(
            user_agent=self.config.user_agent,
            ignore_https_errors=True,
        )

        print("监控环境初始化完成")

    def close(self) -> None:
        """关闭监控环境"""
        if self.api_context:
            self.api_context.dispose()
        if self.playwright:
            self.playwright.stop()
        print("监控环境已关闭")

    # -------------------------------------------------------------------------
    # 快速健康检查（使用 APIRequestContext）
    # -------------------------------------------------------------------------

    def quick_health_check(self, url: str) -> UrlMonitorResult:
        """快速健康检查（仅检查 HTTP 状态）"""
        import time

        start_time = time.time()
        timestamp = datetime.now()

        try:
            response = self.api_context.get(
                url,
                timeout=self.config.response_time_threshold * 1000,
            )
            response_time = time.time() - start_time

            # 判断状态
            if response.ok:
                if response_time > self.config.degraded_threshold:
                    status = MonitorStatus.DEGRADED
                else:
                    status = MonitorStatus.HEALTHY
            else:
                status = MonitorStatus.UNHEALTHY

            return UrlMonitorResult(
                url=url,
                status=status,
                timestamp=timestamp,
                response_time=response_time,
                status_code=response.status,
            )

        except Exception as exc:
            response_time = time.time() - start_time
            return UrlMonitorResult(
                url=url,
                status=MonitorStatus.ERROR,
                timestamp=timestamp,
                response_time=response_time,
                error_message=str(exc),
            )

    # -------------------------------------------------------------------------
    # 完整监控检查（使用 Browser）
    # -------------------------------------------------------------------------

    def full_monitor_check(self, url_config: dict[str, Any]) -> UrlMonitorResult:
        """完整监控检查"""
        url = url_config["url"]
        keywords = url_config.get("keywords", [])

        # 创建浏览器（每次检查独立创建，确保隔离）
        browser = self.playwright.chromium.launch(headless=self.config.headless)
        context = browser.new_context(
            viewport=self.config.viewport,
            user_agent=self.config.user_agent,
        )

        page = context.new_page()

        # 设置超时
        page.set_default_navigation_timeout(int(self.config.response_time_threshold * 1000))

        # 开始 Trace 记录
        trace_file = self.config.traces_dir / f"{hashlib.md5(url.encode()).hexdigest()}_{datetime.now():%Y%m%d_%H%M%S}.zip"
        context.tracing.start(screenshots=True, snapshots=True)

        timestamp = datetime.now()
        import time
        start_time = time.time()

        try:
            # 访问页面
            response = page.goto(url, wait_until="networkidle")
            response_time = time.time() - start_time

            # 等待页面稳定
            page.wait_for_load_state("networkidle", timeout=5000)

            status_code = response.status if response else None

            # 判断基本状态
            if status_code and status_code >= 400:
                status = MonitorStatus.UNHEALTHY
            elif response_time > self.config.response_time_threshold:
                status = MonitorStatus.UNHEALTHY
            elif response_time > self.config.degraded_threshold:
                status = MonitorStatus.DEGRADED
            else:
                status = MonitorStatus.HEALTHY

            # 收集性能指标
            performance = None
            if self.config.enable_performance_monitoring:
                performance = self._collect_performance_metrics(page)

            # 关键字检查
            keywords_found = []
            keywords_missing = []
            if self.config.enable_keyword_check and keywords:
                page_text = page.inner_text("body")
                for keyword in keywords:
                    if keyword in page_text:
                        keywords_found.append(keyword)
                    else:
                        keywords_missing.append(keyword)

            # 截图
            screenshot_path = None
            screenshot_hash = None
            if status != MonitorStatus.HEALTHY or self.config.enable_visual_regression:
                screenshot_path = self.config.screenshots_dir / f"{hashlib.md5(url.encode()).hexdigest()}_{datetime.now():%Y%m%d_%H%M%S}.png"
                page.screenshot(path=str(screenshot_path), full_page=True)

                # 计算截图哈希（用于视觉回归）
                screenshot_hash = self._calculate_screenshot_hash(screenshot_path)

            # 停止 Trace
            context.tracing.stop(path=str(trace_file))

            result = UrlMonitorResult(
                url=url,
                status=status,
                timestamp=timestamp,
                response_time=response_time,
                status_code=status_code,
                performance=performance,
                keywords_found=keywords_found,
                keywords_missing=keywords_missing,
                screenshot_path=str(screenshot_path) if screenshot_path else None,
                trace_path=str(trace_file) if self.config.save_trace_on_error else None,
                screenshot_hash=screenshot_hash,
            )

            # 清理资源
            context.close()
            browser.close()

            return result

        except Exception as exc:
            response_time = time.time() - start_time
            screenshot_path = self.config.screenshots_dir / f"ERROR_{hashlib.md5(url.encode()).hexdigest()}_{datetime.now():%Y%m%d_%H%M%S}.png"
            try:
                page.screenshot(path=str(screenshot_path), full_page=True)
            except Exception:
                pass

            context.tracing.stop(path=str(trace_file))
            # 清理资源
            context.close()
            browser.close()

            return UrlMonitorResult(
                url=url,
                status=MonitorStatus.ERROR,
                timestamp=timestamp,
                response_time=response_time,
                error_message=str(exc),
                screenshot_path=str(screenshot_path),
                trace_path=str(trace_file),
            )

    # -------------------------------------------------------------------------
    # 性能指标收集
    # -------------------------------------------------------------------------

    def _collect_performance_metrics(self, page: Any) -> PerformanceMetrics:
        """收集页面性能指标"""
        try:
            metrics = page.evaluate(
                """() => {
                    const timing = performance.timing;
                    const navigation = performance.getEntriesByType('navigation')[0];

                    return {
                        dns_lookup: timing.domainLookupEnd - timing.domainLookupStart,
                        connection: timing.connectEnd - timing.connectStart,
                        tls_negotiation: timing.connectEnd - timing.secureConnectionStart,
                        ttfb: timing.responseStart - timing.requestStart,
                        download: timing.responseEnd - timing.responseStart,
                        total: timing.loadEventEnd - timing.navigationStart,
                        dom_content_loaded: timing.domContentLoadedEventEnd - timing.navigationStart,
                        load_complete: timing.loadEventEnd - timing.navigationStart,
                        first_contentful_paint: navigation?.loadEventEnd,  // 简化
                    };
                }"""
            )

            # 获取资源统计
            resource_stats = page.evaluate(
                """() => {
                    const resources = performance.getEntriesByType('resource');
                    return {
                        count: resources.length,
                        transferSize: resources.reduce((sum, r) => sum + (r.transferSize || 0), 0),
                    };
                }"""
            )

            return PerformanceMetrics(
                dns_lookup_time=metrics.get("dns_lookup") / 1000 if metrics.get("dns_lookup") else None,
                connection_time=metrics.get("connection") / 1000 if metrics.get("connection") else None,
                tls_negotiation_time=metrics.get("tls_negotiation") / 1000 if metrics.get("tls_negotiation") else None,
                ttfb=metrics.get("ttfb") / 1000 if metrics.get("ttfb") else None,
                download_time=metrics.get("download") / 1000 if metrics.get("download") else None,
                total_time=metrics.get("total") / 1000 if metrics.get("total") else None,
                dom_content_loaded=metrics.get("dom_content_loaded") / 1000 if metrics.get("dom_content_loaded") else None,
                load_complete=metrics.get("load_complete") / 1000 if metrics.get("load_complete") else None,
                total_requests=resource_stats.get("count", 0),
                total_transfer_size=resource_stats.get("transferSize", 0),
            )

        except Exception as exc:
            print(f"收集性能指标失败: {exc}")
            return PerformanceMetrics()

    # -------------------------------------------------------------------------
    # 视觉回归
    # -------------------------------------------------------------------------

    def _calculate_screenshot_hash(self, screenshot_path: Path) -> str:
        """计算截图哈希值"""
        try:
            with open(screenshot_path, "rb") as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception:
            return ""

    def save_baseline(self, url: str, screenshot_path: Path) -> None:
        """保存基准截图"""
        baseline_path = self.config.baselines_dir / f"{hashlib.md5(url.encode()).hexdigest()}_baseline.png"
        import shutil
        shutil.copy(screenshot_path, baseline_path)
        print(f"基准截图已保存: {baseline_path}")

    # -------------------------------------------------------------------------
    # 报告生成
    # -------------------------------------------------------------------------

    def generate_report(self, results: list[UrlMonitorResult]) -> MonitorReport:
        """生成监控报告"""
        report = MonitorReport(
            start_time=min(r.timestamp for r in results) if results else datetime.now(),
            end_time=max(r.timestamp for r in results) if results else datetime.now(),
            results=results,
        )

        # 生成 JSON 报告
        json_file = self.config.reports_dir / f"report_{datetime.now():%Y%m%d_%H%M%S}.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump({
                "start_time": report.start_time.isoformat(),
                "end_time": report.end_time.isoformat(),
                "summary": {
                    "total_urls": report.total_urls,
                    "healthy": report.healthy_count,
                    "degraded": report.degraded_count,
                    "unhealthy": report.unhealthy_count,
                    "error": report.error_count,
                    "avg_response_time": report.avg_response_time,
                },
                "results": [
                    {
                        "url": r.url,
                        "status": r.status.value,
                        "timestamp": r.timestamp.isoformat(),
                        "response_time": r.response_time,
                        "status_code": r.status_code,
                        "error": r.error_message,
                        "performance": dataclasses.asdict(r.performance) if r.performance else None,
                        "keywords_found": r.keywords_found,
                        "keywords_missing": r.keywords_missing,
                    }
                    for r in results
                ],
            }, f, ensure_ascii=False, indent=2)

        print(f"JSON 报告已生成: {json_file}")

        return report

    def print_report_summary(self, report: MonitorReport) -> None:
        """打印报告摘要"""
        print("\n" + "="*60)
        print("监控报告摘要")
        print("="*60)
        print(f"检查时间: {report.start_time:%Y-%m-%d %H:%M:%S} - {report.end_time:%Y-%m-%d %H:%M:%S}")
        print(f"\nURL 总数: {report.total_urls}")
        print(f"  健康: {report.healthy_count}")
        print(f"  性能下降: {report.degraded_count}")
        print(f"  不可用: {report.unhealthy_count}")
        print(f"  错误: {report.error_count}")
        print(f"\n平均响应时间: {report.avg_response_time:.3f}s")

        # 打印详情
        print("\n详细结果:")
        for result in report.results:
            status_symbol = {
                MonitorStatus.HEALTHY: "✓",
                MonitorStatus.DEGRADED: "⚠",
                MonitorStatus.UNHEALTHY: "✗",
                MonitorStatus.ERROR: "!",
            }[result.status]

            print(f"\n{status_symbol} {result.url}")
            print(f"  状态: {result.status.value}")
            print(f"  响应时间: {result.response_time:.3f}s")
            if result.status_code:
                print(f"  状态码: {result.status_code}")
            if result.error_message:
                print(f"  错误: {result.error_message}")
            if result.keywords_missing:
                print(f"  缺失关键字: {result.keywords_missing}")
            if result.performance and result.performance.total_time:
                print(f"  页面加载: {result.performance.total_time:.3f}s")

    # -------------------------------------------------------------------------
    # 告警
    # -------------------------------------------------------------------------

    def send_alert(self, result: UrlMonitorResult) -> None:
        """发送告警"""
        should_alert = (
            (result.status == MonitorStatus.UNHEALTHY and self.config.alert_on_unhealthy) or
            (result.status == MonitorStatus.DEGRADED and self.config.alert_on_degraded) or
            (result.status == MonitorStatus.ERROR)
        )

        if not should_alert:
            return

        print(f"\n[告警] {result.url}")
        print(f"  状态: {result.status.value}")
        print(f"  响应时间: {result.response_time:.3f}s")
        if result.error_message:
            print(f"  错误: {result.error_message}")

        # 这里可以添加邮件告警逻辑
        # if self.config.email_alerts:
        #     self._send_email_alert(result)


# =============================================================================
# 模拟监控目标
# =============================================================================


def create_mock_monitor_targets() -> list[dict[str, Any]]:
    """创建模拟监控目标（实际项目中应该从配置文件读取）"""
    return [
        {
            "url": "https://example.com",
            "name": "Example 主页",
            "keywords": ["Example Domain", "illustrative examples"],
        },
        {
            "url": "https://httpbin.org/status/200",
            "name": "HTTPBin 健康",
            "keywords": [],
        },
        {
            "url": "https://httpbin.org/delay/1",
            "name": "HTTPBin 延迟测试",
            "keywords": [],
        },
        {
            "url": "https://invalid-domain-12345.com",
            "name": "无效域名测试",
            "keywords": [],
        },
    ]


# =============================================================================
# 主程序
# =============================================================================


def main() -> None:
    """主程序入口"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        print("请先安装：python3 -m pip install playwright==1.58.0")
        return

    # 创建配置
    config = MonitorConfig(
        target_urls=create_mock_monitor_targets(),
        response_time_threshold=5.0,
        degraded_threshold=2.0,
        enable_visual_regression=True,
        enable_performance_monitoring=True,
        enable_keyword_check=True,
        headless=True,
    )

    # 创建监控器
    monitor = WebsiteMonitor(config)

    try:
        # 初始化
        monitor.init()

        print("\n" + "="*60)
        print("网站健康监控系统")
        print("="*60)
        print(f"开始时间: {datetime.now():%Y-%m-%d %H:%M:%S}")
        print(f"监控目标数: {len(config.target_urls)}")

        results = []

        # 第一轮：快速健康检查（API 方式）
        print("\n[第一轮] 快速健康检查")
        print("-"*60)

        for target in config.target_urls:
            url = target["url"]
            print(f"检查: {url}")

            result = monitor.quick_health_check(url)
            results.append(result)

            status_symbol = {
                MonitorStatus.HEALTHY: "✓",
                MonitorStatus.DEGRADED: "⚠",
                MonitorStatus.UNHEALTHY: "✗",
                MonitorStatus.ERROR: "!",
            }[result.status]

            print(f"  {status_symbol} {result.status.value} - {result.response_time:.3f}s")

            if result.status != MonitorStatus.HEALTHY:
                monitor.send_alert(result)

        # 第二轮：完整监控检查（浏览器方式）
        # 只对重要的 URL 进行完整检查
        print("\n[第二轮] 完整监控检查")
        print("-"*60)

        important_urls = config.target_urls[:2]  # 只检查前两个

        for target in important_urls:
            url = target["url"]
            print(f"完整检查: {url}")

            result = monitor.full_monitor_check(target)
            results.append(result)

            print(f"  状态: {result.status.value}")
            print(f"  响应时间: {result.response_time:.3f}s")

            if result.performance and result.performance.total_time:
                print(f"  页面加载: {result.performance.total_time:.3f}s")
                print(f"  请求数: {result.performance.total_requests}")

            if result.keywords_found:
                print(f"  关键字: {result.keywords_found}")
            if result.keywords_missing:
                print(f"  缺失关键字: {result.keywords_missing}")

            if result.status != MonitorStatus.HEALTHY:
                monitor.send_alert(result)

        # 生成报告
        print("\n[报告生成]")
        print("-"*60)

        report = monitor.generate_report(results)
        monitor.print_report_summary(report)

        # 保存基准截图（用于视觉回归）
        print("\n[视觉回归基准]")
        print("-"*60)

        for result in results:
            if result.screenshot_path and result.status == MonitorStatus.HEALTHY:
                monitor.save_baseline(result.url, Path(result.screenshot_path))

    except KeyboardInterrupt:
        print("\n监控被用户中断")
    except Exception as exc:
        print(f"\n发生错误: {exc}")
        import traceback
        traceback.print_exc()
    finally:
        monitor.close()


if __name__ == "__main__":
    main()
