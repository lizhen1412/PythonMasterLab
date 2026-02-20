#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: signal handlers and atexit hooks.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/05_signal_and_atexit.py
"""

import atexit
import signal


def on_exit() -> None:
    print("atexit: cleanup")


def handle_sigint(signum: int, _frame) -> None:
    print(f"signal handler called: {signum}")


def main() -> None:
    atexit.register(on_exit)
    signal.signal(signal.SIGINT, handle_sigint)

    print("simulate handler call")
    handle_sigint(signal.SIGINT, None)


if __name__ == "__main__":
    main()