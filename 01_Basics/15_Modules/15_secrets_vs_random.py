#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：secrets vs random。
Author: Lambert

- `random` 适合模拟/游戏，不适合安全场景
- `secrets` 提供密码学安全随机：token_hex、choice
"""

from __future__ import annotations

import secrets
import string


def insecure_token(length: int = 8) -> str:
    """示范：游戏用随机码（非安全）。"""
    import random

    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))


def secure_token(length_bytes: int = 16) -> str:
    """使用 secrets 生成安全 token。"""
    return secrets.token_hex(length_bytes)


def secure_choice() -> str:
    """从字符集安全选择（如临时密码）。"""
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(12))


def main() -> None:
    print("不安全随机码（random） ->", insecure_token())
    print("安全 token_hex ->", secure_token(8))
    print("安全 choice 生成密码 ->", secure_choice())
    print("提示：涉及安全/令牌/密码请用 secrets 或系统提供的安全随机源。")


if __name__ == "__main__":
    main()