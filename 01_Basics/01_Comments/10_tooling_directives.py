#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：工具指令注释（pragma-like comments）。

这些注释对 Python 解释器没有任何意义，但常被各类工具读取，例如：
- flake8/ruff:  `# noqa`（忽略某行的 lint 报警）
- black:        `# fmt: off` / `# fmt: on`
- isort:        `# isort: skip`
- pylint:       `# pylint: disable=...`
- coverage.py:  `# pragma: no cover`

注意：这些指令是否生效，取决于你实际使用的工具及其配置。
"""

from __future__ import annotations


def main() -> None:
    # noqa 示例：通常用来忽略“这一行太长”等 lint 规则（解释器会忽略）
    long_text = "x" * 120  # noqa: E501

    # black 示例：格式化工具可能会跳过 fmt off/on 区域
    # fmt: off
    ugly_list = [1,2,3,4,5]  # noqa: E231
    # fmt: on

    # isort 示例：让 import 排序工具跳过下一行
    import sys  # isort: skip

    # pylint 示例：关闭指定检查项（需要 pylint）
    unused_variable = 123  # pylint: disable=unused-variable

    # coverage 示例：让覆盖率工具忽略这一行/分支（需要 coverage 配置）
    if False:  # pragma: no cover
        print("never")

    print("len(long_text) =", len(long_text))
    print("ugly_list      =", ugly_list)
    print("sys.version    =", sys.version.split()[0])
    print("unused_variable=", unused_variable)


if __name__ == "__main__":
    main()
