#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: Verify HMAC.

Task:
Implement sign(secret, message) -> str and verify(secret, message, sig) -> bool.

Run:
    python3 01_Basics/31_Network_Security/Exercises/05_hmac_verify.py
"""

import hashlib
import hmac


def sign(secret: bytes, message: bytes) -> str:
    return hmac.new(secret, message, hashlib.sha256).hexdigest()


def verify(secret: bytes, message: bytes, sig: str) -> bool:
    expected = sign(secret, message)
    return hmac.compare_digest(expected, sig)


def main() -> None:
    secret = b"key"
    msg = b"data"
    sig = sign(secret, msg)
    print("verify ->", verify(secret, msg, sig))
    print("verify bad ->", verify(secret, msg, sig + "x"))


if __name__ == "__main__":
    main()
