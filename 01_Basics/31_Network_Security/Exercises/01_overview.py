#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: Network and Security basics.
Author: Lambert

Run:
    python3 01_Basics/31_Network_Security/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_parse_query_params.py", "Parse query params"),
    ("03_build_query_url.py", "Build URL with query"),
    ("04_hash_password.py", "Compute sha256"),
    ("05_hmac_verify.py", "Verify HMAC"),
    ("06_https_client.py", "HTTPS client with SSL wrapped socket"),
    ("07_selectors_server.py", "Echo server using selectors"),
    ("08_socketserver_handler.py", "TCP server using socketserver"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"Directory: {here}")
    print("Exercise files:")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()