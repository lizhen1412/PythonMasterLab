#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：是否能“枚举出全部内容”？
Author: Lambert

结论：可以（在当前仓库结构下“很可靠”）。

题目：
1) 扫描 `01_Basics/` 下的章节目录（形如 `NN_Title/`），按数字前缀排序
2) 对每个章节，读取 `01_overview.py`，解析常量 `TOPICS = [(filename, desc), ...]`
3) 要求“不 import 章节代码”（避免副作用），用 AST + `ast.literal_eval()` 安全读取
4) 打印每章脚本清单，并标记 `OK/MISSING`，最后汇总统计

参考答案：
- 本文件即为参考实现；直接运行会输出枚举结果与统计。

运行：
    python3 01_Basics/08_Exercises/02_enumerate_all_lessons.py
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Chapter:
    name: str
    path: Path
    overview_path: Path | None
    topics: list[tuple[str, str]] | None


def _find_topics_node(module: ast.Module) -> ast.AST | None:
    for node in module.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == "TOPICS":
            return node.value
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "TOPICS":
                    return node.value
    return None


def load_topics_from_overview(overview_path: Path) -> list[tuple[str, str]] | None:
    try:
        source = overview_path.read_text(encoding="utf-8")
    except OSError:
        return None

    try:
        module = ast.parse(source, filename=str(overview_path))
    except SyntaxError:
        return None

    topics_node = _find_topics_node(module)
    if topics_node is None:
        return None

    try:
        topics = ast.literal_eval(topics_node)
    except ValueError:
        return None

    if not isinstance(topics, list):
        return None
    normalized: list[tuple[str, str]] = []
    for item in topics:
        if (
            isinstance(item, tuple)
            and len(item) == 2
            and isinstance(item[0], str)
            and isinstance(item[1], str)
        ):
            normalized.append((item[0], item[1]))
    return normalized or None


def find_chapters(basics_dir: Path) -> list[Chapter]:
    chapter_dirs = [
        p
        for p in basics_dir.iterdir()
        if p.is_dir() and re.match(r"^\d{2}_[A-Za-z0-9_]+$", p.name)
    ]
    chapters: list[Chapter] = []
    for chapter_dir in sorted(chapter_dirs, key=lambda p: p.name):
        overview_path = chapter_dir / "01_overview.py"
        topics = load_topics_from_overview(overview_path) if overview_path.exists() else None
        chapters.append(
            Chapter(
                name=chapter_dir.name,
                path=chapter_dir,
                overview_path=overview_path if overview_path.exists() else None,
                topics=topics,
            )
        )
    return chapters


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    basics_dir = repo_root / "01_Basics"
    if not basics_dir.exists():
        raise SystemExit(f"未找到目录: {basics_dir}")

    chapters = find_chapters(basics_dir)
    total_files = 0
    print(f"扫描目录: {basics_dir}")
    print()

    for chapter in chapters:
        if chapter.topics is None:
            print(f"- {chapter.name}: 未解析到 TOPICS（或缺少 01_overview.py）")
            continue

        total_files += len(chapter.topics)
        print(f"- {chapter.name}: {len(chapter.topics)} 个脚本")
        for filename, desc in chapter.topics:
            exists = (chapter.path / filename).exists()
            marker = "OK" if exists else "MISSING"
            print(f"  - {marker} {filename}: {desc}")
        print()

    print(f"章节数: {len(chapters)}")
    print(f"脚本总数（按 TOPICS 统计）: {total_files}")


if __name__ == "__main__":
    main()