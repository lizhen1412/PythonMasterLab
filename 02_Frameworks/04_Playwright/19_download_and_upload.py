#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 19：下载与上传。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/19_download_and_upload.py

本示例展示如何处理文件下载和上传：
1. set_input_files(): 模拟文件选择/上传
2. expect_download(): 等待并捕获下载文件
3. download.save_as(): 保存下载的文件

核心概念：
- 文件上传：使用 set_input_files() 直接指定本地文件路径
- 文件下载：使用 expect_download() 捕获下载事件
- 下载的文件默认保存在临时目录，可以使用 save_as() 移动

文件上传：
- set_input_files(selector, file_path): 上传单个文件
- set_input_files(selector, [path1, path2]): 上传多个文件
- 支持绝对路径和相对路径

文件下载：
- expect_download() 返回 DownloadContext，通过 .value 获取 Download 对象
- download.save_as(path): 保存文件到指定位置
- download.failure(): 获取下载失败信息（如果有）
- download.path(): 获取下载文件的临时路径

常见用途：
- 测试文件导入/导出功能
- 自动化下载报表
- 上传配置文件或数据文件
"""

from __future__ import annotations

from pathlib import Path


# 临时目录和文件路径
TMP_DIR = Path("/tmp/playwright_demo")
UPLOAD_FILE = TMP_DIR / "upload_source.txt"
DOWNLOAD_FILE = TMP_DIR / "download_result.txt"


# 模拟包含文件上传和下载功能的 HTML
HTML = """
<input type="file" id="file" />
<p id="filename"></p>
<a id="dl" download="demo.txt" href="data:text/plain,download-ok">download</a>
<script>
  document.querySelector('#file').addEventListener('change', (e) => {
    const files = e.target.files;
    document.querySelector('#filename').textContent = files.length ? files[0].name : '';
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 创建临时目录和测试文件
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    UPLOAD_FILE.write_text("upload-demo", encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.set_content(HTML)

            # === 文件上传 ===
            # set_input_files() 直接指定要上传的文件路径
            # 这会自动填写文件选择框，触发 change 事件
            page.set_input_files("#file", str(UPLOAD_FILE))
            print("uploaded file name ->", page.locator("#filename").inner_text())

            # === 文件下载 ===
            # expect_download() 等待并捕获下载事件
            # 返回 DownloadContext，通过 .value 获取 Download 对象
            with page.expect_download() as download_info:
                page.click("#dl")

            download = download_info.value
            # save_as() 将下载的文件保存到指定路径
            download.save_as(str(DOWNLOAD_FILE))
            print("download saved ->", DOWNLOAD_FILE)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
