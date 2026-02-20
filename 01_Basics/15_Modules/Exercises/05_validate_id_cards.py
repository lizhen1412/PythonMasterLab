#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：批量校验身份证号。
Author: Lambert

要求：
- 复用章节中的 validate_id 函数（动态加载模块）
- 对一组号码输出校验结果
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Callable, Tuple


def load_validator() -> Callable[[str], Tuple[bool, str]]:
    """从章节脚本加载 validate_id 函数。"""
    root = Path(__file__).resolve().parents[2]
    module_path = root / "01_Basics" / "15_Modules" / "07_id_card_validation.py"
    spec = importlib.util.spec_from_file_location("id_card_module", module_path)
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return getattr(module, "validate_id")


def main() -> None:
    validate_id = load_validator()
    samples = [
        "11010519491231002X",
        "110105194912310021",
        "12345678901234567X",
    ]
    for s in samples:
        ok, msg = validate_id(s)
        print(f"{s} -> {ok}: {msg}")


if __name__ == "__main__":
    main()