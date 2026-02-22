#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 30：Codegen 与调试命令清单。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/30_codegen_and_debug_commands.py

本示例展示 Playwright 的常用命令行工具：
1. playwright codegen: 录制浏览器操作生成代码
2. PWDEBUG: 调试模式
3. playwright show-trace: 查看 trace 文件
4. playwright --version: 查看版本

核心概念：
- Playwright 提供了丰富的命令行工具
- codegen 可以快速生成测试代码
- 调试工具帮助定位问题
- trace 文件记录完整执行过程

命令清单：
- codegen: 录制操作并生成代码
- show-trace: 查看录制好的 trace
- --version: 显示版本信息
- install: 安装浏览器驱动

调试模式：
- PWDEBUG=1: 启用调试模式，打开 inspector
- PWDEBUG=console: 只输出调试信息
- PWDEBUG=0: 禁用调试

codegen 参数：
- --target: 生成代码语言（python/python-async）
- --browser: 选择浏览器
- --save-trace: 保存 trace 文件
- --save-storage: 保存登录状态

常见用途：
- 快速生成测试代码
- 调试测试失败
- 查看详细的执行过程
"""

from __future__ import annotations


def main() -> None:
    print("== Playwright 常用命令（新手必备） ==\n")

    print("1) 录制脚本（codegen）：")
    print("   python3 -m playwright codegen https://example.com")

    print("\n2) 打开 Inspector 调试：")
    print("   PWDEBUG=1 python3 your_script.py")

    print("\n3) 生成 Trace 后查看：")
    print("   python3 -m playwright show-trace /path/to/trace.zip")

    print("\n4) 查看版本：")
    print("   python3 -m playwright --version")


if __name__ == "__main__":
    main()
