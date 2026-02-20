#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 29：NumPy 线性代数高级操作 (QR分解、Schur分解、广义特征值等)。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/29_linalg_advanced.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=== QR 分解 ===")

    # QR 分解：将矩阵分解为正交矩阵 Q 和上三角矩阵 R
    A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
    Q, R = np.linalg.qr(A)

    print("原始矩阵 A:")
    print(A)
    print("\nQ (正交矩阵):")
    print(Q)
    print("\nR (上三角矩阵):")
    print(R)
    print("\n验证 Q @ R ≈ A:")
    print(Q @ R)

    # 1. QR 分解用于最小二乘
    print("\n=== QR 用于最小二乘 ===")
    # 构造一个超定系统 Ax = b
    A_ls = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
    b_ls = np.array([3, 7, 11])

    # 使用 QR 分解求解
    Q, R = np.linalg.qr(A_ls)
    # Rx = Q^T b
    x = np.linalg.solve(R[:2], Q.T[:2] @ b_ls)
    print("最小二乘解:", x)

    # 2. Schur 分解
    print("\n=== Schur 分解 ===")
    B = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], dtype=float)
    T, Z = np.linalg.schur(B)

    print("原始矩阵 B:")
    print(B)
    print("\nT (Schur 形式，上三角):")
    print(T)
    print("\nZ (Schur 向量):")
    print(Z)
    print("\n验证 Z @ T @ Z^T ≈ B:")
    print(Z @ T @ Z.T)

    # 3. 广义特征值问题
    print("\n=== 广义特征值问题 ===")
    # 求解 A x = λ B x
    A_gen = np.array([[1, 2], [3, 4]], dtype=float)
    B_gen = np.array([[2, 1], [1, 2]], dtype=float)

    eigvals, eigvecs = np.linalg.eig(np.linalg.solve(B_gen, A_gen))
    print("矩阵 A:")
    print(A_gen)
    print("\n矩阵 B:")
    print(B_gen)
    print("\n广义特征值:")
    print(eigvals)
    print("\n广义特征向量:")
    print(eigvecs)

    # 4. 条件数
    print("\n=== 条件数 ===")
    C = np.array([[1, 1000], [0, 1]], dtype=float)
    print("矩阵 C:")
    print(C)
    print("\n条件数 (2-范数):", np.linalg.cond(C))
    print("条件数 (Frobenius 范数):", np.linalg.cond(C, "fro"))
    print("\n条件数越大，矩阵越接近奇异")

    # 5. 矩阵秩
    print("\n=== 矩阵秩 ===")
    D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
    print("矩阵 D:")
    print(D)
    print("矩阵秩:", np.linalg.matrix_rank(D))

    D_full = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
    print("\n单位矩阵秩:", np.linalg.matrix_rank(D_full))

    # 6. 伪逆 (Moore-Penrose)
    print("\n=== 伪逆 ===")
    # 对非方阵或奇异矩阵求伪逆
    E = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
    print("矩阵 E (3x2):")
    print(E)
    print("\n伪逆 E^+ (2x3):")
    E_pinv = np.linalg.pinv(E)
    print(E_pinv)
    print("\n验证 E @ E^+ @ E ≈ E:")
    print(E @ E_pinv @ E)

    # 7. Cholesky 分解
    print("\n=== Cholesky 分解 ===")
    # 对正定矩阵进行分解 A = L L^T
    F = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=float)
    print("正定矩阵 F:")
    print(F)

    try:
        L = np.linalg.cholesky(F)
        print("\nCholesky 分解 L (下三角):")
        print(L)
        print("\n验证 L @ L^T ≈ F:")
        print(L @ L.T)
    except np.linalg.LinAlgError:
        print("矩阵不是正定的，无法进行 Cholesky 分解")

    # 8. 分块矩阵运算
    print("\n=== 分块矩阵 ===")
    A1 = np.array([[1, 2], [3, 4]])
    A2 = np.array([[5, 6], [7, 8]])
    B1 = np.array([[9, 10], [11, 12]])
    B2 = np.array([[13, 14], [15, 16]])

    # 水平和垂直拼接
    top = np.hstack([A1, A2])
    bottom = np.hstack([B1, B2])
    block = np.vstack([top, bottom])
    print("分块矩阵:")
    print(block)

    # 9. Hadamard 积 (逐元素乘积)
    print("\n=== Hadamard 积 ===")
    G = np.array([[1, 2], [3, 4]])
    H = np.array([[5, 6], [7, 8]])
    print("矩阵 G:")
    print(G)
    print("\n矩阵 H:")
    print(H)
    print("\nHadamard 积 (G * H):")
    print(G * H)

    # 10. Kronecker 积
    print("\n=== Kronecker 积 ===")
    I = np.array([[1, 2], [3, 4]])
    J = np.array([[0, 5], [6, 7]])
    print("矩阵 I:")
    print(I)
    print("\n矩阵 J:")
    print(J)
    print("\nKronecker 积 I ⊗ J:")
    print(np.kron(I, J))

    # 11. 矩阵指数和对数
    print("\n=== 矩阵指数和对数 ===")
    K = np.array([[0, -1], [1, 0]], dtype=float)
    print("矩阵 K:")
    print(K)
    print("\n矩阵指数 exp(K):")
    print(np.exp(K))  # 逐元素指数
    print("\n矩阵指数 expm(K) (使用 scipy，如果可用):")
    try:
        from scipy.linalg import expm
        print(expm(K))
    except ImportError:
        print("scipy 未安装，跳过 expm")

    # 12. 张量积
    print("\n=== 张量积 ===")
    # 外积
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    print("向量 v1:", v1)
    print("向量 v2:", v2)
    print("\n外积 v1 ⊗ v2:")
    print(np.outer(v1, v2))

    # 13. 分解汇总
    print("\n=== 分解方法汇总 ===")
    print("- QR 分解: np.linalg.qr()")
    print("- Schur 分解: np.linalg.schur()")
    print("- SVD 分解: np.linalg.svd()")
    print("- 特征值分解: np.linalg.eig()")
    print("- Cholesky 分解: np.linalg.cholesky()")
    print("- 伪逆: np.linalg.pinv()")


if __name__ == "__main__":
    main()