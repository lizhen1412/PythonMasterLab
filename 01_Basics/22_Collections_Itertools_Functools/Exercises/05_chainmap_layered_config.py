#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：ChainMap 配置覆盖。

题目：
实现函数 `build_config(defaults, user, env)`：
- 返回 ChainMap，优先级 env > user > defaults

示例：
    defaults={"host":"localhost","port":8000}
    user={"port":9000}
    env={"debug":True}
    -> config["port"] == 9000

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/22_Collections_Itertools_Functools/Exercises/05_chainmap_layered_config.py
"""

from collections import ChainMap


def build_config(defaults: dict, user: dict, env: dict) -> ChainMap:
    return ChainMap(env, user, defaults)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    defaults = {"host": "localhost", "port": 8000}
    user = {"port": 9000}
    env = {"debug": True}
    config = build_config(defaults, user, env)

    check("host", config["host"], "localhost")
    check("port", config["port"], 9000)
    check("debug", config["debug"], True)


if __name__ == "__main__":
    main()
