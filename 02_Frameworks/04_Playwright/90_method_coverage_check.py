#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 90：方法覆盖检查脚本（04_Playwright vs third_party_refs）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/90_method_coverage_check.py
"""

from __future__ import annotations

import ast
from collections import Counter, defaultdict
from pathlib import Path


CHAPTER_ROOT = Path("02_Frameworks/04_Playwright")
REFERENCE_ROOT = Path("third_party_refs/playwright-python/tests")

TARGET_RECEIVERS = {
    "page",
    "context",
    "browser",
    "locator",
    "route",
    "request",
    "response",
    "frame",
    "dialog",
    "download",
    "video",
    "clock",
    "keyboard",
    "mouse",
    "tracing",
    "expect",
    "playwright",
}

STRICT_TARGET_RECEIVERS = {
    "page",
    "context",
    "browser",
    "locator",
    "route",
    "request",
    "response",
    "frame",
    "dialog",
    "download",
    "video",
    "clock",
    "keyboard",
    "mouse",
    "tracing",
    "expect",
    "playwright",
    "chromium",
    "firefox",
    "webkit",
    "browser_type",
    "request_context",
    "new_page",
    "popup",
}

# 来自官网 Writing tests/Library 入门高频方法（用于“是否漏掉关键 API”检查）。
CORE_METHODS = {
    "goto",
    "get_by_role",
    "locator",
    "click",
    "fill",
    "check",
    "uncheck",
    "hover",
    "focus",
    "press",
    "set_input_files",
    "select_option",
    "to_have_title",
    "to_have_url",
    "to_be_visible",
    "to_be_checked",
    "to_be_enabled",
    "to_contain_text",
    "to_have_attribute",
    "to_have_count",
    "to_have_text",
    "to_have_value",
    "expect_request",
    "expect_response",
    "wait_for_url",
    "route",
    "fulfill",
    "abort",
    "continue_",
    "fallback",
    "new_context",
    "new_page",
    "clear_cookies",
    "unroute",
    "type",
    "down",
    "up",
    "insert_text",
    "move",
    "dblclick",
    "wheel",
}


def scan_calls(
    root: Path,
    skip_name: str | None = None,
) -> tuple[set[str], dict[str, set[str]], Counter[str]]:
    attrs: set[str] = set()
    recv_methods: dict[str, set[str]] = defaultdict(set)
    recv_method_counter: Counter[str] = Counter()

    for py_file in sorted(root.rglob("*.py")):
        if skip_name and py_file.name == skip_name:
            continue
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if not isinstance(node.func, ast.Attribute):
                continue

            method = node.func.attr
            attrs.add(method)

            recv = None
            value = node.func.value
            if isinstance(value, ast.Name):
                recv = value.id
            elif isinstance(value, ast.Attribute):
                recv = value.attr

            if recv in TARGET_RECEIVERS:
                recv_methods[recv].add(method)
                recv_method_counter[f"{recv}.{method}"] += 1

    return attrs, recv_methods, recv_method_counter


def scan_strict_ref_methods(root: Path) -> set[str]:
    methods: set[str] = set()
    for py_file in sorted(root.rglob("*.py")):
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if not isinstance(node.func, ast.Attribute):
                continue

            value = node.func.value
            recv = None
            if isinstance(value, ast.Name):
                recv = value.id
            elif isinstance(value, ast.Attribute):
                recv = value.attr

            if recv in STRICT_TARGET_RECEIVERS:
                methods.add(node.func.attr)
    return methods


def main() -> None:
    if not CHAPTER_ROOT.exists():
        print("未找到目录：", CHAPTER_ROOT)
        return
    if not REFERENCE_ROOT.exists():
        print("未找到目录：", REFERENCE_ROOT)
        return

    # 跳过工具文件和静态 API 目录文件
    SKIP_FILES = {
        Path(__file__).name,
        "99_api_surface_full_catalog.py",
        "01_overview.py",
        "02_install_and_version.py",
        "13_chapter_summary.py",
        "30_codegen_and_debug_commands.py",
        "31_todomvc_reference_walkthrough.py",
        "32_chapter_summary.py",
        "39_methods_coverage_summary.py",
        "40_methods_coverage_summary.py",
    }
    chapter_attrs, chapter_recv_methods, _ = scan_calls(
        CHAPTER_ROOT, skip_name=None
    )
    # 手动过滤跳过的文件
    for skip_file in SKIP_FILES:
        full_path = CHAPTER_ROOT / skip_file
        if full_path.exists():
            skip_attrs, _, _ = scan_calls(full_path)
            chapter_attrs -= skip_attrs
    ref_attrs, ref_recv_methods, ref_counter = scan_calls(REFERENCE_ROOT)

    print("== 04_Playwright 方法覆盖检查 ==\n")
    print("章节方法总数（按属性名去重）->", len(chapter_attrs))
    print("参考方法总数（按属性名去重）->", len(ref_attrs))

    covered_core = sorted(CORE_METHODS & chapter_attrs)
    missing_core = sorted(CORE_METHODS - chapter_attrs)
    print("\n[1] 官网入门高频方法覆盖")
    print(f"- 覆盖: {len(covered_core)}/{len(CORE_METHODS)}")
    if missing_core:
        print("- 缺失:")
        for m in missing_core:
            print("  -", m)
    else:
        print("- 结论: 高频方法已覆盖")

    strict_ref_methods = scan_strict_ref_methods(REFERENCE_ROOT)
    strict_missing = sorted(strict_ref_methods - chapter_attrs)
    print("\n[2] third_party 严格方法集合覆盖（方法名维度）")
    print(f"- 覆盖: {len(strict_ref_methods) - len(strict_missing)}/{len(strict_ref_methods)}")
    if strict_missing:
        print("- 缺失:")
        for method in strict_missing[:30]:
            print("  -", method)
    else:
        print("- 结论: strict 方法集合已全覆盖")

    print("\n[3] 与 third_party 粗粒度对照（按接收者变量名）")
    key_receivers = [
        "page",
        "context",
        "route",
        "request",
        "response",
        "keyboard",
        "mouse",
        "locator",
        "frame",
    ]
    for recv in key_receivers:
        ref_set = ref_recv_methods.get(recv, set())
        if not ref_set:
            continue
        mine_set = chapter_recv_methods.get(recv, set())
        missing = sorted(ref_set - mine_set)
        print(
            f"- {recv}: ref={len(ref_set)} mine={len(mine_set)} missing={len(missing)}"
        )
        if missing:
            print("  top:", ", ".join(missing[:12]))

    print("\n[4] third_party 高频调用但章节未出现（前 20）")
    missing_rank: list[tuple[str, int]] = []
    for recv_method, cnt in ref_counter.items():
        _, method = recv_method.split(".", 1)
        if method not in chapter_attrs:
            missing_rank.append((recv_method, cnt))
    missing_rank.sort(key=lambda x: (-x[1], x[0]))

    if not missing_rank:
        print("- 无")
    else:
        for recv_method, cnt in missing_rank[:20]:
            print(f"- {recv_method}: {cnt}")

    print("\n提示：")
    print("- [3] 是变量名级别的粗粒度分析，不等价于完整 API 覆盖证明。")
    print("- 方法名维度是否全覆盖，请看 [2]。")


if __name__ == "__main__":
    main()
