#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：多行输入（直到哨兵 END）。
Author: Lambert

常见场景：
- 让用户粘贴一段多行文本（配置、SQL、日志片段、备注等）
- 以某个“哨兵行”结束输入，例如输入一行 `END` 表示结束

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/07_multiline_until_sentinel.py
"""

from __future__ import annotations


def main() -> None:
    print("请输入多行文本；输入一行 END 结束：")
    lines: list[str] = []

    while True:
        try:
            line = input()
        except EOFError:
            print("\n遇到 EOF，结束输入。")
            break
        except KeyboardInterrupt:
            print("\n输入被中断，结束输入。")
            break

        if line == "END":
            break

        lines.append(line)

    text = "\n".join(lines)
    print("\n你输入了", len(lines), "行：")
    print("--- BEGIN ---")
    print(text)
    print("--- END ---")


if __name__ == "__main__":
    main()
