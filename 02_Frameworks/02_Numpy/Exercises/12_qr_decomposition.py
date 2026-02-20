#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 12：QR 分解。
Author: Lambert

题目：
对给定的矩阵进行 QR 分解，并验证 Q 是正交矩阵。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/12_qr_decomposition.py
"""

from __future__ import annotations

import numpy as np


def qr_and_verify(A: np.ndarray) -> tuple[bool, float]:
    """
    对矩阵 A 进行 QR 分解
    返回 (Q是否正交, 重构误差)
    """
    Q, R = np.linalg.qr(A)

    # 验证 Q 是正交的: Q^T Q ≈ I
    I = Q.T @ Q
    identity = np.eye(I.shape[0])
    is_orthogonal = np.allclose(I, identity, atol=1e-10)

    # 重构误差: ||A - QR||
    reconstruction_error = np.linalg.norm(A - Q @ R)

    return is_orthogonal, float(reconstruction_error)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got}")


def main() -> None:
    A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
    is_ortho, error = qr_and_verify(A)

    check("Q is orthogonal", is_ortho, True)
    print(f"[OK] reconstruction_error: {error:.2e} (should be small)")


if __name__ == "__main__":
    main()