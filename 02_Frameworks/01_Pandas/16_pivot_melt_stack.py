#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：透视与重塑（pivot/melt/stack/unstack）。

运行：
    python3 02_Frameworks/01_Pandas/16_pivot_melt_stack.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    data = pd.DataFrame(
        {
            "name": ["Alice", "Alice", "Bob", "Bob"],
            "subject": ["math", "english", "math", "english"],
            "score": [88, 92, 75, 81],
        }
    )

    print("pivot_table ->")
    wide = data.pivot_table(index="name", columns="subject", values="score")
    print(wide)

    print("\nmelt ->")
    long = wide.reset_index().melt(id_vars="name", var_name="subject", value_name="score")
    print(long)

    print("\nstack/unstack ->")
    stacked = wide.stack()
    print(stacked)
    print(stacked.unstack())


if __name__ == "__main__":
    main()
