#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：保存/读取（内存 I/O）。

运行：
    python3 02_Frameworks/02_Numpy/14_io_save_load.py
"""

from __future__ import annotations

from io import BytesIO, StringIO

import numpy as np


def main() -> None:
    arr = np.arange(5)

    print("np.save / np.load (BytesIO) ->")
    buffer = BytesIO()
    np.save(buffer, arr)
    buffer.seek(0)
    loaded = np.load(buffer)
    print(loaded)

    print("
np.savetxt / np.loadtxt (StringIO) ->")
    text_buffer = StringIO()
    np.savetxt(text_buffer, arr, fmt="%.1f", delimiter=",")
    text = text_buffer.getvalue()
    print(text)

    text_buffer.seek(0)
    loaded_text = np.loadtxt(text_buffer, delimiter=",")
    print(loaded_text)


if __name__ == "__main__":
    main()
