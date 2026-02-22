#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 20：录制视频（context.record_video_dir）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/20_video_recording.py

本示例展示如何使用 Playwright 录制浏览器操作视频：
1. record_video_dir: 设置视频录制目录
2. page.video.path(): 获取录制视频的文件路径

核心概念：
- Playwright 可以在 context 级别录制所有页面的视频
- 视频仅在 context 关闭后才会保存到磁盘
- 每个页面和 frame 都会有独立的视频文件
- 视频以 webm 格式录制

视频录制：
- record_video_dir: 指定视频保存目录
- record_video_size: 可选，指定视频尺寸（宽 x 高）
- 视频文件名格式：{hash}.webm

访问视频：
- context.close() 后，通过 page.video.path() 获取视频路径
- 如果 video 为 None，说明当前模式未生成视频

常见用途：
- 调试测试失败时的操作过程
- 生成测试执行的视频报告
- 演示自动化脚本执行效果

注意事项：
- 视频文件仅在 context 关闭后才会写入磁盘
- 录制视频会略微降低性能
- 视频质量可以通过 launch 参数调整
"""

from __future__ import annotations

from pathlib import Path


# 视频保存目录
VIDEO_DIR = Path("/tmp/playwright_demo/videos")


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 创建视频保存目录
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = None
        try:
            # 创建 context 并启用视频录制
            # record_video_dir: 指定视频保存目录
            # record_video_size: 可选，指定视频尺寸，如 {"width": 1280, "height": 720}
            context = browser.new_context(record_video_dir=str(VIDEO_DIR))
            page = context.new_page()
            page.set_content("<h2>recording video</h2>")
            # 等待一小段时间，确保视频录制到内容
            page.wait_for_timeout(200)

            # context 关闭后，视频文件才会保存到磁盘
            context.close()
            context = None  # 标记已关闭
            video = page.video
            if video is None:
                print("当前运行模式未生成 video 对象")
            else:
                print("video path ->", video.path())
        finally:
            if context:
                context.close()
            browser.close()


if __name__ == "__main__":
    main()
