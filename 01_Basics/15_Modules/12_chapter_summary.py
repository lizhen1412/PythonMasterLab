#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：本章总结与常见坑。
Author: Lambert
"""

from __future__ import annotations


RULES = [
    "保持脚本入口使用 `if __name__ == \"__main__\": main()`，被 import 时不会意外执行",
    "包目录要有 `__init__.py` 才能做相对导入；顶层脚本请用绝对导入",
    "`python -m 包名.模块` 可按包路径运行；包下 `__main__.py` 让 `python -m 包名` 生效",
    "sys.modules 缓存已导入模块；需要重新执行可用 importlib.reload（谨慎，最好重启进程）",
    "包内数据文件用 importlib.resources 读取，避免硬编码相对路径",
    "`random.seed(...)` 可以复现随机序列；不要把随机数当安全用途（请用 secrets 模块）",
    "`re.compile` 重用模式更高效；善用命名分组提升可读性",
    "日期时间使用 `datetime`/`timezone`；`time` 模块更偏低级（睡眠、时间戳）",
    "turtle 需要 GUI 环境，远程/无显示场景要提前检查或跳过",
    "socket 示例可先用 `socketpair`/本地回环测试，避免直接对外网络",
    "第三方库优先安装到虚拟环境；工具类 CLI 可用 pipx 隔离",
]


PITFALLS = [
    "循环导入：模块互相 import 会导致运行时属性缺失；拆分或延迟导入",
    "使用 `from module import *` 可能污染命名空间，且难以读懂来源，建议避免",
    "可变默认值陷阱在模块级同样存在（定义时求值）；配置对象尽量用不可变类型",
    "正则贪婪匹配导致过度匹配或性能问题；必要时使用非贪婪模式或明确边界",
    "turtle 在无显示环境会报 TclError；需要防御性检查 DISPLAY/平台",
    "网络示例不要在生产环境直接绑定 0.0.0.0 或硬编码端口，注意权限与防火墙",
    "硬编码相对路径读取资源在打包/嵌入时会失效；应使用 importlib.resources",
    "importlib.reload 不会更新已有引用，容易导致状态不一致，生产环境慎用",
]


def main() -> None:
    print("== 规则清单 ==")
    for idx, rule in enumerate(RULES, start=1):
        print(f"{idx:02d}. {rule}")

    print("\n== 常见坑 ==")
    for idx, pitfall in enumerate(PITFALLS, start=1):
        print(f"{idx:02d}. {pitfall}")


if __name__ == "__main__":
    main()