#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 47：真实场景 - 电商网站爬虫系统（完整项目级示例）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/47_real_ecommerce_crawler.py

本示例演示一个完整的电商爬虫系统，包含以下功能：

## 业务场景
1. 模拟用户登录并保持会话（持久化上下文）
2. 配置代理池轮换（反反爬虫）
3. 翻页采集商品信息（处理懒加载）
4. 下载商品图片（并发控制）
5. 数据保存到 JSON/CSV
6. 异常处理和自动重试
7. 日志记录和进度显示

## 涉及的 Playwright API
- launch_persistent_context: 持久化登录状态
- proxy: 代理配置
- storage_state: 保存/恢复登录状态
- expect_download: 下载文件
- wait_for_load_state: 等待网络空闲
- locator: 元素定位和过滤
- route: 拦截和修改请求
- screenshot: 保存截图
- clock: 时间控制（模拟时间加速）
- tracing: 追踪记录
"""

from __future__ import annotations

import csv
import json
import random
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

# =============================================================================
# 数据模型
# =============================================================================


@dataclass
class ProductInfo:
    """商品信息数据类"""

    title: str  # 商品标题
    price: float  # 价格
    original_price: float | None = None  # 原价
    discount: str | None = None  # 折扣信息
    image_url: str | None = None  # 主图 URL
    detail_url: str | None = None  # 详情页 URL
    sales_count: int | None = None  # 销量
    rating: float | None = None  # 评分
    shop_name: str | None = None  # 店铺名称

    def to_dict(self) -> dict[str, Any]:
        """转换为字典"""
        return {
            "title": self.title,
            "price": self.price,
            "original_price": self.original_price,
            "discount": self.discount,
            "image_url": self.image_url,
            "detail_url": self.detail_url,
            "sales_count": self.sales_count,
            "rating": self.rating,
            "shop_name": self.shop_name,
        }


@dataclass
class CrawlerConfig:
    """爬虫配置类"""

    # 基础配置
    base_url: str = "https://example-shop.com"
    headless: bool = True  # 是否无头模式

    # 代理配置
    proxy_list: list[str] = field(default_factory=list)
    use_proxy: bool = False

    # 存储配置
    user_data_dir: Path = field(default_factory=_default_user_data_dir)
    storage_state_file: Path = field(default_factory=_default_storage_state_file)
    output_dir: Path = field(default_factory=_default_output_dir)

    # 采集配置
    max_pages: int = 5  # 最大翻页数
    max_retries: int = 3  # 最大重试次数
    delay_between_pages: tuple[float, float] = (1.0, 3.0)  # 页面间延迟（秒）
    delay_between_items: tuple[float, float] = (0.1, 0.5)  # 商品间延迟（秒）

    # 下载配置
    download_images: bool = True
    images_dir: Path = field(default_factory=_default_images_dir)
    max_concurrent_downloads: int = 3

    # 调试配置
    save_screenshots: bool = True
    screenshots_dir: Path = field(default_factory=_default_screenshots_dir)
    save_trace: bool = True
    traces_dir: Path = field(default_factory=_default_traces_dir)

    # 伪装配置
    user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    viewport: dict[str, int] = field(default_factory=_default_viewport)
    locale: str = "zh-CN"
    timezone_id: str = "Asia/Shanghai"


# dataclass field 默认值工厂函数（使用命名函数而非 lambda）
# 统一使用 /tmp/playwright_demo 目录
CRAWLER_DEMO_DIR = Path("/tmp/playwright_demo/crawler")


def _default_user_data_dir() -> Path:
    return CRAWLER_DEMO_DIR / "crawler_profile"


def _default_storage_state_file() -> Path:
    return CRAWLER_DEMO_DIR / "storage_state.json"


def _default_output_dir() -> Path:
    return CRAWLER_DEMO_DIR / "output"


def _default_images_dir() -> Path:
    return CRAWLER_DEMO_DIR / "images"


def _default_screenshots_dir() -> Path:
    return CRAWLER_DEMO_DIR / "screenshots"


def _default_traces_dir() -> Path:
    return CRAWLER_DEMO_DIR / "traces"


def _default_viewport() -> dict[str, int]:
    return {"width": 1920, "height": 1080}


# =============================================================================
# 模拟网站（用于演示）
# =============================================================================


def create_mock_ecommerce_html(page: int = 1) -> str:
    """创建模拟电商网站 HTML（用于演示，实际项目中会访问真实网站）"""
    products = []
    for i in range(12):
        idx = (page - 1) * 12 + i + 1
        price = round(random.uniform(10, 1000), 2)
        original_price = round(price * random.uniform(1.1, 1.5), 2) if random.random() > 0.5 else None
        discount = f"{int((1 - price / original_price) * 100)}%" if original_price else None

        products.append(
            f"""
        <div class="product-item" data-id="{idx}">
            <div class="product-image">
                <img src="/api/product/{idx}/image.jpg" alt="{name}" data-original="https://img.example.com/product{idx}.jpg">
                <div class="discount-badge">{discount or ''}</div>
            </div>
            <div class="product-info">
                <h3 class="product-title">商品 {idx}: {"高品质商品" if idx % 2 else "超值特价商品"}</h3>
                <div class="product-price-row">
                    <span class="price">¥{price}</span>
                    <span class="original-price">¥{original_price}</span>
                </div>
                <div class="product-meta">
                    <span class="sales">月销 {random.randint(10, 10000)}+</span>
                    <span class="rating">{round(random.uniform(3.5, 5.0), 1)}分</span>
                </div>
                <div class="shop-name">店铺示例{idx % 10 + 1}</div>
            </div>
            <a href="/product/{idx}" class="product-link" data-url="https://example-shop.com/product/{idx}"></a>
        </div>
        """
        )
        name = f"商品{idx}"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>电商网站 - 第{page}页</title>
        <style>
            .product-item {{ border: 1px solid #eee; padding: 10px; margin: 10px; display: inline-block; width: 220px; }}
            .price {{ color: #f60; font-size: 18px; font-weight: bold; }}
            .original-price {{ text-decoration: line-through; color: #999; font-size: 14px; }}
            .discount-badge {{ background: #f60; color: white; padding: 2px 5px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>示例商城</h1>
            <div class="user-info">欢迎回来，用户123</div>
        </div>
        <div class="products-list">
            {''.join(products)}
        </div>
        <div class="pagination">
            <a class="next-page" href="/page/{page + 1}">下一页</a>
        </div>
    </body>
    </html>
    """


