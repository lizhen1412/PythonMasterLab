#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：本地 async echo server + 客户端验证回显。
"""

from __future__ import annotations

import asyncio
from typing import Tuple


async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    data = await reader.read(1024)
    writer.write(data)
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def run_server() -> Tuple[asyncio.AbstractServer, int]:
    server = await asyncio.start_server(handle_echo, host="127.0.0.1", port=0)
    addr = server.sockets[0].getsockname()
    assert isinstance(addr, tuple)
    return server, addr[1]


async def run_client(port: int, message: bytes) -> bytes:
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    writer.write(message)
    await writer.drain()
    data = await reader.read(1024)
    writer.close()
    await writer.wait_closed()
    return data


async def main_async() -> None:
    server, port = await run_server()
    async with server:
        msg = b"hello exercise"
        echoed = await run_client(port, msg)
        print("echoed ->", echoed)
        await server.wait_closed()


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
