#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 48：真实场景 - Web 自动化测试套件（完整项目级示例）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/48_real_test_suite.py

本示例演示一个完整的 Web 自动化测试框架，包含以下功能：

## 业务场景
1. 用户注册/登录流程测试
2. 表单验证测试
3. 文件上传测试
4. 弹窗处理测试
5. 多浏览器兼容性测试
6. 移动端设备模拟测试
7. 测试报告生成
8. 失败截图和 Trace 记录
9. 数据驱动测试

## 涉及的 Playwright API
- browser.new_context: 创建隔离测试环境
- expect: 各种断言方法
- set_input_files: 文件上传
- expect_dialog: 处理弹窗
- tracing.start/stop: 记录测试 trace
- devices: 模拟移动设备
- locator: 元素定位和操作
- wait_for: 等待条件
- screenshot: 失败截图
- evaluate: 执行 JavaScript
"""

from __future__ import annotations

import dataclasses
import json
import traceback
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Callable

# =============================================================================
# 测试结果模型
# =============================================================================


class TestStatus(Enum):
    """测试状态枚举"""
    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"
    ERROR = "error"


@dataclass
class TestResult:
    """单个测试结果"""
    name: str
    status: TestStatus
    duration: float  # 执行时长（秒）
    error_message: str | None = None
    screenshot_path: str | None = None
    trace_path: str | None = None


@dataclass
class TestSuiteResult:
    """测试套件结果"""
    suite_name: str
    start_time: datetime
    end_time: datetime | None = None
    results: list[TestResult] = field(default_factory=list)
    total: int = 0
    passed: int = 0
    failed: int = 0
    skipped: int = 0
    errors: int = 0

    @property
    def duration(self) -> float:
        """总执行时长"""
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0

    def add_result(self, result: TestResult) -> None:
        """添加测试结果"""
        self.results.append(result)
        self.total += 1
        if result.status == TestStatus.PASSED:
            self.passed += 1
        elif result.status == TestStatus.FAILED:
            self.failed += 1
        elif result.status == TestStatus.SKIPPED:
            self.skipped += 1
        elif result.status == TestStatus.ERROR:
            self.errors += 1


@dataclass
class TestCase:
    """测试用例"""
    name: str
    test_func: Callable[[Any], None]
    description: str = ""
    enabled: bool = True
    tags: list[str] = field(default_factory=list)


# =============================================================================
# 模拟待测试网站
# =============================================================================


def create_test_website_html() -> str:
    """创建模拟的测试网站 HTML"""
    return """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>测试网站 - 用户注册登录</title>
        <style>
            * { box-sizing: border-box; }
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input[type="text"], input[type="email"], input[type="password"], select, textarea {
                width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px;
            }
            input.error, select.error { border-color: red; }
            .error-message { color: red; font-size: 14px; margin-top: 5px; display: none; }
            .error-message.visible { display: block; }
            button {
                padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;
            }
            button:hover { background: #0056b3; }
            button:disabled { background: #ccc; cursor: not-allowed; }
            .success-message { color: green; display: none; }
            .success-message.visible { display: block; }
            .tabs { display: flex; border-bottom: 1px solid #ddd; margin-bottom: 20px; }
            .tab { padding: 10px 20px; cursor: pointer; }
            .tab.active { border-bottom: 2px solid #007bff; color: #007bff; }
            .tab-content { display: none; }
            .tab-content.active { display: block; }
            #uploaded-file-info { margin-top: 10px; padding: 10px; background: #f0f0f0; display: none; }
            #uploaded-file-info.visible { display: block; }
        </style>
    </head>
    <body>
        <h1>用户注册登录系统</h1>

        <div class="tabs">
            <div class="tab active" data-tab="register">注册</div>
            <div class="tab" data-tab="login">登录</div>
            <div class="tab" data-tab="upload">文件上传</div>
        </div>

        <!-- 注册表单 -->
        <div id="register-tab" class="tab-content active">
            <h2>用户注册</h2>
            <form id="register-form">
                <div class="form-group">
                    <label for="reg-username">用户名 *</label>
                    <input type="text" id="reg-username" name="username" required>
                    <div class="error-message" id="username-error"></div>
                </div>
                <div class="form-group">
                    <label for="reg-email">邮箱 *</label>
                    <input type="email" id="reg-email" name="email" required>
                    <div class="error-message" id="email-error"></div>
                </div>
                <div class="form-group">
                    <label for="reg-password">密码 *</label>
                    <input type="password" id="reg-password" name="password" required>
                    <div class="error-message" id="password-error"></div>
                </div>
                <div class="form-group">
                    <label for="reg-confirm-password">确认密码 *</label>
                    <input type="password" id="reg-confirm-password" name="confirmPassword" required>
                    <div class="error-message" id="confirm-password-error"></div>
                </div>
                <div class="form-group">
                    <label for="reg-country">国家/地区</label>
                    <select id="reg-country" name="country">
                        <option value="">请选择</option>
                        <option value="CN">中国</option>
                        <option value="US">美国</option>
                        <option value="JP">日本</option>
                    </select>
                </div>
                <button type="submit" id="register-btn">注册</button>
            </form>
            <div class="success-message" id="register-success">注册成功！</div>
        </div>

        <!-- 登录表单 -->
        <div id="login-tab" class="tab-content">
            <h2>用户登录</h2>
            <form id="login-form">
                <div class="form-group">
                    <label for="login-username">用户名/邮箱 *</label>
                    <input type="text" id="login-username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="login-password">密码 *</label>
                    <input type="password" id="login-password" name="password" required>
                </div>
                <div class="form-group">
                    <label>
                        <input type="checkbox" id="remember-me" name="rememberMe">
                        记住我
                    </label>
                </div>
                <button type="submit" id="login-btn">登录</button>
            </form>
            <div class="success-message" id="login-success">登录成功！</div>
        </div>

        <!-- 文件上传 -->
        <div id="upload-tab" class="tab-content">
            <h2>文件上传测试</h2>
            <form id="upload-form">
                <div class="form-group">
                    <label for="file-upload">选择文件</label>
                    <input type="file" id="file-upload" name="file" accept=".txt,.pdf,.jpg,.png">
                </div>
                <button type="submit" id="upload-btn">上传</button>
            </form>
            <div id="uploaded-file-info"></div>
        </div>

        <script>
            // Tab 切换
            document.querySelectorAll('.tab').forEach(tab => {
                tab.addEventListener('click', function() {
                    const targetTab = this.dataset.tab;
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                    this.classList.add('active');
                    document.getElementById(targetTab + '-tab').classList.add('active');
                });
            });

            // 注册表单验证
            document.getElementById('register-form').addEventListener('submit', function(e) {
                e.preventDefault();
                let valid = true;

                // 用户名验证
                const username = document.getElementById('reg-username');
                const usernameError = document.getElementById('username-error');
                if (username.value.length < 3) {
                    username.classList.add('error');
                    usernameError.textContent = '用户名至少3个字符';
                    usernameError.classList.add('visible');
                    valid = false;
                } else {
                    username.classList.remove('error');
                    usernameError.classList.remove('visible');
                }

                // 邮箱验证
                const email = document.getElementById('reg-email');
                const emailError = document.getElementById('email-error');
                const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
                if (!emailRegex.test(email.value)) {
                    email.classList.add('error');
                    emailError.textContent = '请输入有效的邮箱地址';
                    emailError.classList.add('visible');
                    valid = false;
                } else {
                    email.classList.remove('error');
                    emailError.classList.remove('visible');
                }

                // 密码验证
                const password = document.getElementById('reg-password');
                const passwordError = document.getElementById('password-error');
                if (password.value.length < 6) {
                    password.classList.add('error');
                    passwordError.textContent = '密码至少6个字符';
                    passwordError.classList.add('visible');
                    valid = false;
                } else {
                    password.classList.remove('error');
                    passwordError.classList.remove('visible');
                }

                // 确认密码验证
                const confirmPassword = document.getElementById('reg-confirm-password');
                const confirmError = document.getElementById('confirm-password-error');
                if (confirmPassword.value !== password.value) {
                    confirmPassword.classList.add('error');
                    confirmError.textContent = '两次密码不一致';
                    confirmError.classList.add('visible');
                    valid = false;
                } else {
                    confirmPassword.classList.remove('error');
                    confirmError.classList.remove('visible');
                }

                if (valid) {
                    document.getElementById('register-success').classList.add('visible');
                    setTimeout(() => {
                        document.getElementById('register-success').classList.remove('visible');
                        document.getElementById('register-form').reset();
                    }, 2000);
                }
            });

            // 登录表单
            document.getElementById('login-form').addEventListener('submit', function(e) {
                e.preventDefault();
                const username = document.getElementById('login-username').value;
                const password = document.getElementById('login-password').value;
                if (username && password) {
                    document.getElementById('login-success').classList.add('visible');
                }
            });

            // 文件上传
            document.getElementById('upload-form').addEventListener('submit', function(e) {
                e.preventDefault();
                const fileInput = document.getElementById('file-upload');
                if (fileInput.files.length > 0) {
                    const file = fileInput.files[0];
                    document.getElementById('uploaded-file-info').innerHTML =
                        '已上传: ' + file.name + ' (' + (file.size / 1024).toFixed(2) + ' KB)';
                    document.getElementById('uploaded-file-info').classList.add('visible');
                }
            });
        </script>
    </body>
    </html>
    """


# =============================================================================
# 测试框架核心类
# =============================================================================


class WebTestRunner:
    """Web 自动化测试运行器"""

    def __init__(
        self,
        headless: bool = True,
        screenshots_dir: Path | None = None,
        traces_dir: Path | None = None,
        reports_dir: Path | None = None,
    ):
        # 使用脚本所在目录下的 test_output 子目录
        demo_root = Path(__file__).parent / "test_output"

        self.headless = headless
        self.screenshots_dir = screenshots_dir or demo_root / "screenshots"
        self.traces_dir = traces_dir or demo_root / "traces"
        self.reports_dir = reports_dir or demo_root / "reports"

        # 创建目录
        for dir_path in [self.screenshots_dir, self.traces_dir, self.reports_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

        # 测试结果
        self.suite_results: list[TestSuiteResult] = []
        self.playwright: Any = None
        self.browser: Any = None
        self.context: Any = None
        self.page: Any = None

        # 当前测试信息
        self.current_test_name: str | None = None
        self.current_trace_file: Path | None = None

    # -------------------------------------------------------------------------
    # 浏览器管理
    # -------------------------------------------------------------------------

    def setup_browser(self, browser_type: str = "chromium", device: str | None = None) -> None:
        """设置浏览器"""
        from playwright.sync_api import sync_playwright

        if self.playwright is None:
            self.playwright = sync_playwright().start()

        # 获取浏览器类型
        browser_class = getattr(self.playwright, browser_type)

        # 启动浏览器
        self.browser = browser_class.launch(headless=self.headless)

        # 创建上下文
        context_args = {}
        if device:
            # 使用预设设备配置
            devices = self.playwright.devices
            if device in devices:
                context_args = devices[device]

        self.context = self.browser.new_context(**context_args)

        # 创建页面
        self.page = self.context.new_page()

        # 设置默认超时
        self.page.set_default_timeout(10000)

    def teardown_browser(self) -> None:
        """关闭浏览器"""
        if self.context:
            self.context.close()
            self.context = None
        if self.browser:
            self.browser.close()
            self.browser = None
        if self.playwright:
            self.playwright.stop()
            self.playwright = None

    # -------------------------------------------------------------------------
    # 测试执行
    # -------------------------------------------------------------------------

    def run_test_suite(self, suite_name: str, test_cases: list[TestCase]) -> TestSuiteResult:
        """运行测试套件"""
        suite_result = TestSuiteResult(
            suite_name=suite_name,
            start_time=datetime.now(),
        )

        print(f"\n{'='*60}")
        print(f"测试套件: {suite_name}")
        print(f"{'='*60}")

        for test_case in test_cases:
            if not test_case.enabled:
                result = TestResult(
                    name=test_case.name,
                    status=TestStatus.SKIPPED,
                    duration=0.0,
                )
                suite_result.add_result(result)
                print(f"  [SKIP] {test_case.name}")
                continue

            # 运行单个测试
            result = self.run_single_test(test_case)
            suite_result.add_result(result)

            # 打印结果
            status_symbol = {
                TestStatus.PASSED: "[PASS]",
                TestStatus.FAILED: "[FAIL]",
                TestStatus.ERROR: "[ERROR]",
            }.get(result.status, "[???]")
            print(f"  {status_symbol} {test_case.name} ({result.duration:.2f}s)")

            if result.error_message:
                print(f"        错误: {result.error_message}")

        suite_result.end_time = datetime.now()
        self.suite_results.append(suite_result)

        # 打印套件汇总
        print(f"\n套件汇总: {suite_result.passed}/{suite_result.total} 通过")
        if suite_result.failed > 0:
            print(f"  失败: {suite_result.failed}")
        if suite_result.errors > 0:
            print(f"  错误: {suite_result.errors}")

        return suite_result

    def run_single_test(self, test_case: TestCase) -> TestResult:
        """运行单个测试用例"""
        import time

        self.current_test_name = test_case.name
        start_time = time.time()

        # 开始 Trace 记录
        self.current_trace_file = self.traces_dir / f"{test_case.name}_{datetime.now():%Y%m%d_%H%M%S}.zip"
        self.context.tracing.start(screenshots=True, snapshots=True)

        try:
            # 执行测试
            test_case.test_func(self)

            duration = time.time() - start_time
            return TestResult(
                name=test_case.name,
                status=TestStatus.PASSED,
                duration=duration,
            )

        except AssertionError as exc:
            duration = time.time() - start_time
            screenshot_path = self._take_failure_screenshot(test_case.name)

            return TestResult(
                name=test_case.name,
                status=TestStatus.FAILED,
                duration=duration,
                error_message=str(exc),
                screenshot_path=str(screenshot_path) if screenshot_path else None,
                trace_path=str(self.current_trace_file) if self.current_trace_file else None,
            )

        except Exception as exc:
            duration = time.time() - start_time
            screenshot_path = self._take_failure_screenshot(test_case.name)

            return TestResult(
                name=test_case.name,
                status=TestStatus.ERROR,
                duration=duration,
                error_message=f"{type(exc).__name__}: {exc}",
                screenshot_path=str(screenshot_path) if screenshot_path else None,
                trace_path=str(self.current_trace_file) if self.current_trace_file else None,
            )

        finally:
            # 停止 Trace 记录
            self.context.tracing.stop(path=str(self.current_trace_file))

    def _take_failure_screenshot(self, test_name: str) -> Path | None:
        """测试失败时截图"""
        try:
            screenshot_path = self.screenshots_dir / f"FAIL_{test_name}_{datetime.now():%Y%m%d_%H%M%S}.png"
            self.page.screenshot(path=str(screenshot_path), full_page=True)
            return screenshot_path
        except Exception:
            return None

    # -------------------------------------------------------------------------
    # 断言方法
    # -------------------------------------------------------------------------

    def assert_equal(self, actual: Any, expected: Any, message: str = "") -> None:
        """断言相等"""
        if actual != expected:
            raise AssertionError(f"{message}\nExpected: {expected}\nActual: {actual}")

    def assert_true(self, condition: bool, message: str = "") -> None:
        """断言为真"""
        if not condition:
            raise AssertionError(f"{message}\nExpected: True\nActual: False")

    def assert_false(self, condition: bool, message: str = "") -> None:
        """断言为假"""
        if condition:
            raise AssertionError(f"{message}\nExpected: False\nActual: True")

    def assert_contains(self, text: str, substring: str, message: str = "") -> None:
        """断言包含子串"""
        if substring not in text:
            raise AssertionError(f"{message}\nExpected '{text}' to contain '{substring}'")

    def assert_visible(self, selector: str, message: str = "") -> None:
        """断言元素可见"""
        locator = self.page.locator(selector)
        if not locator.is_visible():
            raise AssertionError(f"{message}\nElement '{selector}' is not visible")

    def assert_hidden(self, selector: str, message: str = "") -> None:
        """断言元素隐藏"""
        locator = self.page.locator(selector)
        if not locator.is_hidden():
            raise AssertionError(f"{message}\nElement '{selector}' is visible")

    def assert_has_class(self, selector: str, class_name: str, message: str = "") -> None:
        """断言元素包含指定 class"""
        elem = self.page.locator(selector)
        classes = elem.get_attribute("class") or ""
        if class_name not in classes.split():
            raise AssertionError(f"{message}\nElement '{selector}' does not have class '{class_name}'")

    def assert_element_count(self, selector: str, count: int, message: str = "") -> None:
        """断言元素数量"""
        actual_count = self.page.locator(selector).count()
        if actual_count != count:
            raise AssertionError(f"{message}\nExpected {count} elements, found {actual_count}")

    # -------------------------------------------------------------------------
    # 报告生成
    # -------------------------------------------------------------------------

    def generate_html_report(self, output_file: Path | None = None) -> None:
        """生成 HTML 测试报告"""
        if output_file is None:
            output_file = self.reports_dir / f"report_{datetime.now():%Y%m%d_%H%M%S}.html"

        html_content = self._generate_html_report_content()

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"\nHTML 报告已生成: {output_file}")

    def _generate_html_report_content(self) -> str:
        """生成 HTML 报告内容"""
        total_suites = len(self.suite_results)
        total_tests = sum(r.total for r in self.suite_results)
        total_passed = sum(r.passed for r in self.suite_results)
        total_failed = sum(r.failed for r in self.suite_results)
        total_errors = sum(r.errors for r in self.suite_results)

        pass_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0

        # 生成测试结果行
        test_rows = ""
        for suite in self.suite_results:
            for result in suite.results:
                status_class = result.status.value
                status_badge = {
                    TestStatus.PASSED: "✓ 通过",
                    TestStatus.FAILED: "✗ 失败",
                    TestStatus.SKIPPED: "- 跳过",
                    TestStatus.ERROR: "! 错误",
                }[result.status]

                test_rows += f"""
                <tr class="{status_class}">
                    <td>{suite.suite_name}</td>
                    <td>{result.name}</td>
                    <td><span class="badge badge-{status_class}">{status_badge}</span></td>
                    <td>{result.duration:.3f}s</td>
                    <td>{result.error_message or '-'}</td>
                    <td>{result.screenshot_path or '-'}</td>
                </tr>
                """

        return f"""
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <title>测试报告 - {datetime.now():%Y-%m-%d %H:%M:%S}</title>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; background: #f5f5f5; padding: 20px; }}
                .container {{ max-width: 1200px; margin: 0 auto; background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
                .header {{ padding: 20px; border-bottom: 1px solid #eee; }}
                .header h1 {{ font-size: 24px; color: #333; }}
                .header .timestamp {{ color: #999; font-size: 14px; margin-top: 5px; }}
                .summary {{ padding: 20px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; }}
                .summary-card {{ background: #f9f9f9; padding: 15px; border-radius: 6px; text-align: center; }}
                .summary-card .number {{ font-size: 32px; font-weight: bold; }}
                .summary-card.passed .number {{ color: #28a745; }}
                .summary-card.failed .number {{ color: #dc3545; }}
                .summary-card.error .number {{ color: #fd7e14; }}
                .summary-card.skipped .number {{ color: #6c757d; }}
                .summary-card .label {{ color: #666; font-size: 14px; margin-top: 5px; }}
                .progress-bar {{ height: 8px; background: #e9ecef; border-radius: 4px; overflow: hidden; margin: 20px; }}
                .progress-fill {{ height: 100%; background: #28a745; transition: width 0.3s; }}
                .table-container {{ overflow-x: auto; }}
                table {{ width: 100%; border-collapse: collapse; }}
                th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #eee; }}
                th {{ background: #f8f9fa; font-weight: 600; color: #495057; }}
                tr.passed {{ background: #d4edda; }}
                tr.failed {{ background: #f8d7da; }}
                tr.error {{ background: #fff3cd; }}
                tr.skipped {{ background: #e2e3e5; }}
                .badge {{ display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }}
                .badge-passed {{ background: #28a745; color: white; }}
                .badge-failed {{ background: #dc3545; color: white; }}
                .badge-error {{ background: #fd7e14; color: white; }}
                .badge-skipped {{ background: #6c757d; color: white; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Web 自动化测试报告</h1>
                    <div class="timestamp">生成时间: {datetime.now():%Y-%m-%d %H:%M:%S}</div>
                </div>

                <div class="summary">
                    <div class="summary-card passed">
                        <div class="number">{total_passed}</div>
                        <div class="label">通过 ({pass_rate:.1f}%)</div>
                    </div>
                    <div class="summary-card failed">
                        <div class="number">{total_failed}</div>
                        <div class="label">失败</div>
                    </div>
                    <div class="summary-card error">
                        <div class="number">{total_errors}</div>
                        <div class="label">错误</div>
                    </div>
                    <div class="summary-card skipped">
                        <div class="number">{total_skipped}</div>
                        <div class="label">跳过</div>
                    </div>
                </div>

                <div class="progress-bar">
                    <div class="progress-fill" style="width: {pass_rate}%"></div>
                </div>

                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>测试套件</th>
                                <th>测试用例</th>
                                <th>状态</th>
                                <th>耗时</th>
                                <th>错误信息</th>
                                <th>截图</th>
                            </tr>
                        </thead>
                        <tbody>
                            {test_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </body>
        </html>
        """

    def generate_json_report(self, output_file: Path | None = None) -> None:
        """生成 JSON 测试报告"""
        if output_file is None:
            output_file = self.reports_dir / f"report_{datetime.now():%Y%m%d_%H%M%S}.json"

        report_data = {
            "generated_at": datetime.now().isoformat(),
            "summary": {
                "total_suites": len(self.suite_results),
                "total_tests": sum(r.total for r in self.suite_results),
                "total_passed": sum(r.passed for r in self.suite_results),
                "total_failed": sum(r.failed for r in self.suite_results),
                "total_errors": sum(r.errors for r in self.suite_results),
                "total_skipped": sum(r.skipped for r in self.suite_results),
            },
            "suites": [
                {
                    "name": suite.suite_name,
                    "start_time": suite.start_time.isoformat(),
                    "end_time": suite.end_time.isoformat() if suite.end_time else None,
                    "duration": suite.duration,
                    "total": suite.total,
                    "passed": suite.passed,
                    "failed": suite.failed,
                    "errors": suite.errors,
                    "skipped": suite.skipped,
                    "tests": [
                        {
                            "name": result.name,
                            "status": result.status.value,
                            "duration": result.duration,
                            "error_message": result.error_message,
                            "screenshot_path": result.screenshot_path,
                            "trace_path": result.trace_path,
                        }
                        for result in suite.results
                    ],
                }
                for suite in self.suite_results
            ],
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)

        print(f"JSON 报告已生成: {output_file}")


# =============================================================================
# 测试用例定义
# =============================================================================


class UserAuthTests:
    """用户认证测试"""

    @staticmethod
    def test_valid_login(runner: WebTestRunner) -> None:
        """测试有效登录"""
        # 切换到登录 tab
        runner.page.click(".tab[data-tab='login']")
        runner.page.wait_for_selector("#login-tab", state="visible")

        # 填写登录表单
        runner.page.fill("#login-username", "test@example.com")
        runner.page.fill("#login-password", "password123")
        runner.page.check("#remember-me")

        # 提交表单
        runner.page.click("#login-btn")

        # 验证登录成功消息
        success_elem = runner.page.locator("#login-success")
        success_elem.wait_for(state="visible", timeout=5000)
        runner.assert_true(success_elem.is_visible(), "登录成功消息应该显示")

    @staticmethod
    def test_login_empty_fields(runner: WebTestRunner) -> None:
        """测试空字段登录"""
        runner.page.click(".tab[data-tab='login']")

        # 不填写任何字段，直接提交
        runner.page.click("#login-btn")

        # HTML5 required 验证会阻止提交
        # 检查输入框的 validity
        is_valid = runner.page.evaluate(
            """() => {
                const username = document.getElementById('login-username');
                return username.validity.valid;
            }"""
        )
        runner.assert_false(is_valid, "空用户名应该验证失败")

    @staticmethod
    def test_valid_registration(runner: WebTestRunner) -> None:
        """测试有效注册"""
        # 切换到注册 tab
        runner.page.click(".tab[data-tab='register']")
        runner.page.wait_for_selector("#register-tab", state="visible")

        # 填写注册表单
        runner.page.fill("#reg-username", "testuser123")
        runner.page.fill("#reg-email", "test@example.com")
        runner.page.fill("#reg-password", "password123")
        runner.page.fill("#reg-confirm-password", "password123")
        runner.page.select_option("#reg-country", "CN")

        # 提交表单
        runner.page.click("#register-btn")

        # 验证成功消息
        success_elem = runner.page.locator("#register-success")
        success_elem.wait_for(state="visible", timeout=5000)
        runner.assert_true(success_elem.is_visible(), "注册成功消息应该显示")

    @staticmethod
    def test_registration_username_too_short(runner: WebTestRunner) -> None:
        """测试用户名过短"""
        runner.page.click(".tab[data-tab='register']")

        # 输入过短的用户名
        runner.page.fill("#reg-username", "ab")
        runner.page.fill("#reg-email", "test@example.com")
        runner.page.fill("#reg-password", "password123")
        runner.page.fill("#reg-confirm-password", "password123")

        runner.page.click("#register-btn")

        # 验证错误消息
        error_elem = runner.page.locator("#username-error")
        runner.assert_true(error_elem.is_visible(), "用户名错误消息应该显示")
        runner.assert_contains(error_elem.inner_text(), "至少3个字符", "应该显示最小长度错误")

    @staticmethod
    def test_registration_invalid_email(runner: WebTestRunner) -> None:
        """测试无效邮箱"""
        runner.page.click(".tab[data-tab='register']")

        # 输入无效邮箱
        runner.page.fill("#reg-username", "testuser")
        runner.page.fill("#reg-email", "invalid-email")
        runner.page.fill("#reg-password", "password123")
        runner.page.fill("#reg-confirm-password", "password123")

        runner.page.click("#register-btn")

        # 验证错误消息
        error_elem = runner.page.locator("#email-error")
        runner.assert_true(error_elem.is_visible(), "邮箱错误消息应该显示")

    @staticmethod
    def test_registration_password_mismatch(runner: WebTestRunner) -> None:
        """测试密码不匹配"""
        runner.page.click(".tab[data-tab='register']")

        runner.page.fill("#reg-username", "testuser")
        runner.page.fill("#reg-email", "test@example.com")
        runner.page.fill("#reg-password", "password123")
        runner.page.fill("#reg-confirm-password", "different123")

        runner.page.click("#register-btn")

        # 验证错误消息
        error_elem = runner.page.locator("#confirm-password-error")
        runner.assert_true(error_elem.is_visible(), "确认密码错误消息应该显示")
        runner.assert_contains(error_elem.inner_text(), "不一致", "应该显示密码不一致错误")


class FileUploadTests:
    """文件上传测试"""

    @staticmethod
    def test_file_upload(runner: WebTestRunner) -> None:
        """测试文件上传"""
        # 切换到上传 tab
        runner.page.click(".tab[data-tab='upload']")
        runner.page.wait_for_selector("#upload-tab", state="visible")

        # 创建临时文件
        import tempfile
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("Test file content for upload")
            temp_file = f.name

        try:
            # 上传文件
            runner.page.set_input_files("#file-upload", temp_file)
            runner.page.click("#upload-btn")

            # 验证上传结果
            info_elem = runner.page.locator("#uploaded-file-info")
            info_elem.wait_for(state="visible", timeout=5000)
            runner.assert_true(info_elem.is_visible(), "上传信息应该显示")
            runner.assert_contains(info_elem.inner_text(), "已上传", "应该显示已上传消息")

        finally:
            import os
            os.unlink(temp_file)


class TabSwitchTests:
    """Tab 切换测试"""

    @staticmethod
    def test_tab_switching(runner: WebTestRunner) -> None:
        """测试 Tab 切换功能"""
        # 默认应该是注册 tab
        runner.assert_has_class(".tab[data-tab='register']", "active", "注册 tab 应该默认激活")
        runner.assert_visible("#register-tab", "注册内容应该可见")

        # 点击登录 tab
        runner.page.click(".tab[data-tab='login']")
        runner.assert_has_class(".tab[data-tab='login']", "active", "登录 tab 应该激活")
        runner.assert_visible("#login-tab", "登录内容应该可见")
        runner.assert_hidden("#register-tab", "注册内容应该隐藏")

        # 点击上传 tab
        runner.page.click(".tab[data-tab='upload']")
        runner.assert_has_class(".tab[data-tab='upload']", "active", "上传 tab 应该激活")
        runner.assert_visible("#upload-tab", "上传内容应该可见")
        runner.assert_hidden("#login-tab", "登录内容应该隐藏")


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

    # 创建测试运行器
    runner = WebTestRunner(headless=True)

    # 加载测试网站
    test_html = create_test_website_html()

    try:
        # 桌面版 Chrome 测试
        print("\n" + "="*60)
        print("桌面版 Chrome 测试")
        print("="*60)

        runner.setup_browser(browser_type="chromium")
        runner.page.set_content(test_html)

        # 定义测试用例
        auth_tests = [
            TestCase("有效登录", UserAuthTests.test_valid_login),
            TestCase("空字段登录", UserAuthTests.test_login_empty_fields),
            TestCase("有效注册", UserAuthTests.test_valid_registration),
            TestCase("用户名过短", UserAuthTests.test_registration_username_too_short),
            TestCase("无效邮箱", UserAuthTests.test_registration_invalid_email),
            TestCase("密码不匹配", UserAuthTests.test_registration_password_mismatch),
        ]

        upload_tests = [
            TestCase("文件上传", FileUploadTests.test_file_upload),
        ]

        tab_tests = [
            TestCase("Tab 切换", TabSwitchTests.test_tab_switching),
        ]

        # 运行测试套件
        runner.run_test_suite("用户认证测试", auth_tests)
        runner.teardown_browser()

        runner.setup_browser(browser_type="chromium")
        runner.page.set_content(test_html)
        runner.run_test_suite("文件上传测试", upload_tests)
        runner.teardown_browser()

        runner.setup_browser(browser_type="chromium")
        runner.page.set_content(test_html)
        runner.run_test_suite("Tab 切换测试", tab_tests)
        runner.teardown_browser()

        # 移动端测试
        print("\n" + "="*60)
        print("移动端测试 (iPhone 13)")
        print("="*60)

        runner.setup_browser(browser_type="chromium", device="iPhone 13")
        runner.page.set_content(test_html)

        # 移动端只运行关键测试
        mobile_tests = [
            TestCase("移动端-有效登录", UserAuthTests.test_valid_login),
            TestCase("移动端-有效注册", UserAuthTests.test_valid_registration),
        ]

        runner.run_test_suite("移动端测试", mobile_tests)
        runner.teardown_browser()

        # 多浏览器测试
        print("\n" + "="*60)
        print("跨浏览器测试")
        print("="*60)

        for browser_type in ["chromium"]:  # 可以添加 "firefox", "webkit"
            runner.setup_browser(browser_type=browser_type)
            runner.page.set_content(test_html)
            runner.run_test_suite(
                f"{browser_type.capitalize()} 浏览器测试",
                [TestCase("登录测试", UserAuthTests.test_valid_login)]
            )
            runner.teardown_browser()

        # 生成报告
        print("\n" + "="*60)
        print("生成测试报告")
        print("="*60)

        runner.generate_html_report()
        runner.generate_json_report()

        # 打印最终汇总
        print("\n" + "="*60)
        print("最终测试汇总")
        print("="*60)

        total_tests = sum(r.total for r in runner.suite_results)
        total_passed = sum(r.passed for r in runner.suite_results)
        total_failed = sum(r.failed + r.errors for r in runner.suite_results)

        print(f"总测试数: {total_tests}")
        print(f"通过: {total_passed}")
        print(f"失败: {total_failed}")
        print(f"通过率: {total_passed/total_tests*100:.1f}%")

        if total_failed == 0:
            print("\n所有测试通过！")
        else:
            print(f"\n有 {total_failed} 个测试失败，请查看报告详情。")

    except KeyboardInterrupt:
        print("\n测试被用户中断")
    except Exception as exc:
        print(f"\n发生错误: {exc}")
        traceback.print_exc()
    finally:
        runner.teardown_browser()


if __name__ == "__main__":
    main()
