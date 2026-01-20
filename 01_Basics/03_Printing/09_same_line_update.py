#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：同一行刷新输出（进度条/状态更新）

如果你想“不断更新同一行”，常用技巧是：
- `end="\\r"`（回到行首）或 `end=""`（不换行）
- `flush=True`（立刻刷新）

注意：
- 在某些 IDE/日志收集器里，\\r 的效果可能会被“当成换行”或显示不一致；
  这属于终端/环境差异，不是 Python 语法问题。

运行：
    python3 01_Basics/03_Printing/09_same_line_update.py
"""

import time


def main() -> None:
    for i in range(0, 101, 10):
        print(f"\rprogress={i:3d}%", end="", flush=True)
        time.sleep(0.05)
    print()  # 换行收尾

    print("\n同一行拼接多个片段（end 不换行）：")
    print("user=", end="")
    print("Alice", end=" ")
    print("score=", end="")
    print(98)


if __name__ == "__main__":
    main()

