#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：asyncio Subprocess - 子进程管理。
Author: Lambert

本示例演示 asyncio 的子进程管理功能：

1. **asyncio.create_subprocess_exec()** - 执行命令（参数列表）
2. **asyncio.create_subprocess_shell()** - 通过shell执行命令
3. **asyncio.subprocess.Process** - 进程对象
4. **stdout/stderr 处理** - 流重定向
5. **process.communicate()** - 与进程交互
6. **process.wait()** - 等待进程结束
7. **process.kill() / terminate()** - 终止进程
8. **process.pid** - 进程ID
9. **process.returncode** - 退出码

注意：子进程操作与操作系统相关，部分功能在Windows上可能不可用。
"""

from __future__ import annotations

import asyncio
import sys
import signal
from typing import Any


# =============================================================================
# create_subprocess_exec - 执行命令
# =============================================================================


async def demo_subprocess_exec() -> None:
    """示例 01：create_subprocess_exec - 直接执行命令。"""
    print("== asyncio.create_subprocess_exec() ==\n")

    # 执行命令（不通过shell）
    proc = await asyncio.create_subprocess_exec(
        'echo', 'Hello from subprocess',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    print(f"进程已启动")
    print(f"  PID: {proc.pid}")
    print(f"  命令: echo Hello from subprocess")

    # 等待进程完成
    stdout, stderr = await proc.communicate()

    print(f"\n进程输出:")
    print(f"  stdout: {stdout.decode().strip()}")
    print(f"  stderr: {stderr.decode().strip() if stderr else '(empty)'}")
    print(f"  返回码: {proc.returncode}")


# =============================================================================
# create_subprocess_shell - 通过shell执行
# =============================================================================


async def demo_subprocess_shell() -> None:
    """示例 02：create_subprocess_shell - 通过shell执行。"""
    print("\n\n== asyncio.create_subprocess_shell() ==\n")

    # 通过shell执行命令（支持shell特性）
    proc = await asyncio.create_subprocess_shell(
        'echo "Hello from shell" && sleep 0.1 && echo "Done"',
        stdout=asyncio.subprocess.PIPE,
    )

    print(f"Shell命令已启动")

    # 读取输出
    stdout, _ = await proc.communicate()

    print(f"\n输出:")
    print(f"  {stdout.decode().strip()}")
    print(f"  返回码: {proc.returncode}")

    print("\nshell vs exec:")
    print("  shell: 支持 shell 特性（管道、重定向、变量等）")
    print("  exec:  直接执行，更安全（避免shell注入）")


# =============================================================================
# 进程交互
# =============================================================================


async def demo_process_communicate() -> None:
    """示例 03：communicate() - 与进程交互。"""
    print("\n\n== process.communicate() - 进程交互 ==\n")

    # 创建一个需要输入的进程
    proc = await asyncio.create_subprocess_exec(
        'python3', '-c',
        '''
import sys
print("Enter your name:")
name = sys.stdin.readline().strip()
print(f"Hello, {name}!")
print("Enter your age:")
age = sys.stdin.readline().strip()
print(f"You are {age} years old.")
        ''',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    print(f"进程已启动")

    # 与进程交互
    # communicate() 会发送输入并等待进程结束
    stdout, stderr = await proc.communicate(
        input=b'Alice\n25\n'
    )

    print(f"\n进程输出:")
    print(f"--- stdout ---")
    print(stdout.decode())
    print(f"--- stderr ---")
    print(stderr.decode() if stderr else '(empty)')
    print(f"--- end ---")
    print(f"返回码: {proc.returncode}")


# =============================================================================
# 流式处理输出
# =============================================================================


async def demo_stream_output() -> None:
    """示例 04：流式处理进程输出。"""
    print("\n\n== 流式处理输出 ==\n")

    proc = await asyncio.create_subprocess_exec(
        'python3', '-c',
        '''
import time
for i in range(5):
    print(f"Line {i}")
    time.sleep(0.1)
print("Done")
        ''',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    print(f"进程已启动，流式读取输出:\n")

    # 实时读取输出
    while True:
        # 逐行读取
        line = await proc.stdout.readline()
        if not line:
            # EOF
            break
        print(f"  [stdout] {line.decode().strip()}")

    # 等待进程结束
    await proc.wait()

    print(f"\n进程结束，返回码: {proc.returncode}")


# =============================================================================
# 并发执行多个进程
# =============================================================================


async def run_command(name: str, cmd: list[str]) -> int:
    """运行单个命令并返回退出码。"""
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    if stdout:
        print(f"[{name}] stdout: {stdout.decode().strip()}")
    if stderr:
        print(f"[{name}] stderr: {stderr.decode().strip()}")

    return proc.returncode


async def demo_concurrent_processes() -> None:
    """示例 05：并发执行多个进程。"""
    print("\n\n== 并发执行多个进程 ==\n")

    # 定义要执行的命令
    commands = {
        'date': ['date'],
        'uname': ['uname', '-a'],
        'pwd': ['pwd'],
    }

    print(f"并发执行 {len(commands)} 个命令...\n")

    # 并发执行所有命令
    tasks = [
        run_command(name, cmd)
        for name, cmd in commands.items()
    ]

    results = await asyncio.gather(*tasks)

    print(f"\n所有命令执行完成")
    print(f"返回码: {dict(zip(commands.keys(), results))}")


# =============================================================================
# 进程控制
# =============================================================================


async def demo_process_control() -> None:
    """示例 06：进程控制 - 等待、终止、超时。"""
    print("\n\n== 进程控制 ==\n")

    # 创建一个长时间运行的进程
    proc = await asyncio.create_subprocess_exec(
        'python3', '-c',
        '''
import time
print("Long running process...")
for i in range(10):
    print(f"Working... {i+1}/10")
    time.sleep(0.1)
print("Done")
        ''',
        stdout=asyncio.subprocess.PIPE,
    )

    print(f"进程已启动，PID: {proc.pid}")

    # 等待一小段时间
    await asyncio.sleep(0.3)

    print(f"\n终止进程...")
    # terminate() 发送 SIGTERM（优雅终止）
    # kill() 发送 SIGKILL（强制终止）
    proc.terminate()

    # 等待进程结束
    await proc.wait()

    print(f"进程已终止")
    print(f"  返回码: {proc.returncode}")
    print(f"  (负返回码表示被信号终止)")


# =============================================================================
# 超时控制
# =============================================================================


async def demo_process_timeout() -> None:
    """示例 07：进程执行超时控制。"""
    print("\n\n== 进程超时控制 ==\n")

    try:
        # 使用 asyncio.wait_for 设置超时
        proc = await asyncio.create_subprocess_exec(
            'python3', '-c', 'import time; time.sleep(10); print("Done")',
            stdout=asyncio.subprocess.PIPE,
        )

        print(f"进程已启动，设置 0.5 秒超时...")

        # 等待进程完成（带超时）
        await asyncio.wait_for(proc.wait(), timeout=0.5)

    except asyncio.TimeoutError:
        print(f"\n超时！终止进程")

        # 超时后需要手动终止进程
        try:
            proc.kill()
            await proc.wait()
        except ProcessLookupError:
            pass

        print(f"进程已终止，返回码: {proc.returncode}")


# =============================================================================
# 进程状态检查
# =============================================================================


async def demo_process_status() -> None:
    """示例 08：进程状态检查。"""
    print("\n\n== 进程状态检查 ==\n")

    proc = await asyncio.create_subprocess_exec(
        'echo', 'Hello',
        stdout=asyncio.subprocess.PIPE,
    )

    print(f"进程状态:")
    print(f"  PID: {proc.pid}")
    print(f"  返回码: {proc.returncode} (None = 运行中)")

    # 等待进程完成
    await proc.wait()

    print(f"\n进程结束后:")
    print(f"  返回码: {proc.returncode}")


# =============================================================================
# 错误处理
# =============================================================================


async def demo_error_handling() -> None:
    """示例 09：错误处理。"""
    print("\n\n== 错误处理 ==\n")

    # 执行不存在的命令
    print(f"执行不存在的命令:")
    proc = await asyncio.create_subprocess_exec(
        'nonexistent_command_xyz',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    print(f"  返回码: {proc.returncode}")
    print(f"  stderr: {stderr.decode().strip()}")
    print(f"  (非零返回码表示命令失败)")

    # 执行命令但参数错误
    print(f"\n执行参数错误的命令:")
    proc = await asyncio.create_subprocess_exec(
        'ls', '/nonexistent_path_xyz',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    print(f"  返回码: {proc.returncode}")
    print(f"  stderr: {stderr.decode().strip()}")


# =============================================================================
# 管道和重定向
# =============================================================================


async def demo_pipe_redirection() -> None:
    """示例 10：管道和重定向。"""
    print("\n\n== 管道和重定向 ==\n")

    # stdin=subprocess.PIPE
    # stdout=subprocess.PIPE
    # stderr=subprocess.PIPE
    # stderr=subprocess.STDOUT (合并到stdout)

    proc = await asyncio.create_subprocess_exec(
        'python3', '-c',
        '''
import sys
print("To stdout")
print("To stderr", file=sys.stderr)
sys.stderr.write("Stderr write\\n")
        ''',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    print(f"重定向设置:")
    print(f"  stdin: PIPE")
    print(f"  stdout: PIPE")
    print(f"  stderr: PIPE")

    stdout, stderr = await proc.communicate()

    print(f"\n输出:")
    print(f"  stdout: {stdout.decode().strip()}")
    print(f"  stderr: {stderr.decode().strip()}")


# =============================================================================
# 主函数
# =============================================================================


async def main() -> None:
    """运行所有示例。"""
    print("="*60)
    print("asyncio 子进程管理示例")
    print("="*60)

    demo_subprocess_exec()
    await demo_subprocess_exec()

    demo_subprocess_shell()
    await demo_subprocess_shell()

    demo_process_communicate()
    await demo_process_communicate()

    demo_stream_output()
    await demo_stream_output()

    demo_concurrent_processes()
    await demo_concurrent_processes()

    demo_process_control()
    await demo_process_control()

    demo_process_timeout()
    await demo_process_timeout()

    demo_process_status()
    await demo_process_status()

    demo_error_handling()
    await demo_error_handling()

    demo_pipe_redirection()
    await demo_pipe_redirection()

    print("\n" + "="*60)
    print("asyncio.subprocess API 速查")
    print("="*60)
    print("\n创建进程:")
    print("  create_subprocess_exec(*args, **kwargs)")
    print("  create_subprocess_shell(cmd, **kwargs)")
    print("\n参数:")
    print("  stdout=PIPE        捕获标准输出")
    print("  stderr=PIPE        捕获标准错误")
    print("  stdin=PIPE         提供标准输入")
    print("  stderr=STDOUT      合并stderr到stdout")
    print("\nProcess对象:")
    print("  proc.pid            进程ID")
    print("  proc.returncode     退出码")
    print("  proc.wait()         等待结束")
    print("  proc.communicate(input) 发送输入并等待结束")
    print("  proc.terminate()    发送SIGTERM")
    print("  proc.kill()         发送SIGKILL")
    print("\n注意事项:")
    print("  ✓ 使用exec更安全（避免shell注入）")
    print("  ✓ 记得等待进程结束（wait或communicate）")
    print("  ✓ 超时时手动终止进程")
    print("  ✓ 检查returncode判断成功与否")


if __name__ == "__main__":
    asyncio.run(main())
