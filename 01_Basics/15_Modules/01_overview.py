#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 模块与包（Modules & Packages）章节索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/15_Modules/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_import_basics.py", "模块导入基础：import/from/as、__name__ 与脚本入口"),
    ("03_package_structure_and_init.py", "包结构、__init__.py、相对导入与 __all__ 讲解"),
    ("04_random_basics.py", "random：取数、打乱、采样、种子"),
    ("05_random_guessing_game.py", "随机小游戏：猜数字（模拟输入）"),
    ("06_regex_basics.py", "正则基础：编译、搜索、分组、替换"),
    ("07_id_card_validation.py", "身份证号校验：格式 + 出生日期 + 校验码"),
    ("08_datetime_and_time.py", "日期时间：now/utc/格式化/解析/时间戳"),
    ("09_turtle_basics.py", "turtle 绘图入门（需图形界面，内置安全跳过）"),
    ("10_socket_basics.py", "socket 基础：地址族/类型，socketpair 本地收发演示"),
    ("11_installing_third_party_packages.md", "文档：pip/venv/uv/pipx 安装第三方库指南"),
    ("12_chapter_summary.py", "本章总结：规则清单与常见坑"),
    ("13_package_main_and_reload.py", "包入口（-m/__main__.py）与模块缓存、reload"),
    ("14_importing_resources.py", "importlib.resources 读取包内资源文件"),
    ("15_secrets_vs_random.py", "安全随机：secrets vs random（密码学 vs 非安全）"),
    ("Exercises/01_overview.py", "练习题索引（每题一个文件）"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
