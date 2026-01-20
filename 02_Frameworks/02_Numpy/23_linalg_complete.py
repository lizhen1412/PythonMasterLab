#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 23：线性代数全集。

运行：
    python3 02_Frameworks/02_Numpy/23_linalg_complete.py

知识点：
- det - 行列式
- inv - 矩阵逆
- pinv - 伪逆
- matrix_rank - 矩阵秩
- eig / eigh - 特征值/特征向量
- svd - 奇异值分解
- qr - QR分解
- cholesky - Cholesky分解
- lstsq - 最小二乘
- matrix_power - 矩阵幂
- trace - 迹
- norm - 范数（所有类型）
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. 基础矩阵运算")
    print("=" * 70)

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[2, 0], [1, 2]])

    print("A:")
    print(A)
    print("\nB:")
    print(B)

    print("\n1.1 矩阵乘法")
    print("-" * 70)
    print(f"A @ B:\n{A @ B}")
    print(f"np.dot(A, B):\n{np.dot(A, B)}")
    print(f"np.matmul(A, B):\n{np.matmul(A, B)}")

    print("\n1.2 转置")
    print("-" * 70)
    print(f"A.T:\n{A.T}")
    print(f"A.transpose():\n{A.transpose()}")

    print("\n" + "=" * 70)
    print("2. det - 行列式")
    print("=" * 70)

    A = np.array([[1, 2], [3, 4]])
    print(f"A:\n{A}")
    print(f"det(A): {np.linalg.det(A):.2f}")

    print("\n2.1 行列式的几何意义")
    print("-" * 70)
    print(f"det(A) 表示线性变换的缩放因子")
    print(f"det(A) > 0: 保持方向")
    print(f"det(A) < 0: 翻转方向")
    print(f"det(A) = 0: 不可逆（奇异矩阵）")

    print("\n" + "=" * 70)
    print("3. inv - 矩阵逆")
    print("=" * 70)

    A = np.array([[1, 2], [3, 4]])
    print(f"A:\n{A}")

    A_inv = np.linalg.inv(A)
    print(f"\ninv(A):\n{A_inv}")

    print(f"\nA @ inv(A) (应该是单位矩阵):\n{A @ A_inv}")

    print("\n3.1 不可逆矩阵")
    print("-" * 70)
    A_singular = np.array([[1, 2], [2, 4]])
    print(f"A_singular:\n{A_singular}")
    print(f"det(A_singular): {np.linalg.det(A_singular):.2f}")

    try:
        np.linalg.inv(A_singular)
    except np.linalg.LinAlgError as e:
        print(f"inv(A_singular) 错误: {e}")

    print("\n" + "=" * 70)
    print("4. pinv - 伪逆（Moore-Penrose 伪逆）")
    print("=" * 70)

    A = np.array([[1, 2], [2, 4]])  # 奇异矩阵
    print(f"A (奇异矩阵):\n{A}")

    A_pinv = np.linalg.pinv(A)
    print(f"\npinv(A):\n{A_pinv}")

    print(f"\nA @ pinv(A):\n{A @ A_pinv}")
    print(f"pinv(A) @ A:\n{A_pinv @ A}")

    print("\n伪逆的性质:")
    print("- 可以处理奇异矩阵")
    print("- 可以处理非方阵")
    print("- 最小二乘解")

    print("\n" + "=" * 70)
    print("5. matrix_rank - 矩阵秩")
    print("=" * 70)

    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"A:\n{A}")
    print(f"rank(A): {np.linalg.matrix_rank(A)}")

    print("\n5.1 满秩矩阵")
    print("-" * 70)
    B = np.array([[1, 2], [3, 4]])
    print(f"B:\n{B}")
    print(f"rank(B): {np.linalg.matrix_rank(B)}")

    print("\n" + "=" * 70)
    print("6. eig / eigh - 特征值和特征向量")
    print("=" * 70)

    A = np.array([[4, -2], [1, 1]])
    print(f"A:\n{A}")

    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"\neigenvalues (特征值): {eigenvalues}")
    print(f"eigenvectors (特征向量):\n{eigenvectors}")

    print("\n6.1 验证: A @ v = λ @ v")
    print("-" * 70)
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i]
        lambda_v = eigenvalues[i] * v
        Av = A @ v
        print(f"特征值 {i+1}: {eigenvalues[i]:.4f}")
        print(f"  A @ v: {Av}")
        print(f"  λ @ v: {lambda_v}")

    print("\n6.2 eigh - 对称矩阵（更快）")
    print("-" * 70)
    A_sym = np.array([[2, 1], [1, 2]])
    print(f"A_sym (对称矩阵):\n{A_sym}")

    eigenvalues, eigenvectors = np.linalg.eigh(A_sym)
    print(f"\neigenvalues: {eigenvalues}")
    print(f"eigenvectors:\n{eigenvectors}")

    print("\n" + "=" * 70)
    print("7. svd - 奇异值分解")
    print("=" * 70)

    A = np.array([[1, 2], [3, 4], [5, 6]])
    print(f"A:\n{A}")

    U, S, Vt = np.linalg.svd(A)
    print(f"\nU (左奇异向量):\n{U}")
    print(f"\nS (奇异值): {S}")
    print(f"\nVt (右奇异向量转置):\n{Vt}")

    print("\n7.1 重构矩阵")
    print("-" * 70)
    Sigma = np.zeros(A.shape)
    Sigma[:A.shape[1], :A.shape[1]] = np.diag(S)
    A_reconstructed = U @ Sigma @ Vt
    print(f"重构的 A:\n{A_reconstructed}")
    print(f"与原矩阵的差异: {np.max(np.abs(A - A_reconstructed)):.2e}")

    print("\n" + "=" * 70)
    print("8. qr - QR 分解")
    print("=" * 70)

    A = np.array([[1, 2], [3, 4], [5, 6]])
    print(f"A:\n{A}")

    Q, R = np.linalg.qr(A)
    print(f"\nQ (正交矩阵):\n{Q}")
    print(f"\nR (上三角矩阵):\n{R}")
    print(f"\nQ @ R:\n{Q @ R}")

    print("\n8.1 验证正交性")
    print("-" * 70)
    print(f"Q.T @ Q (应该是单位矩阵):\n{Q.T @ Q}")

    print("\n" + "=" * 70)
    print("9. cholesky - Cholesky 分解")
    print("=" * 70)

    A = np.array([[4, 2], [2, 5]])
    print(f"A (正定矩阵):\n{A}")

    L = np.linalg.cholesky(A)
    print(f"\nL (下三角矩阵):\n{L}")
    print(f"L @ L.T:\n{L @ L.T}")

    print("\n9.1 性质")
    print("-" * 70)
    print("Cholesky 分解用于对称正定矩阵")
    print("比通用 LU 分解快约 2 倍")

    print("\n" + "=" * 70)
    print("10. lstsq - 最小二乘解")
    print("=" * 70)

    # Ax = b 的最小二乘解
    A = np.array([[1, 2], [3, 4], [5, 6]])
    b = np.array([3, 7, 11])

    print(f"A:\n{A}")
    print(f"b: {b}")

    x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    print(f"\n最小二乘解 x: {x}")
    print(f"残差平方和: {residuals}")
    print(f"矩阵秩: {rank}")
    print(f"奇异值: {s}")

    print(f"\n验证: A @ x = {A @ x}")

    print("\n" + "=" * 70)
    print("11. matrix_power - 矩阵幂")
    print("=" * 70)

    A = np.array([[1, 2], [3, 4]])
    print(f"A:\n{A}")

    print(f"\nmatrix_power(A, 0) = I:\n{np.linalg.matrix_power(A, 0)}")
    print(f"\nmatrix_power(A, 1) = A:\n{np.linalg.matrix_power(A, 1)}")
    print(f"\nmatrix_power(A, 2):\n{np.linalg.matrix_power(A, 2)}")
    print(f"\nmatrix_power(A, -1) = inv(A):\n{np.linalg.matrix_power(A, -1)}")

    print("\n" + "=" * 70)
    print("12. trace - 矩阵的迹")
    print("=" * 70)

    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"A:\n{A}")
    print(f"trace(A) = {np.trace(A)}")
    print(f"对角线元素之和: 1 + 5 + 9 = 15")

    print("\n迹的性质:")
    print("- trace(AB) = trace(BA)")
    print("- trace(A) = 特征值之和")

    print("\n" + "=" * 70)
    print("13. norm - 范数")
    print("=" * 70)

    v = np.array([3, 4])
    print(f"向量 v: {v}")

    print("\n13.1 向量范数")
    print("-" * 70)
    print(f"norm(v, ord=1) [L1 范数]: {np.linalg.norm(v, ord=1)}")
    print(f"norm(v, ord=2) [L2 范数]: {np.linalg.norm(v, ord=2)}")
    print(f"norm(v) [默认 L2]: {np.linalg.norm(v)}")
    print(f"norm(v, ord=np.inf) [无穷范数]: {np.linalg.norm(v, ord=np.inf)}")

    print("\n13.2 矩阵范数")
    print("-" * 70)
    A = np.array([[1, 2], [3, 4]])
    print(f"A:\n{A}")
    print(f"norm(A, 'fro') [Frobenius 范数]: {np.linalg.norm(A, 'fro'):.4f}")
    print(f"norm(A, ord=1) [列和范数]: {np.linalg.norm(A, ord=1):.4f}")
    print(f"norm(A, ord=np.inf) [行和范数]: {np.linalg.norm(A, ord=np.inf):.4f}")
    print(f"norm(A, ord=2) [谱范数]: {np.linalg.norm(A, ord=2):.4f}")

    print("\n" + "=" * 70)
    print("14. cond - 条件数")
    print("=" * 70)

    A = np.array([[1, 2], [3, 4]])
    print(f"A:\n{A}")
    print(f"cond(A) = {np.linalg.cond(A):.4f}")
    print(f"条件数越大，矩阵越接近奇异")

    print("\n" + "=" * 70)
    print("15. 实际应用示例")
    print("=" * 70)

    # 示例 1: 解线性方程组
    print("\n示例 1: 解 Ax = b")
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])
    x = np.linalg.solve(A, b)
    print(f"A:\n{A}")
    print(f"b: {b}")
    print(f"解 x: {x}")
    print(f"验证: A @ x = {A @ x}")

    # 示例 2: 最小二乘拟合
    print("\n示例 2: 线性回归（最小二乘）")
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.1, 4.0, 5.9, 8.1, 10.2])

    # 构造设计矩阵 [1, x]
    A_design = np.vstack([np.ones_like(x), x]).T
    print(f"设计矩阵:\n{A_design}")

    # 最小二乘求解
    coeffs, _, _, _ = np.linalg.lstsq(A_design, y, rcond=None)
    print(f"拟合系数 [截距, 斜率]: {coeffs}")
    print(f"拟合直线: y = {coeffs[0]:.2f} + {coeffs[1]:.2f}x")

    # 示例 3: 主成分分析（使用 SVD）
    print("\n示例 3: 使用 SVD 进行降维")
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=float)
    print(f"原始数据:\n{data}")

    # 中心化
    data_centered = data - np.mean(data, axis=0)
    U, S, Vt = np.linalg.svd(data_centered)

    print(f"\n奇异值: {S}")
    print(f"第一主成分解释方差: {S[0]**2 / np.sum(S**2) * 100:.1f}%")

    # 示例 4: 求解特征问题
    print("\n示例 4: 协方差矩阵的特征分解")
    X = np.random.randn(100, 3)
    cov_matrix = np.cov(X.T)
    print(f"协方差矩阵:\n{cov_matrix}")

    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    print(f"\n特征值: {eigenvalues}")
    print(f"特征向量（主成分方向）:\n{eigenvectors}")


if __name__ == "__main__":
    main()
