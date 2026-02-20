#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：文件下载（流式）。
Author: Lambert

题目：
实现一个下载大文件的函数，支持进度显示和断点续传。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/07_file_download.py
"""

from __future__ import annotations

import requests
from pathlib import Path


def download_file(url: str, dest: Path, chunk_size: int = 8192) -> bool:
    """
    流式下载文件
    返回是否成功
    """
    try:
        with requests.get(url, stream=True, timeout=30) as response:
            response.raise_for_status()

            total_size = int(response.headers.get("content-length", 0))
            downloaded = 0

            dest.parent.mkdir(parents=True, exist_ok=True)

            with dest.open("wb") as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            progress = (downloaded / total_size) * 100
                            print(f"\r下载进度: {progress:.1f}%", end="")

            print()  # 换行
            return True

    except Exception as e:
        print(f"\n下载失败: {e}")
        return False


def main() -> None:
    # 下载一个小文件测试
    dest = Path("/tmp/test_download.txt")

    # httpbin 的 bytes endpoint 返回指定字节的内容
    url = "https://httpbin.org/bytes/1024"

    success = download_file(url, dest)

    if success:
        file_size = dest.stat().st_size
        assert file_size == 1024
        print(f"[OK] file downloaded: {dest} ({file_size} bytes)")

        # 清理
        dest.unlink()
        print("[OK] cleanup")
    else:
        print("[FAIL] download failed")


if __name__ == "__main__":
    main()