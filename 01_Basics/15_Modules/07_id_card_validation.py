#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：身份证号校验（中国大陆 18 位二代证）。
Author: Lambert

校验步骤：
- 长度与格式：17 位数字 + 1 位校验码（数字或 X/x）
- 出生日期字段合法（YYYYMMDD）
- 校验码算法：加权求和取模 11
"""

from __future__ import annotations

import datetime as dt
from typing import Iterable, Tuple


WEIGHTS: tuple[int, ...] = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
CHECKMAP: tuple[str, ...] = ("1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2")


def calc_checksum(number17: str) -> str:
    """根据前 17 位计算校验码。"""
    total = sum(int(n) * w for n, w in zip(number17, WEIGHTS))
    return CHECKMAP[total % 11]


def valid_date(yyyymmdd: str) -> bool:
    """校验出生日期字段。"""
    try:
        dt.datetime.strptime(yyyymmdd, "%Y%m%d")
    except ValueError:
        return False
    return True


def validate_id(id_number: str) -> Tuple[bool, str]:
    if len(id_number) != 18:
        return False, "长度必须为 18 位"
    prefix, checksum = id_number[:17], id_number[17].upper()
    if not prefix.isdigit():
        return False, "前 17 位必须为数字"
    if not (checksum.isdigit() or checksum == "X"):
        return False, "最后一位必须是数字或 X"

    birth = prefix[6:14]
    if not valid_date(birth):
        return False, "出生日期字段非法"

    expected = calc_checksum(prefix)
    if checksum != expected:
        return False, f"校验码不匹配，应为 {expected}"

    return True, "校验通过"


def main() -> None:
    samples = [
        "11010519491231002X",  # 官方示例
        "110105194912310021",  # 校验码错
        "12345678901234567X",  # 日期错
        "11010519490229002X",  # 非法日期（非闰年 2 月 29）
    ]
    for s in samples:
        ok, msg = validate_id(s)
        print(f"{s} -> {ok}: {msg}")


if __name__ == "__main__":
    main()