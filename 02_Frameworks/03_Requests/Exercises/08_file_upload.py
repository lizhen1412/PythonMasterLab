#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：文件上传。
Author: Lambert

题目：
实现一个上传文件的函数，支持单文件和多文件上传。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/03_Requests/Exercises/08_file_upload.py
"""

from __future__ import annotations

import requests
from pathlib import Path


def upload_file(url: str, file_path: Path, file_key: str = "file") -> dict:
    """上传单个文件"""
    with file_path.open("rb") as f:
        files = {file_key: (file_path.name, f)}
        response = requests.post(url, files=files, timeout=30)
        response.raise_for_status()
        return response.json()


def upload_multiple_files(url: str, file_paths: list[Path]) -> dict:
    """上传多个文件"""
    files = []
    for file_path in file_paths:
        files.append(
            ("files", (file_path.name, file_path.open("rb"), "application/octet-stream"))
        )

    # 注意：使用 context manager 自动关闭文件
    import contextlib

    with contextlib.ExitStack() as stack:
        files = [
            ("files", (path.name, stack.enter_context(path.open("rb")), "text/plain"))
            for path in file_paths
        ]
        response = requests.post(url, files=files, timeout=30)
        response.raise_for_status()
        return response.json()


def main() -> None:
    # 创建测试文件
    test_file = Path("/tmp/test_upload.txt")
    test_file.write_text("Hello, this is a test file for upload!")

    # 单文件上传测试
    url = "https://httpbin.org/post"
    result = upload_file(url, test_file)
    assert result["files"] is not None
    print("[OK] single file upload")

    # 多文件上传测试
    test_file2 = Path("/tmp/test_upload2.txt")
    test_file2.write_text("Second test file")

    result = upload_multiple_files(url, [test_file, test_file2])
    assert "files" in result
    print("[OK] multiple file upload")

    # 清理
    test_file.unlink()
    test_file2.unlink()
    print("[OK] cleanup")


if __name__ == "__main__":
    main()