#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 26：随机分布。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/26_random_distributions.py

知识点：
- 正态分布/均匀分布
- 泊松分布/二项分布
- 指数分布/贝塔分布
- 多项式分布/多项分布
- 随机状态管理
- permutation / shuffle
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    # 创建随机数生成器
    rng = np.random.default_rng(42)

    print("=" * 70)
    print("1. 均匀分布")
    print("=" * 70)

    print("\n1.1 random - [0, 1) 均匀分布")
    print("-" * 70)
    samples = rng.random(5)
    print(f"random(5): {samples}")

    print("\n1.2 uniform - 指定范围均匀分布")
    print("-" * 70)
    samples = rng.uniform(10, 20, 5)
    print(f"uniform(10, 20, 5): {samples}")

    print("\n1.3 integers - 随机整数")
    print("-" * 70)
    samples = rng.integers(0, 10, 5)
    print(f"integers(0, 10, 5): {samples}")

    print("\n1.4 choice - 从数组随机选择")
    print("-" * 70)
    arr = np.array([10, 20, 30, 40, 50])
    samples = rng.choice(arr, 3)
    print(f"choice({arr}, 3): {samples}")

    print("\n带放回:")
    samples = rng.choice(arr, 5, replace=True)
    print(f"choice({arr}, 5, replace=True): {samples}")

    print("\n不带放回:")
    samples = rng.choice(arr, 3, replace=False)
    print(f"choice({arr}, 3, replace=False): {samples}")

    print("\n加权选择:")
    weights = np.array([0.1, 0.2, 0.3, 0.2, 0.2])
    samples = rng.choice(arr, 5, p=weights)
    print(f"choice({arr}, 5, p={weights}): {samples}")

    print("\n" + "=" * 70)
    print("2. 正态分布（高斯分布）")
    print("=" * 70)

    print("\n2.1 standard_normal - 标准正态分布 N(0, 1)")
    print("-" * 70)
    samples = rng.standard_normal(5)
    print(f"standard_normal(5): {samples}")

    print("\n2.2 normal - 指定均值和标准差")
    print("-" * 70)
    samples = rng.normal(loc=10, scale=2, size=5)
    print(f"normal(loc=10, scale=2, size=5): {samples}")

    print("\n2.3 multivariate_normal - 多元正态分布")
    print("-" * 70)
    mean = [0, 0]
    cov = [[1, 0.5], [0.5, 1]]
    samples = rng.multivariate_normal(mean, cov, 3)
    print(f"multivariate_normal(mean={mean}, cov={cov}, size=3):")
    print(samples)

    print("\n" + "=" * 70)
    print("3. 二项分布")
    print("=" * 70)

    print("\n3.1 binomial - 二项分布")
    print("-" * 70)
    # n 次试验，每次成功概率 p
    samples = rng.binomial(n=10, p=0.5, size=10)
    print(f"binomial(n=10, p=0.5, size=10): {samples}")
    print("（10 次掷硬币，正面朝上的次数）")

    print("\n" + "=" * 70)
    print("4. 泊松分布")
    print("=" * 70)

    print("\n4.1 poisson - 泊松分布")
    print("-" * 70)
    samples = rng.poisson(lam=5, size=10)
    print(f"poisson(lam=5, size=10): {samples}")
    print("（单位时间内事件发生的次数）")

    print("\n" + "=" * 70)
    print("5. 指数分布")
    print("=" * 70)

    print("\n5.1 exponential - 指数分布")
    print("-" * 70)
    samples = rng.exponential(scale=2.0, size=5)
    print(f"exponential(scale=2.0, size=5): {samples}")
    print("（事件之间的等待时间）")

    print("\n" + "=" * 70)
    print("6. 其他常见分布")
    print("=" * 70)

    print("\n6.1 beta - 贝塔分布")
    print("-" * 70)
    samples = rng.beta(a=2, b=5, size=5)
    print(f"beta(a=2, b=5, size=5): {samples}")

    print("\n6.2 gamma - 伽马分布")
    print("-" * 70)
    samples = rng.gamma(shape=2, scale=2, size=5)
    print(f"gamma(shape=2, scale=2, size=5): {samples}")

    print("\n6.3 chisquare - 卡方分布")
    print("-" * 70)
    samples = rng.chisquare(df=3, size=5)
    print(f"chisquare(df=3, size=5): {samples}")

    print("\n6.4 f - F 分布")
    print("-" * 70)
    samples = rng.f(dfn=2, dfd=5, size=5)
    print(f"f(dfn=2, dfd=5, size=5): {samples}")

    print("\n6.5 t - 学生 t 分布")
    print("-" * 70)
    samples = rng.standard_t(df=5, size=5)
    print(f"standard_t(df=5, size=5): {samples}")

    print("\n" + "=" * 70)
    print("7. 排列与洗牌")
    print("=" * 70)

    arr = np.array([1, 2, 3, 4, 5])

    print("\n7.1 permutation - 返回打乱的副本")
    print("-" * 70)
    permuted = rng.permutation(arr)
    print(f"原数组: {arr}")
    print(f"permutation(arr): {permuted}")

    print("\n7.2 shuffle - 就地打乱")
    print("-" * 70)
    arr_copy = arr.copy()
    rng.shuffle(arr_copy)
    print(f"原数组: {arr}")
    print(f"shuffle(arr) 后: {arr_copy}")

    print("\n7.3 permutation 作用于整数")
    print("-" * 70)
    perm = rng.permutation(5)
    print(f"permutation(5): {perm}")
    print("返回 0-4 的随机排列")

    print("\n" + "=" * 70)
    print("8. 随机状态管理")
    print("=" * 70)

    print("\n8.1 设置种子（可重复性）")
    print("-" * 70)
    rng1 = np.random.default_rng(42)
    samples1 = rng1.random(3)

    rng2 = np.random.default_rng(42)
    samples2 = rng2.random(3)

    print(f"rng1(42): {samples1}")
    print(f"rng2(42): {samples2}")
    print(f"相同种子 -> 相同结果")

    print("\n8.2 获取/设置状态")
    print("-" * 70)
    rng = np.random.default_rng(42)
    state = rng.bit_generator.state
    print(f"获取状态: {type(state)}")

    samples1 = rng.random(3)
    print(f"随机数: {samples1}")

    rng.bit_generator.state = state
    samples2 = rng.random(3)
    print(f"恢复状态后: {samples2}")

    print("\n8.3 独立的随机流")
    print("-" * 70)
    seed_sequence = np.random.SeedSequence(42)
    child_seeds = seed_sequence.spawn(3)

    for i, seed in enumerate(child_seeds):
        rng = np.random.default_rng(seed)
        print(f"Stream {i}: {rng.random(3)}")

    print("\n" + "=" * 70)
    print("9. 实际应用示例")
    print("=" * 70)

    # 示例 1: 蒙特卡洛积分
    print("\n示例 1: 蒙特卡洛估算 π")
    N = 10000
    points = rng.random((N, 2)) * 2 - 1  # [-1, 1] × [-1, 1]
    inside = np.sum(points[:, 0]**2 + points[:, 1]**2 <= 1)
    pi_estimate = 4 * inside / N
    print(f"π 的估算值: {pi_estimate:.4f}")
    print(f"实际值: {np.pi:.4f}")

    # 示例 2: 随机漫步
    print("\n示例 2: 一维随机漫步")
    steps = 1000
    # 每步 +1 或 -1
    random_steps = rng.choice([-1, 1], size=steps)
    position = np.cumsum(random_steps)
    print(f"起点: 0")
    print(f"终点: {position[-1]}")
    print(f"最大位置: {position.max()}")
    print(f"最小位置: {position.min()}")

    # 示例 3: 布朗运动
    print("\n示例 3: 二维布朗运动")
    n_steps = 1000
    dt = 0.01
    # 每步的随机位移
    dx = rng.normal(0, np.sqrt(dt), n_steps)
    dy = rng.normal(0, np.sqrt(dt), n_steps)
    # 累积位置
    x = np.cumsum(dx)
    y = np.cumsum(dy)
    print(f"起点: (0, 0)")
    print(f"终点: ({x[-1]:.4f}, {y[-1]:.4f})")
    print(f"距起点距离: {np.sqrt(x[-1]**2 + y[-1]**2):.4f}")

    # 示例 4: 抽样调查
    print("\n示例 4: 从总体中抽样")
    population = np.arange(1, 101)  # 1-100
    sample_size = 10
    sample = rng.choice(population, size=sample_size, replace=False)
    print(f"总体: 1-100")
    print(f"样本 (n={sample_size}): {sample}")
    print(f"样本均值: {np.mean(sample):.2f}")
    print(f"总体均值: 50.50")

    # 示例 5: 伯努利过程
    print("\n示例 5: 伯努利过程（成功/失败）")
    n_trials = 100
    success_prob = 0.3
    outcomes = rng.binomial(n=1, p=success_prob, size=n_trials)
    n_successes = np.sum(outcomes)
    print(f"试验次数: {n_trials}")
    print(f"成功概率: {success_prob}")
    print(f"实际成功次数: {n_successes}")
    print(f"实际成功率: {n_successes / n_trials:.2%}")

    # 示例 6: 指数衰减
    print("\n示例 6: 放射性衰变模拟")
    half_life = 10  # 半衰期
    lambda_decay = np.log(2) / half_life
    n_atoms = 10000
    # 每个原子的衰变时间
    decay_times = rng.exponential(scale=1 / lambda_decay, size=n_atoms)
    # 按时间排序，计算剩余原子数
    time_points = np.arange(0, 50, 5)
    remaining = [np.sum(decay_times > t) for t in time_points]
    print(f"初始原子数: {n_atoms}")
    print(f"半衰期: {half_life}")
    print(f"各时间点剩余原子数:")
    for t, n in zip(time_points, remaining):
        print(f"  t={t}: {n} ({n / n_atoms * 100:.1f}%)")


if __name__ == "__main__":
    main()