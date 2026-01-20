#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：模块与包（Modules & Packages）章节练习。

运行方式（在仓库根目录执行）：
    python3 01_Basics/15_Modules/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_inspect_import_paths.py", "查看/修改 sys.path，理解导入搜索顺序"),
    ("03_random_dice_simulation.py", "模拟掷骰子 10000 次，统计频率"),
    ("04_regex_extract_emails.py", "用正则提取邮箱地址列表"),
    ("05_validate_id_cards.py", "批量校验身份证号（调用章节函数）"),
    ("06_socket_echo_with_socketpair.py", "用 socket.socketpair 实现本地 echo"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习题清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
