#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 21：Financial Functions - 金融函数。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/21_financial.py

NumPy 提供了一套完整的金融计算函数，涵盖货币时间价值、
折旧、债券收益率等常见金融计算。

本节演示：
1. 货币时间价值 (TVM): pv, fv, npv, pmt, ppmt, ipmt, nper, rate
2. 折旧计算
3. 内部收益率 (irr, mirr)
4. 实际应用案例
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. 货币时间价值基础")
    print("=" * 60)

    print("\n关键概念:")
    print("  PV (Present Value): 现值")
    print("  FV (Future Value): 未来值")
    print("  PMT (Payment): 每期支付额")
    print("  NPER (Number of Periods): 期数")
    print("  RATE: 每期利率")

    print("\n基本公式: FV = PV * (1 + r)^n")

    print("\n" + "=" * 60)
    print("2. fv - 计算未来值")
    print("=" * 60)

    # 场景：存入一笔钱，n 年后值多少？
    pv = 10000  # 本金
    rate = 0.05  # 年利率 5%
    nper = 10  # 10 年
    pmt = 0  # 每年不额外存入

    future_value = np.fv(rate, nper, pmt, pv)
    print(f"\n本金: ¥{pv:,.0f}")
    print(f"年利率: {rate*100}%")
    print(f"年数: {nper} 年")
    print(f"10 年后金额: ¥{abs(future_value):,.2f}")

    # 场景：每年定期存款
    pv = 0  # 初始本金
    pmt = -10000  # 每年存入 1 万
    rate = 0.05
    nper = 20

    future_value = np.fv(rate, nper, pmt, pv)
    print(f"\n每年存入: ¥{abs(pmt):,.0f}")
    print(f"年利率: {rate*100}%")
    print(f"年数: {nper} 年")
    print(f"20 年后总额: ¥{abs(future_value):,.2f}")

    print("\n" + "=" * 60)
    print("3. pv - 计算现值")
    print("=" * 60)

    # 场景：未来需要一笔钱，现在需要存多少？
    fv_target = 100000  # 目标 10 万
    rate = 0.05
    nper = 10
    pmt = 0

    present_value = np.pv(rate, nper, pmt, fv_target)
    print(f"\n目标金额: ¥{fv_target:,.0f}")
    print(f"年利率: {rate*100}%")
    print(f"年数: {nper} 年")
    print(f"现在需要存入: ¥{abs(present_value):,.2f}")

    # 场景：年金现值
    pmt = -10000  # 每年收到 1 万，共 10 年
    nper = 10
    rate = 0.05
    fv = 0

    pv_annuity = np.pv(rate, nper, pmt, fv)
    print(f"\n每年收到: ¥{abs(pmt):,.0f}")
    print(f"年数: {nper} 年")
    print(f"年利率: {rate*100}%")
    print(f"这笔年金的现值: ¥{abs(pv_annuity):,.2f}")

    print("\n" + "=" * 60)
    print("4. pmt - 计算每期支付额")
    print("=" * 60)

    # 场景：房贷计算
    pv = 1000000  # 贷款 100 万
    rate = 0.049 / 12  # 月利率（年利率 4.9%）
    nper = 30 * 12  # 30 年 = 360 个月
    fv = 0

    monthly_payment = np.pmt(rate, nper, pv, fv)
    print(f"\n贷款金额: ¥{pv:,.0f}")
    print(f"年利率: 4.9%")
    print(f"贷款年限: 30 年")
    print(f"月供: ¥{abs(monthly_payment):,.2f}")
    print(f"总还款额: ¥{abs(monthly_payment) * nper:,.2f}")
    print(f"总利息: ¥{abs(monthly_payment) * nper - pv:,.2f}")

    # 不同期限的月供对比
    print(f"\n不同贷款期限对比（贷款 ¥{pv:,.0f}，年利率 4.9%）:")
    for years in [10, 20, 30]:
        n = years * 12
        payment = np.pmt(rate, n, pv, 0)
        total = abs(payment) * n
        interest = total - pv
        print(f"  {years:2d} 年: 月供 ¥{abs(payment):,.2f}, "
              f"总利息 ¥{interest:,.2f}")

    print("\n" + "=" * 60)
    print("5. nper - 计算期数")
    print("=" * 60)

    # 场景：每月存钱，多久能达成目标？
    target = 1000000
    pmt = -10000  # 每月存 1 万
    rate = 0.05 / 12  # 月利率
    pv = 0

    months = np.nper(rate, pmt, pv, -target)
    years = months / 12
    print(f"\n目标金额: ¥{target:,.0f}")
    print(f"每月存入: ¥{abs(pmt):,.0f}")
    print(f"年利率: 5%")
    print(f"需要 {months:.1f} 个月 ≈ {years:.1f} 年")

    # 场景：每月还贷，多久还清？
    debt = 500000
    pmt = -10000  # 每月还 1 万
    rate = 0.049 / 12

    months_to_pay = np.nper(rate, pmt, debt, 0)
    print(f"\n债务: ¥{debt:,.0f}")
    print(f"每月还款: ¥{abs(pmt):,.0f}")
    print(f"年利率: 4.9%")
    print(f"需要 {months_to_pay:.1f} 个月 ≈ {months_to_pay/12:.1f} 年还清")

    print("\n" + "=" * 60)
    print("6. rate - 计算利率")
    print("=" * 60)

    # 场景：已知投资和回报，计算收益率
    pv = -10000  # 投资 1 万
    nper = 5  # 5 年后
    pmt = 0
    fv = 15000  # 变成 1.5 万

    annual_rate = np.rate(nper, pmt, pv, fv)
    print(f"\n投资: ¥{abs(pv):,.0f}")
    print(f"{nper} 年后: ¥{fv:,.0f}")
    print(f"年化收益率: {annual_rate*100:.2f}%")

    print("\n" + "=" * 60)
    print("7. ppmt 和 ipmt - 本金与利息分解")
    print("=" * 60)

    # 场景：房贷还款中的本金和利息
    pv = 1000000
    annual_rate = 0.049
    monthly_rate = annual_rate / 12
    years = 30
    nper = years * 12

    print(f"\n贷款: ¥{pv:,.0f}")
    print(f"年利率: {annual_rate*100}%")
    print(f"期限: {years} 年")

    # 查看第 1 期、第 60 期、第 120 期的本金和利息
    for period in [1, 60, 120, 360]:
        principal = np.ppmt(monthly_rate, period, nper, pv)
        interest = np.ipmt(monthly_rate, period, nper, pv)
        total = principal + interest
        print(f"\n第 {period} 期:")
        print(f"  本金: ¥{abs(principal):,.2f}")
        print(f"  利息: ¥{abs(interest):,.2f}")
        print(f"  合计: ¥{abs(total):,.2f}")

    print("\n" + "=" * 60)
    print("8. npv - 净现值")
    print("=" * 60)

    # 场景：投资项目的现金流
    cashflows = [-100000, 30000, 35000, 40000, 45000, 50000]
    discount_rate = 0.08

    print(f"\n折现率: {discount_rate*100}%")
    print("现金流:")
    for i, cf in enumerate(cashflows):
        print(f"  第 {i} 年: ¥{cf:,.0f}")

    npv_value = np.npv(discount_rate, cashflows)
    print(f"\n净现值 (NPV): ¥{npv_value:,.2f}")
    print(f"结论: {'值得投资' if npv_value > 0 else '不值得投资'}")

    # 不同折现率下的 NPV
    print(f"\n不同折现率下的 NPV:")
    for rate in [0.05, 0.08, 0.10, 0.12, 0.15]:
        npv_r = np.npv(rate, cashflows)
        print(f"  {rate*100:.0f}%: ¥{npv_r:,.2f}")

    print("\n" + "=" * 60)
    print("9. irr - 内部收益率")
    print("=" * 60)

    # 场景：计算投资项目的内部收益率
    cashflows = [-100000, 30000, 35000, 40000, 45000, 50000]

    print(f"\n现金流:")
    for i, cf in enumerate(cashflows):
        print(f"  第 {i} 年: ¥{cf:,.0f}")

    irr_value = np.irr(cashflows)
    print(f"\n内部收益率 (IRR): {irr_value*100:.2f}%")

    if irr_value > 0.08:
        print(f"IRR > 8%，值得投资")
    else:
        print(f"IRR < 8%，不值得投资")

    print("\n" + "=" * 60)
    print("10. mirr - 修正内部收益率")
    print("=" * 60)

    # 场景：考虑再投资率和借款率的 IRR
    cashflows = [-100000, 30000, 35000, 40000, 45000, 50000]
    finance_rate = 0.05  # 借款利率
    reinvest_rate = 0.10  # 再投资利率

    print(f"\n现金流:")
    for i, cf in enumerate(cashflows):
        print(f"  第 {i} 年: ¥{cf:,.0f}")

    irr_value = np.irr(cashflows)
    mirr_value = np.mirr(cashflows, finance_rate, reinvest_rate)

    print(f"\n内部收益率 (IRR): {irr_value*100:.2f}%")
    print(f"借款利率: {finance_rate*100:.0f}%")
    print(f"再投资利率: {reinvest_rate*100:.0f}%")
    print(f"修正内部收益率 (MIRR): {mirr_value*100:.2f}%")

    print("\n说明: MIRR 考虑了:")
    print("  - 负现金流的借款成本")
    print("  - 正现金流的再投资收益")

    print("\n" + "=" * 60)
    print("11. 折旧计算")
    print("=" * 60)

    cost = 1000000  # 资产成本
    salvage_value = 100000  # 残值
    useful_life = 5  # 使用年限

    print(f"\n资产信息:")
    print(f"  成本: ¥{cost:,.0f}")
    print(f"  残值: ¥{salvage_value:,.0f}")
    print(f"  使用年限: {useful_life} 年")

    # 直线折旧
    depreciation_sl = (cost - salvage_value) / useful_life
    print(f"\n直线折旧法:")
    print(f"  年折旧额: ¥{depreciation_sl:,.2f}")
    print(f"  年折旧率: {(depreciation_sl/cost)*100:.2f}%")

    # 双倍余额递减法
    print(f"\n双倍余额递减法 (前3年):")
    book_value = cost
    for year in range(1, 4):
        depreciation_dd = book_value * (2 / useful_life)
        depreciation_dd = min(depreciation_dd, book_value - salvage_value)
        book_value -= depreciation_dd
        print(f"  第{year}年折旧: ¥{depreciation_dd:,.2f}, "
              f"账面价值: ¥{book_value:,.2f}")

    print("\n" + "=" * 60)
    print("12. 实际应用案例")
    print("=" * 60)

    print("\n案例1: 退休规划")
    print("-" * 40)
    current_age = 30
    retirement_age = 60
    years_to_retirement = retirement_age - current_age
    monthly_savings = 5000
    expected_return = 0.07

    pv = 0
    pmt = -monthly_savings
    rate = expected_return / 12
    nper = years_to_retirement * 12

    retirement_fund = np.fv(rate, nper, pmt, pv)
    print(f"年龄: {current_age} -> {retirement_age}")
    print(f"每月存入: ¥{monthly_savings:,.0f}")
    print(f"预期年收益: {expected_return*100:.0f}%")
    print(f"退休时可有: ¥{abs(retirement_fund):,.0f}")

    # 退休后每月可领多少（假设发20年）
    retirement_years = 20
    monthly_withdraw = np.pmt(rate, retirement_years * 12, -abs(retirement_fund), 0)
    print(f"退休后每月可领: ¥{abs(monthly_withdraw):,.2f}（发{retirement_years}年）")

    print("\n案例2: 教育金规划")
    print("-" * 40)
    child_age = 5
    college_age = 18
    years_to_college = college_age - child_age
    college_cost = 500000  # 4年大学费用
    inflation = 0.03

    future_cost = college_cost * (1 + inflation) ** years_to_college
    monthly_savings_needed = np.pmt(
        inflation / 12,
        years_to_college * 12,
        0,
        -future_cost
    )

    print(f"孩子年龄: {child_age} 岁")
    print(f"{college_age} 岁上大学（还需 {years_to_college} 年）")
    print(f"当前大学费用: ¥{college_cost:,.0f}")
    print(f"通胀率: {inflation*100:.0f}%")
    print(f"{college_age} 岁时需要: ¥{future_cost:,.2f}")
    print(f"每月需存: ¥{abs(monthly_savings_needed):,.2f}")

    print("\n" + "=" * 60)
    print("13. 金融函数速查")
    print("=" * 60)

    functions = {
        "fv(rate, nper, pmt, pv)": "计算未来值",
        "pv(rate, nper, pmt, fv)": "计算现值",
        "pmt(rate, nper, pv, fv)": "计算每期支付额",
        "nper(rate, pmt, pv, fv)": "计算期数",
        "rate(nper, pmt, pv, fv)": "计算利率",
        "ppmt(rate, per, nper, pv)": "计算某期本金",
        "ipmt(rate, per, nper, pv)": "计算某期利息",
        "npv(rate, values)": "计算净现值",
        "irr(values)": "计算内部收益率",
        "mirr(values, finance_rate, reinvest_rate)": "计算修正内部收益率",
    }

    print("\n常用金融函数:")
    for func, desc in functions.items():
        print(f"  {func:50s} # {desc}")

    print("\n注意事项:")
    print("  - 现金流方向: 用正负号区分流入/流出")
    print("  - 利率期数匹配: 年利率需转换为月利率")
    print("  - 货币时间价值: 今天的 100 元 > 明天的 100 元")


if __name__ == "__main__":
    main()