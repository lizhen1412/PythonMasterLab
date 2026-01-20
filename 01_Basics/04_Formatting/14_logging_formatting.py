#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：logging 的格式化（工程里更推荐“日志系统”而不是到处 print）。

你会学到：
1) logging 的 Formatter 决定最终输出格式（时间、级别、消息等）
2) 推荐写法：`logger.info("user=%s age=%d", user, age)`（延迟格式化）
   - 好处：如果这一条日志被过滤掉（级别不够），就不会花时间做字符串拼接
3) 也可以用 `{}` 风格或 `$` 风格的 Formatter（但 message 的参数化仍推荐用 %s）

运行：
    python3 01_Basics/04_Formatting/14_logging_formatting.py
"""

import logging


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    logger = logging.getLogger("demo")

    user = "Alice"
    age = 20
    score = 98.5

    logger.info("1) 参数化日志：user=%s age=%d score=%.1f", user, age, score)

    # 不推荐：提前拼好字符串（会失去延迟格式化的好处）
    logger.info("2) f-string（不推荐在热路径滥用）：user=%s", f"user={user} age={age} score={score}")

    # 结构化字段通常推荐走 JSON（见 12），这里仅演示可读格式
    logger.info("3) key=value style: user=%s age=%d score=%.1f", user, age, score)


if __name__ == "__main__":
    main()

