#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：编码声明注释（encoding cookie）：`# coding: <encoding>`。

要点：
1) 这行注释必须位于文件的第 1 行或第 2 行（如果第 1 行是 shebang）。
2) Python 3 默认源文件编码是 UTF-8，所以多数情况下不写也可以。
3) 但它仍然被 tokenize/解释器用于检测源文件编码（尤其是非 UTF-8 的历史文件）。
"""

from __future__ import annotations

from pathlib import Path
import tokenize


def main() -> None:
    path = Path(__file__)
    with path.open("rb") as f:
        encoding, _ = tokenize.detect_encoding(f.readline)

    print("detected encoding =", encoding)
    print("中文/emoji 等 Unicode 字符在 UTF-8 源码里可以直接使用：")
    print("示例文本：你好，Python 注释！")


if __name__ == "__main__":
    main()