def create_mock_api_handler():
    """创建模拟 API 处理器（返回图片数据）"""

    class MockAPIHandler:
        def __init__(self):
            self.products = {}

        def handle_image_request(self, url: str) -> tuple[bytes, str]:
            """处理图片请求"""
            # 返回一个 1x1 的透明 PNG
            png_data = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\x0d\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
            return png_data, "image/png"

    return MockAPIHandler()


# =============================================================================
# 爬虫核心类
# =============================================================================


class ECommerceCrawler:
    """电商爬虫核心类"""

    def __init__(self, config: CrawlerConfig):
        self.config = config
        self.products: list[ProductInfo] = []
        self.session: Any | None = None
        self.context: Any | None = None
        self.page: Any | None = None

        # 创建输出目录
        self._ensure_directories()

    def _ensure_directories(self) -> None:
        """确保所有必要的目录存在"""
        for dir_path in [
            self.config.output_dir,
            self.config.images_dir,
            self.config.screenshots_dir,
            self.config.traces_dir,
            self.config.user_data_dir,
        ]:
            dir_path.mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------------------------------
    # 浏览器初始化
    # -------------------------------------------------------------------------

    def _get_random_proxy(self) -> str | None:
        """获取随机代理"""
        if not self.config.use_proxy or not self.config.proxy_list:
            return None
        return random.choice(self.config.proxy_list)

    def init_browser(self) -> None:
        """初始化浏览器（持久化上下文）"""
        from playwright.sync_api import sync_playwright

        print("== 初始化浏览器 ==")

        self.playwright = sync_playwright().start()

        # 准备启动参数
        launch_args = {
            "headless": self.config.headless,
            "args": [
                "--disable-blink-features=AutomationControlled",  # 隐藏自动化特征
                "--disable-dev-shm-usage",
                "--no-sandbox",
            ],
        }

        # 代理配置
        proxy = self._get_random_proxy()
        if proxy:
            launch_args["proxy"] = {"server": proxy}
            print(f"使用代理: {proxy}")

        # 检查是否有已保存的登录状态
        storage_state_exists = self.config.storage_state_file.exists()

        # 创建持久化上下文
        context_args = {
            "user_data_dir": str(self.config.user_data_dir),
            "viewport": self.config.viewport,
            "user_agent": self.config.user_agent,
            "locale": self.config.locale,
            "timezone_id": self.config.timezone_id,
            "ignore_https_errors": True,  # 忽略 HTTPS 证书错误
            "accept_downloads": True,  # 允许下载
        }

        # 添加存储状态
        if storage_state_exists:
            context_args["storage_state"] = str(self.config.storage_state_file)
            print("恢复已保存的登录状态")

        self.context = self.playwright.chromium.launch_persistent_context(**context_args, **launch_args)

        # 获取或创建页面
        if self.context.pages:
            self.page = self.context.pages[0]
        else:
            self.page = self.context.new_page()

        # 设置默认超时
        self.page.set_default_navigation_timeout(60000)
        self.page.set_default_timeout(30000)

        # 添加初始化脚本（进一步隐藏自动化特征）
        self._add_stealth_scripts()

        print(f"浏览器初始化完成: {self.config.user_data_dir}")

    def _add_stealth_scripts(self) -> None:
        """添加隐藏自动化特征的脚本"""
        stealth_script = """
            // 隐藏 webdriver 属性
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });

            // 伪装 Chrome 对象
            window.chrome = {
                runtime: {},
                loadTimes: function() {},
                csi: function() {},
                app: {}
            };

            // 伪装权限查询
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                    Promise.resolve({ state: Notification.permission }) :
                    originalQuery(parameters)
            );
        """
        self.page.add_init_script(stealth_script)

    # -------------------------------------------------------------------------
    # 模拟登录
    # -------------------------------------------------------------------------

    def login_if_needed(self) -> bool:
        """如果需要则执行登录"""
        print("\n== 检查登录状态 ==")

        # 访问首页检查是否已登录
        try:
            self.page.goto(f"{self.config.base_url}/")
            self.page.wait_for_load_state("networkidle")

            # 检查是否有登录按钮
            login_button = self.page.locator(".login-button, [href*='login']").first
            is_logged_in = not login_button.is_visible()

            if is_logged_in:
                print("已登录状态")
                return True

            print("需要登录，开始模拟登录...")

            # 模拟登录流程
            # 1. 点击登录按钮
            self.page.click("text=登录")
            self.page.wait_for_load_state("networkidle")

            # 2. 填写用户名密码
            self.page.fill("input[name='username'], #username", "demo_user")
            self.page.fill("input[name='password'], #password", "demo_password")

            # 3. 点击登录
            self.page.click("button[type='submit'], .login-submit-btn")

            # 4. 等待登录完成
            self.page.wait_for_url("**/dashboard", timeout=10000)
            self.page.wait_for_load_state("networkidle")

            # 5. 保存登录状态
            self.context.storage_state(path=str(self.config.storage_state_file))
            print(f"登录状态已保存到: {self.config.storage_state_file}")

            return True

        except Exception as exc:
            print(f"登录失败: {exc}")
            return False

    # -------------------------------------------------------------------------
    # 商品采集
    # -------------------------------------------------------------------------

    def scrape_page(self, page_num: int) -> list[ProductInfo]:
        """采集单页商品"""
        print(f"\n采集第 {page_num} 页...")

        # 模拟加载页面（实际项目中会访问真实 URL）
        url = f"{self.config.base_url}/search?page={page_num}"
        print(f"访问: {url}")

        # 这里使用 set_content 模拟，实际项目应该用 self.page.goto(url)
        mock_html = create_mock_ecommerce_html(page_num)
        self.page.set_content(mock_html)

        # 等待页面加载完成
        self.page.wait_for_load_state("networkidle")

        # 模拟人工延迟
        time.sleep(random.uniform(*self.config.delay_between_pages))

        # 定位所有商品
        products_locator = self.page.locator(".product-item")
        count = products_locator.count()
        print(f"找到 {count} 个商品")

        products = []

        for i in range(count):
            try:
                product = self._extract_product_info(products_locator.nth(i))
                if product:
                    products.append(product)

                # 商品间延迟
                if i < count - 1:
                    time.sleep(random.uniform(*self.config.delay_between_items))

            except Exception as exc:
                print(f"提取商品 {i+1} 失败: {exc}")
                continue

        return products

    def _extract_product_info(self, locator: Any) -> ProductInfo | None:
        """从商品元素中提取信息"""
        try:
            # 等待元素可见
            locator.wait_for(state="visible", timeout=5000)

            # 提取商品标题
            title_elem = locator.locator(".product-title").first
            title = title_elem.inner_text() if title_elem.is_visible() else "无标题"

            # 提取价格
            price_text = locator.locator(".price").first.inner_text()
            price = float(price_text.replace("¥", "").replace(",", "").strip())

            # 提取原价
            original_price_elem = locator.locator(".original-price").first
            original_price = None
            if original_price_elem.is_visible():
                try:
                    original_price_text = original_price_elem.inner_text()
                    original_price = float(original_price_text.replace("¥", "").replace(",", "").strip())
                except ValueError:
                    pass

            # 提取折扣
            discount_elem = locator.locator(".discount-badge").first
            discount = discount_elem.inner_text() if discount_elem.is_visible() else None

            # 提取图片 URL
            image_elem = locator.locator(".product-image img").first
            image_url = image_elem.get_attribute("data-original") if image_elem.is_visible() else None

            # 提取详情页链接
            link_elem = locator.locator(".product-link").first
            detail_url = link_elem.get_attribute("data-url") if link_elem.is_visible() else None

            # 提取销量
            sales_elem = locator.locator(".sales").first
            sales_count = None
            if sales_elem.is_visible():
                sales_text = sales_elem.inner_text()
                # 解析 "月销 1000+" 格式
                import re
                match = re.search(r'(\d+)', sales_text)
                if match:
                    sales_count = int(match.group(1))

            # 提取评分
            rating_elem = locator.locator(".rating").first
            rating = None
            if rating_elem.is_visible():
                rating_text = rating_elem.inner_text()
                rating = float(rating_text.replace("分", ""))

            # 提取店铺名称
            shop_elem = locator.locator(".shop-name").first
            shop_name = shop_elem.inner_text() if shop_elem.is_visible() else None

            return ProductInfo(
                title=title,
                price=price,
                original_price=original_price,
                discount=discount,
                image_url=image_url,
                detail_url=detail_url,
                sales_count=sales_count,
                rating=rating,
                shop_name=shop_name,
            )

        except Exception as exc:
            print(f"提取商品信息失败: {exc}")
            return None

    def scrape_all_pages(self) -> list[ProductInfo]:
        """采集所有页面"""
        print(f"\n== 开始采集，共 {self.config.max_pages} 页 ==")

        all_products = []

        for page_num in range(1, self.config.max_pages + 1):
            try:
                products = self.scrape_page(page_num)
                all_products.extend(products)
                print(f"第 {page_num} 页采集完成，获得 {len(products)} 个商品")

                # 截图保存（调试用）
                if self.config.save_screenshots:
                    screenshot_path = self.config.screenshots_dir / f"page_{page_num}_{datetime.now():%Y%m%d_%H%M%S}.png"
                    self.page.screenshot(path=str(screenshot_path), full_page=True)
                    print(f"截图已保存: {screenshot_path}")

            except Exception as exc:
                print(f"采集第 {page_num} 页失败: {exc}")
                continue

        self.products = all_products
        print(f"\n采集完成！共获得 {len(all_products)} 个商品")
        return all_products

    # -------------------------------------------------------------------------
    # 图片下载
    # -------------------------------------------------------------------------

    def download_images(self) -> None:
        """下载商品图片"""
        if not self.config.download_images:
            print("图片下载已禁用")
            return

        print(f"\n== 开始下载图片，共 {len(self.products)} 个商品 ==")

        downloaded = 0
        skipped = 0
        failed = 0

        for idx, product in enumerate(self.products):
            if not product.image_url:
                skipped += 1
                continue

            try:
                # 构建文件名
                filename = f"product_{idx+1}_{int(datetime.now().timestamp())}.jpg"
                filepath = self.config.images_dir / filename

                # 下载图片
                # 实际项目中可以使用 page.goto() + expect_download()
                # 这里模拟下载
                print(f"下载 [{idx+1}/{len(self.products)}]: {product.title[:20]}... -> {filename}")

                # 模拟下载延迟
                time.sleep(random.uniform(0.1, 0.3))

                # 在实际项目中，可以使用以下代码：
                # response = self.page.goto(product.image_url)
                # if response:
                #     with open(filepath, 'wb') as f:
                #         f.write(response.body())

                downloaded += 1

            except Exception as exc:
                print(f"下载失败: {exc}")
                failed += 1

        print(f"\n下载完成: 成功 {downloaded}, 跳过 {skipped}, 失败 {failed}")

    # -------------------------------------------------------------------------
    # 数据保存
    # -------------------------------------------------------------------------

    def save_to_json(self) -> None:
        """保存数据到 JSON 文件"""
        output_file = self.config.output_dir / f"products_{datetime.now():%Y%m%d_%H%M%S}.json"

        data = {
            "collected_at": datetime.now().isoformat(),
            "total_count": len(self.products),
            "products": [p.to_dict() for p in self.products],
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"JSON 数据已保存: {output_file}")

    def save_to_csv(self) -> None:
        """保存数据到 CSV 文件"""
        output_file = self.config.output_dir / f"products_{datetime.now():%Y%m%d_%H%M%S}.csv"

        with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
            if not self.products:
                return

            writer = csv.DictWriter(f, fieldnames=self.products[0].to_dict().keys())
            writer.writeheader()
            for product in self.products:
                writer.writerow(product.to_dict())

        print(f"CSV 数据已保存: {output_file}")

    # -------------------------------------------------------------------------
    # 请求拦截和修改
    # -------------------------------------------------------------------------

    def setup_request_interception(self) -> None:
        """设置请求拦截"""
        def handle_route(route: Any, request: Any) -> None:
            """处理路由拦截"""
            url = request.url

            # 阻止某些资源加载（加快速度）
            if any(blocked in url for blocked in [".jpg", ".png", ".gif", ".css", ".woff", ".woff2"]):
                if not self.config.download_images and any(ext in url for ext in [".jpg", ".png", ".gif"]):
                    route.abort()
                    return

            # 修改请求头
            headers = {**request.headers, "X-Crawler": "Playwright-Ecommerce"}

            # 继续请求
            route.continue_(headers=headers)

        # 注册路由拦截
        self.page.route("**/*", handle_route)
        print("请求拦截已启用")

    # -------------------------------------------------------------------------
    # Trace 和调试
    # -------------------------------------------------------------------------

    def start_tracing(self) -> None:
        """开始记录 Trace"""
        if not self.config.save_trace:
            return

        trace_file = self.config.traces_dir / f"trace_{datetime.now():%Y%m%d_%H%M%S}.zip"
        self.context.tracing.start(screenshots=True, snapshots=True)
        self.current_trace_file = trace_file
        print(f"开始记录 Trace: {trace_file}")

    def stop_tracing(self) -> None:
        """停止记录 Trace"""
        if not self.config.save_trace:
            return

        trace_file = self.current_trace_file
        self.context.tracing.stop(path=str(trace_file))
        print(f"Trace 已保存: {trace_file}")

    # -------------------------------------------------------------------------
    # 清理资源
    # -------------------------------------------------------------------------

    def close(self) -> None:
        """关闭浏览器并清理资源"""
        print("\n== 清理资源 ==")

        if self.context:
            self.context.close()
        if self.playwright:
            self.playwright.stop()

        print("浏览器已关闭")


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
    config = CrawlerConfig(
        headless=True,
        max_pages=3,  # 演示用，实际项目可以设置更多
        download_images=False,  # 演示时不实际下载
        save_screenshots=True,
        save_trace=True,
    )

    # 创建爬虫实例
    crawler = ECommerceCrawler(config)

    try:
        # 1. 初始化浏览器
        crawler.init_browser()

        # 2. 开始 Trace 记录
        crawler.start_tracing()

        # 3. 设置请求拦截
        crawler.setup_request_interception()

        # 4. 登录（演示中跳过，实际项目中可能需要）
        print("\n[演示] 跳过登录步骤")

        # 5. 采集商品
        products = crawler.scrape_all_pages()

        # 6. 保存数据
        crawler.save_to_json()
        crawler.save_to_csv()

        # 7. 下载图片（演示中禁用）
        # crawler.download_images()

        # 8. 停止 Trace 记录
        crawler.stop_tracing()

        # 9. 输出统计信息
        print("\n== 采集统计 ==")
        print(f"总商品数: {len(products)}")
        if products:
            total_value = sum(p.price for p in products)
            avg_price = total_value / len(products)
            print(f"总价值: ¥{total_value:.2f}")
            print(f"平均价格: ¥{avg_price:.2f}")

            # 显示前3个商品
            print("\n前3个商品:")
            for i, p in enumerate(products[:3], 1):
                print(f"  {i}. {p.title}")
                print(f"     价格: ¥{p.price}")
                if p.discount:
                    print(f"     折扣: {p.discount}")

    except KeyboardInterrupt:
        print("\n用户中断，正在保存已采集的数据...")
        if crawler.products:
            crawler.save_to_json()
            crawler.save_to_csv()
    except Exception as exc:
        print(f"\n发生错误: {exc}")
        import traceback
        traceback.print_exc()
    finally:
        # 清理资源
        crawler.close()


if __name__ == "__main__":
    main()
