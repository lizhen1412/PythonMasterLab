#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：while 综合示例——猜数字（模拟输入，不阻塞终端）
Author: Lambert

你会学到：
1) `while` + “次数限制”模式（最多尝试 N 次）
2) `break`：猜中就提前结束
3) `continue`：跳过无效输入（本例用 None/非 int 模拟）
4) `while ... else`：只有“没有 break（没猜中）”才执行 else

运行（在仓库根目录执行）：
    python3 01_Basics/11_Loops/08_guess_number_game_simulated.py
"""

from __future__ import annotations


def play_guess_game(secret: int, guesses: list[object], max_attempts: int = 5) -> str:
    attempt = 0
    i = 0
    while attempt < max_attempts and i < len(guesses):
        raw = guesses[i]
        i += 1

        if not isinstance(raw, int):
            # 无效输入：不消耗尝试次数，但要进入下一轮
            continue

        attempt += 1
        if raw == secret:
            break
        if raw < secret:
            print(f"attempt {attempt}: {raw} -> too small")
        else:
            print(f"attempt {attempt}: {raw} -> too large")
    else:
        return "LOSE"
    return "WIN"


def main() -> None:
    print("case 1) win")
    result = play_guess_game(secret=7, guesses=[None, "x", 3, 9, 7], max_attempts=3)
    print("result ->", result)
    print()

    print("case 2) lose (no break)")
    result2 = play_guess_game(secret=7, guesses=[1, 2, 3, 4], max_attempts=3)
    print("result ->", result2)


if __name__ == "__main__":
    main()
