#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：读取包内资源文件。

- `importlib.resources.files` / `read_text`
- 避免手写相对路径（更健壮，可打包/嵌入）

说明：`importlib.resources` 需要“可导入的包名”。本仓库目录名以数字开头并未做成包，
所以示例使用标准库包 `importlib` 来演示用法，思路相同。
"""

from __future__ import annotations

import importlib.resources as res


def read_importlib_init() -> str:
    """读取标准库 importlib/__init__.py 的前几行。"""
    init_file = res.files("importlib") / "__init__.py"
    return "\n".join(init_file.read_text(encoding="utf-8").splitlines()[:3])


def list_importlib_resources(limit: int = 5) -> None:
    paths = list(res.files("importlib").iterdir())[:limit]
    for path in paths:
        print("-", path.name)


def main() -> None:
    print("importlib/__init__.py 开头几行：")
    print(read_importlib_init())

    print("\nimportlib 包内资源（部分）：")
    list_importlib_resources()

    print(
        "\n提示：自己的项目若有数据文件，请确保目录是合法包名并包含 __init__.py，"
        "然后使用 importlib.resources.files('yourpkg').joinpath('data/config.json') 来读取。"
    )


if __name__ == "__main__":
    main()
