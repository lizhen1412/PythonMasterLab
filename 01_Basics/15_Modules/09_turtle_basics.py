#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：turtle 绘图入门。

注意：需要图形界面。无图形环境（如 CI/远程服务器）会自动跳过并打印提示。
"""

from __future__ import annotations

import os
import sys
from typing import Optional


def can_use_gui() -> bool:
    """粗略检测是否可能有图形环境。"""
    if sys.platform.startswith("win"):
        return True
    return bool(os.environ.get("DISPLAY"))


def draw_square(side: int = 100) -> None:
    """绘制一个简单的方形。"""
    import turtle  # 延迟导入，避免无 GUI 环境直接报错

    screen = turtle.Screen()
    t = turtle.Turtle()
    for _ in range(4):
        t.forward(side)
        t.right(90)
    screen.exitonclick()  # 点击关闭窗口


def main() -> None:
    if not can_use_gui():
        print("检测到无图形界面，跳过 turtle 演示。")
        print("提示：在本地桌面环境运行此脚本可看到绘图窗口。")
        return

    print("打开绘图窗口，点击窗口关闭后程序结束。")
    draw_square(120)


if __name__ == "__main__":
    main()
