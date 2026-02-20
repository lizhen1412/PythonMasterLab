#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：collections.ChainMap。
Author: Lambert

你会学到：
1) 多个 dict 的“分层视图”
2) 读取时按层覆盖
3) new_child 可以临时覆盖

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/05_collections_chainmap.py
"""

from collections import ChainMap


def main() -> None:
    defaults = {"host": "localhost", "port": 8000}
    env = {"port": 9000}
    cli = {"debug": True}

    config = ChainMap(cli, env, defaults)
    print("config host ->", config["host"])
    print("config port ->", config["port"])
    print("config debug ->", config["debug"])

    override = config.new_child({"host": "0.0.0.0"})
    print("override host ->", override["host"])
    print("original host ->", config["host"])


if __name__ == "__main__":
    main()