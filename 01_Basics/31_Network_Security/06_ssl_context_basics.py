#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: SSL context basics.

Run:
    python3 01_Basics/31_Network_Security/06_ssl_context_basics.py
"""

import ssl


def main() -> None:
    ctx = ssl.create_default_context()
    print("check_hostname ->", ctx.check_hostname)
    print("verify_mode ->", ctx.verify_mode)
    print("cafile ->", ctx.get_ca_certs()[:1])


if __name__ == "__main__":
    main()
