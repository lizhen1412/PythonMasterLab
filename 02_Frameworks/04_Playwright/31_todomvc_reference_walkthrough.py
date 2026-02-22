#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 31：third_party Todomvc 参考用例走读。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/31_todomvc_reference_walkthrough.py

本示例展示 Playwright 官方的 TodoMVC 参考测试用例：
1. 展示测试用例列表
2. 推荐学习顺序
3. 真实项目的测试模式

核心概念：
- TodoMVC 是一个著名的待办事项应用
- Playwright 官方提供了完整的测试用例
- 这些用例展示了最佳实践和常见模式

参考用例位置：
- third_party_refs/playwright-python/examples/todomvc/mvctests
- 包含多个 test_*.py 文件
- 涵盖增删改查等常见操作

学习顺序建议：
1. test_new_todo.py: 创建新任务
2. test_item.py: 单个任务操作
3. test_mark_all_as_completed.py: 批量操作
4. test_routing.py: 路由和过滤

测试模式：
- 使用 pytest 和 pytest-playwright
- Page fixture 自动管理
- get_by_role 等语义化定位器
- expect 断言自动重试

这些参考用例展示了：
- 如何组织测试结构
- 如何处理异步操作
- 如何使用 Playwright 的各种功能
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path("third_party_refs/playwright-python/examples/todomvc/mvctests")


def main() -> None:
    print("== Todomvc 参考用例列表 ==\n")
    if not ROOT.exists():
        print("未找到参考目录：", ROOT)
        return

    tests = sorted(ROOT.glob("test_*.py"))
    for p in tests:
        print("-", p.name)

    print("\n建议学习顺序：")
    print("1) test_new_todo.py")
    print("2) test_item.py")
    print("3) test_mark_all_as_completed.py")
    print("4) test_routing.py")


if __name__ == "__main__":
    main()
