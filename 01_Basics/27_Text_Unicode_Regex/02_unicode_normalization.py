#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: Unicode normalization with unicodedata.

Run:
    python3 01_Basics/27_Text_Unicode_Regex/02_unicode_normalization.py
"""

import unicodedata


def main() -> None:
    composed = "caf\u00e9"
    decomposed = "cafe\u0301"

    print("composed == decomposed ->", composed == decomposed)
    print("len(composed) ->", len(composed))
    print("len(decomposed) ->", len(decomposed))

    nfc_a = unicodedata.normalize("NFC", composed)
    nfc_b = unicodedata.normalize("NFC", decomposed)
    print("NFC equal ->", nfc_a == nfc_b)

    nfd_a = unicodedata.normalize("NFD", composed)
    nfd_b = unicodedata.normalize("NFD", decomposed)
    print("NFD equal ->", nfd_a == nfd_b)


if __name__ == "__main__":
    main()
