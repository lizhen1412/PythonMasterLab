#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 58：Special I/O Formats - 特殊 I/O 格式。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/58_special_io_formats.py

本节补充一些特殊但有用的 I/O 格式，这些格式在特定场景中非常重要。

本节演示：
1. HDF5 格式 (h5py/pytables)
2. XML 格式 (lxml)
3. Clipboard 剪贴板操作
4. ExcelWriter 高级用法
5. SAS 格式详解
6. 格式选择建议
"""

from __future__ import annotations

import pandas as pd
import numpy as np
import os


def main() -> None:
    print("=" * 60)
    print("1. HDF5 格式")
    print("=" * 60)

    print("\nHDF5 特点:")
    print("  - 分层存储格式，适合大量数据")
    print("  - 支持压缩和分块存储")
    print("  - 需要安装 tables 或 pyarrow")
    print("  - 适合：无法全部装入内存的大数据集")

    # 检查依赖
    try:
        import tables
        hdf5_available = True
    except ImportError:
        hdf5_available = False
        print("\n注意: tables 未安装")
        print("安装命令: pip install tables")

    # 检查 pyarrow
    try:
        import pyarrow as pa
        pyarrow_hdf5_available = True
    except ImportError:
        pyarrow_hdf5_available = False
        print("\n注意: pyarrow 未安装")
        print("安装命令: pip install pyarrow")

    df = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=100),
        'category': np.random.choice(['A', 'B', 'C'], 100),
        'value': np.random.randn(100).cumsum(),
        'volume': np.random.randint(1000, 10000, 100)
    })

    print(f"\n示例数据: {len(df)} 行")

    if hdf5_available or pyarrow_hdf5_available:
        hdf_file = '/tmp/data.h5'

        # 使用 HDFStore
        try:
            store = pd.HDFStore(hdf_file)
            print(f"\n创建 HDFStore: {hdf_file}")

            # 存储数据
            store.put('data', df, format='table')
            print(f"数据已存储到 'data' 键")

            # 读取数据
            df_read = store['data']
            print(f"读取成功: {len(df_read)} 行")

            # 追加数据
            df_append = pd.DataFrame({
                'date': pd.date_range('2024-04-11', periods=50),
                'category': np.random.choice(['A', 'B', 'C'], 50),
                'value': np.random.randn(50).cumsum(),
                'volume': np.random.randint(1000, 10000, 50)
            })
            store.append('data', df_append, format='table')
            print(f"追加后: {len(store['data'])} 行")

            # 查询存储的数据
            print(f"\n查询 category='A' 的数据:")
            result = store.select('data', "category = 'A'", stop=5)
            print(result)

            # 列出所有键
            print(f"\nHDFStore 中的键: {store.keys()}")

            store.close()

            # 清理
            os.remove(hdf_file)

        except Exception as e:
            print(f"\nHDFStore 操作失败: {e}")

        # 使用 read_hdf / to_hdf
        print(f"\n使用 read_hdf / to_hdf:")
        try:
            hdf_file2 = '/tmp/data2.h5'
            df.to_hdf(hdf_file2, key='data', mode='w')
            print(f"写入成功")

            df_read2 = pd.read_hdf(hdf_file2, key='data')
            print(f"读取成功: {len(df_read2)} 行")

            os.remove(hdf_file2)

        except Exception as e:
            print(f"read_hdf/to_hdf 失败: {e}")

    print("\n" + "=" * 60)
    print("2. XML 格式")
    print("=" * 60)

    print("\nXML 特点:")
    print("  - 常用于企业数据交换")
    print("  - 需要安装 lxml")
    print("  - 支持 XPath 查询")

    # 检查依赖
    try:
        from lxml import etree
        xml_available = True
    except ImportError:
        xml_available = False
        print("\n注意: lxml 未安装")
        print("安装命令: pip install lxml")

    df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'score': [85, 92, 78]
    })

    print(f"\n示例数据:")
    print(df)

    if xml_available:
        xml_file = '/tmp/data.xml'

        # 写入 XML
        try:
            df.to_xml(xml_file, index=False, root_name='data', row_name='record')
            print(f"\n写入 XML: {xml_file}")

            # 读取 XML
            df_read = pd.read_xml(xml_file, xpath='.//record')
            print(f"\n读取成功:")
            print(df_read)

            # 使用 XPath
            print(f"\n使用 XPath 查询:")
            df_xpath = pd.read_xml(xml_file, xpath='.//record[score>80]')
            print(df_xpath)

            # 清理
            os.remove(xml_file)

        except Exception as e:
            print(f"\nXML 操作失败: {e}")

    print("\n" + "=" * 60)
    print("3. Clipboard 剪贴板操作")
    print("=" * 60)

    print("\n剪贴板操作说明:")
    print("  - 适合与 Excel/电子表格交互")
    print("  - 跨平台支持（需要 pyperclip 或 xclip/clipcopy）")
    print("  - 在 Jupyter 中可直接使用")

    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

    print(f"\n示例数据:")
    print(df)

    print("\n剪贴板方法:")
    print("  df.to_clipboard()           # 复制到剪贴板")
    print("  pd.read_clipboard()         # 从剪贴板读取")

    print("\n注意:")
    print("  - 需要 GUI 环境（非 SSH 纯终端）")
    print("  - Jupyter Notebook 中可直接使用")
    print("  - 本地脚本可能需要安装 pyperclip")

    # 参数说明
    print("\nto_clipboard 参数:")
    print("  excel=True   # 兼容 Excel 格式")
    print("  sep=','      # 使用分隔符")

    print("\nread_clipboard 参数:")
    print("  sep=None     # 自动检测分隔符")
    print("  header=0     # 假设有标题行")

    print("\n" + "=" * 60)
    print("4. ExcelWriter 高级用法")
    print("=" * 60)

    print("\nExcelWriter 特点:")
    print("  - 写入多个 Sheet")
    print("  - 使用不同的引擎")
    print("  - 附加到现有文件")

    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
    df3 = pd.DataFrame({'E': [13, 14, 15], 'F': [16, 17, 18]})

    excel_file = '/tmp/multi_sheet.xlsx'

    try:
        # 创建 ExcelWriter
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            df1.to_excel(writer, sheet_name='Sheet1', index=False)
            df2.to_excel(writer, sheet_name='Sheet2', index=False)
            df3.to_excel(writer, sheet_name='Sheet3', index=False)

        print(f"\n写入多个 Sheet 到: {excel_file}")

        # 读取所有 Sheet
        excel_file_dict = pd.ExcelFile(excel_file)
        print(f"\n文件中的 Sheet: {excel_file_dict.sheet_names}")

        for sheet in excel_file_dict.sheet_names:
            df_read = pd.read_excel(excel_file, sheet_name=sheet)
            print(f"\n{sheet}:")
            print(df_read)

        # 追加到现有文件
        print(f"\n追加 Sheet 到现有文件:")
        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
            df_new = pd.DataFrame({'G': [19, 20, 21], 'H': [22, 23, 24]})
            df_new.to_excel(writer, sheet_name='Sheet4', index=False)

        excel_file_dict2 = pd.ExcelFile(excel_file)
        print(f"\n追加后的 Sheet: {excel_file_dict2.sheet_names}")

        # 清理
        os.remove(excel_file)

    except Exception as e:
        print(f"\nExcelWriter 操作失败: {e}")
        print("可能需要安装: pip install openpyxl")

    print("\n" + "=" * 60)
    print("5. SAS 格式详解")
    print("=" * 60)

    print("\nSAS (Statistical Analysis System) 格式:")
    print("  - .sas7bdat: SAS 7+ 数据文件")
    print("  - .xpt: 传输文件（更通用）")

    print("\nSAS 文件通常用于:")
    print("  - 临床试验数据")
    print("  - 金融行业数据交换")
    print("  - 与 SAS 系统交互")

    # 注意: 这里只是演示，不创建实际 SAS 文件
    print("\nSAS 文件操作:")
    print("  pd.read_sas('data.sas7bdat')     # 读取 SAS7BDAT")
    print("  pd.read_sas('data.xpt')           # 读取 XPORT")
    print("  df.to_sas('data.xpt')             # 写入 XPORT")

    print("\n注意:")
    print("  - SAS7BDAT 格式是专有的，读取受限")
    print("  - XPORT 格式是开放的，推荐使用")
    print("  - 写入 SAS 格式通常只支持 XPORT")

    print("\n与 Stata 对比:")
    print("  Stata: 社会科学研究常用")
    print("  SAS: 企业级、医疗、金融常用")

    print("\n" + "=" * 60)
    print("6. SPSS 格式")
    print("=" * 60)

    print("\nSPSS 格式说明:")
    print("  - .sav: SPSS 数据文件")
    print("  - .zsav: 压缩的 SPSS 文件")
    print("  - 需要 pyreadstat 或 savReader")

    print("\n读取 SPSS 文件:")
    print("  try:")
    print("      import pyreadstat")
    print("      df = pyreadstat.read_sav('data.sav')")
    print("  except ImportError:")
    print("      # 需要安装: pip install pyreadstat")

    print("\n替代方案:")
    print("  - 使用 SPSS 导出为 CSV/Excel")
    print("  - 使用 Haven 包（R）转换")

    print("\n" + "=" * 60)
    print("7. Google Sheets")
    print("=" * 60)

    print("\nGoogle Sheets 集成:")
    print("  - 需要 gspread 库")
    print("  - 需要 Google Cloud 凭证")

    print("\n基本操作:")
    print("  import gspread")
    print("  gc = gspread.service_account()")
    print("  sh = gc.open('SheetName')")
    print("  df = pd.DataFrame(sh.get_all_records())")

    print("\n写入 Google Sheets:")
    print("  sh.update([df.columns.tolist()] + df.values.tolist())")

    print("\n安装:")
    print("  pip install gspread oauth2client")

    print("\n注意:")
    print("  - 需要配置 Google Cloud 项目")
    print("  - 需要启用 Google Sheets API")
    print("  - 需要创建服务账号密钥")

    print("\n" + "=" * 60)
    print("8. 实际应用场景")
    print("=" * 60)

    print("\n场景1: 大数据存储")
    print("-" * 40)
    print("对于无法全部装入内存的数据:")
    print("  1. 使用 HDFStore 分块存储")
    print("  2. 使用 HDFStore 的查询功能")
    print("  3. 使用 chunksize 参数逐块处理")

    print("\n示例:")
    print("  with pd.HDFStore('large.h5') as store:")
    print("      for chunk in pd.read_csv('large.csv', chunksize=10000):")
    print("          store.append('data', chunk)")

    print("\n场景2: 企业数据交换")
    print("-" * 40)
    print("  格式选择指南:")
    print("  - 与 Excel 用户: Excel 或 CSV")
    print("  - 与 Web 系统: JSON 或 XML")
    print("  - 与 SAS 用户: XPORT 或 CSV")
    print("  - 存档/备份: Parquet 或 HDF5")
    print("  - 快速临时: Feather 或 Pickle")

    print("\n场景3: 报表自动化")
    print("-" * 40)
    print("  使用 ExcelWriter 生成多 Sheet 报表:")
    print("  with pd.ExcelWriter('report.xlsx') as writer:")
    print("      summary.to_excel(writer, sheet_name='Summary')")
    print("      details.to_excel(writer, sheet_name='Details')")
    print("      charts.to_excel(writer, sheet_name='Charts')")

    print("\n场景4: 数据交互")
    print("-" * 40)
    print("  快速复制数据到 Excel:")
    print("  df.to_clipboard()  # 在 Excel 中粘贴")
    print("")
    print("  从 Excel 复制数据:")
    print("  df = pd.read_clipboard()")

    print("\n" + "=" * 60)
    print("9. 格式对比总结")
    print("=" * 60)

    print("\n┌──────────────┬──────────┬──────────┬─────────┬────────────┐")
    print("│ 格式         │ 速度     │ 压缩率   │ 兼容性  │ 适用场景   │")
    print("├──────────────┼──────────┼──────────┼─────────┼────────────┤")
    print("│ CSV          │ ★★☆      │ ★☆☆      │ ★★★    │ 通用交换   │")
    print("│ Excel        │ ★☆☆      │ ★☆☆      │ ★★★    │ 办公协作   │")
    print("│ JSON         │ ★☆☆      │ ★☆☆      │ ★★★    │ Web API    │")
    print("│ Parquet      │ ★★☆      │ ★★★      │ ★★☆    │ 大数据分析 │")
    print("│ Feather       │ ★★★      │ ★★☆      │ ★★☆    │ 临时存储   │")
    print("│ HDF5         │ ★★☆      │ ★★★      │ ★☆☆    │ 超大数据   │")
    print("│ Pickle       │ ★★★      │ ★★☆      │ ★☆☆    │ Python内部 │")
    print("│ XML          │ ★☆☆      │ ★☆☆      │ ★★☆    │ 企业系统   │")
    print("│ SAS/Stata    │ ★★☆      │ ★★☆      │ ★☆☆    │ 统计软件   │")
    print("│ Clipboard    │ ★★★      │ -         │ ★★★    │ 快速交互   │")
    print("└──────────────┴──────────┴──────────┴─────────┴────────────┘")

    print("\n" + "=" * 60)
    print("10. 速查表")
    print("=" * 60)

    print("\n特殊格式读取:")
    print("  pd.read_hdf('file.h5', 'key')          # HDF5 读取")
    print("  pd.read_xml('file.xml')                # XML 读取")
    print("  pd.read_clipboard()                    # 剪贴板读取")
    print("  pd.read_sas('file.sas7bdat')           # SAS 读取")
    print("  pd.read_sas('file.xpt')                # XPORT 读取")
    print("  pd.read_excel('file.xlsx', sheet_name) # Excel 指定 Sheet")

    print("\n特殊格式写入:")
    print("  df.to_hdf('file.h5', 'key')             # HDF5 写入")
    print("  df.to_xml('file.xml')                  # XML 写入")
    print("  df.to_clipboard()                      # 复制到剪贴板")
    print("  df.to_sas('file.xpt')                  # XPORT 写入")

    print("\nExcelWriter 高级:")
    print("  with pd.ExcelWriter('file.xlsx') as writer:")
    print("      df1.to_excel(writer, sheet='Sheet1')")
    print("      df2.to_excel(writer, sheet='Sheet2')")

    print("\nHDFStore 操作:")
    print("  store = pd.HDFStore('file.h5')")
    print("  store.put('key', df, format='table')")
    print("  store.append('key', new_df)")
    print("  store.select('key', 'condition')")
    print("  store.close()")

    print("\n" + "=" * 60)
    print("11. 依赖安装指南")
    print("=" * 60)

    print("\n特殊格式依赖:")
    print()
    print("  # HDF5")
    print("  pip install tables")
    print("  # 或")
    print("  pip install pyarrow")
    print()
    print("  # XML")
    print("  pip install lxml")
    print()
    print("  # Excel")
    print("  pip install openpyxl      # .xlsx")
    print("  pip install xlrd          # 读取 .xls")
    print("  pip install xlsxwriter    # 写入 .xlsx")
    print()
    print("  # SAS/Stata")
    print("  # 通常是内置支持或通过 pandas")
    print()
    print("  # Clipboard (可选)")
    print("  pip install pyperclip")
    print()
    print("  # SPSS (第三方)")
    print("  pip install pyreadstat")
    print()
    print("  # Google Sheets")
    print("  pip install gspread oauth2client")

    print("\n" + "=" * 60)
    print("12. 最佳实践")
    print("=" * 60)

    print("\n格式选择建议:")
    print()
    print("1. 长期存储:")
    print("   - CSV: 通用、可读")
    print("   - Parquet: 压缩、性能")
    print("   - HDF5: 大数据、分块查询")
    print()
    print("2. 数据交换:")
    print("   - Excel: 非技术人员")
    print("   - JSON: Web API")
    print("   - XML: 企业系统")
    print("   - CSV: 通用格式")
    print()
    print("3. 临时存储:")
    print("   - Feather: 速度优先")
    print("   - Pickle: Python 对象")
    print("   - 剪贴板: 快速复制")
    print()
    print("4. 大数据:")
    print("   - HDF5: 分块存储查询")
    print("   - Parquet: 列式压缩")
    print("   - CSV chunksize: 分块读取")


if __name__ == "__main__":
    main()