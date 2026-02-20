#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: HMAC basics.
Author: Lambert

Run:
    python3 01_Basics/31_Network_Security/05_hmac_basics.py
"""

import hmac
import hashlib


def main() -> None:
    secret = b"secret-key"
    message = b"payload"

    sig = hmac.new(secret, message, hashlib.sha256).hexdigest()
    print("signature ->", sig)

    sig2 = hmac.new(secret, message, hashlib.sha256).hexdigest()
    print("verify ->", hmac.compare_digest(sig, sig2))


if __name__ == "__main__":
    main()