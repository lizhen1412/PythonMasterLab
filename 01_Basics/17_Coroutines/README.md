# Python 3.11+ 协程与 asyncio（Coroutines & asyncio）学习笔记（第 17 章）

本章是一组“可运行的小脚本”，讲解 Python 协程/asyncio：async/await 基础、事件循环、任务调度与并发组合（gather/as_completed/TaskGroup）、取消与超时、异步同步原语（Lock/Event/Semaphore/Queue）、阻塞函数转线程、异步 TCP echo 示例、async 上下文/迭代、错误处理与 fire-and-forget 风险，并对比线程使用场景。附带练习题（每题一文件）。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/17_Coroutines/01_overview.py`
- 运行某个示例：`python3 01_Basics/17_Coroutines/02_async_await_basics.py`
- 练习题索引：`python3 01_Basics/17_Coroutines/Exercises/01_overview.py`

> 说明：示例使用 `asyncio.run(...)` 创建/关闭事件循环，要求 Python 3.11+（使用 TaskGroup/asyncio.timeout）。

---

## 2) 本章“知识点全景”清单

- 协程基础：`async def` 定义、`await` 规则、协程对象与事件循环
- 任务与并发：`asyncio.create_task`、`gather`、`as_completed`、`TaskGroup`（结构化并发）
- 取消与超时：`task.cancel`、`CancelledError`、`asyncio.wait_for`、`asyncio.timeout`
- 异步同步原语：`asyncio.Lock/Event/Semaphore/Queue`
- 阻塞代码处理：`asyncio.to_thread` 调用阻塞函数，避免阻塞事件循环
- I/O 示例：本地 TCP echo server/client（`asyncio.start_server`/`open_connection`）
- async 上下文/迭代：`async with`、`async for` 示例
- 错误处理：gather 的 return_exceptions、TaskGroup 异常传播、后台任务异常监控
- fire-and-forget 风险：未 awaited 任务的异常可能被忽略，需监控/封装
- 选择指南：协程 vs 线程（阻塞库 vs async 友好 I/O）

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_async_await_basics.py`](02_async_await_basics.py) | async/await 基础，asyncio.run、sleep、并发 vs 串行 |
| 03 | [`03_tasks_create_and_gather.py`](03_tasks_create_and_gather.py) | create_task、gather、as_completed，返回值与异常 |
| 04 | [`04_taskgroup_structured_concurrency.py`](04_taskgroup_structured_concurrency.py) | TaskGroup（3.11+）结构化并发与异常传播 |
| 05 | [`05_timeout_and_cancel.py`](05_timeout_and_cancel.py) | wait_for/asyncio.timeout、task.cancel、CancelledError |
| 06 | [`06_asyncio_queue_and_sync_primitives.py`](06_asyncio_queue_and_sync_primitives.py) | asyncio.Queue 生产消费；Lock/Event/Semaphore 对比 |
| 07 | [`07_to_thread_and_blocking_calls.py`](07_to_thread_and_blocking_calls.py) | asyncio.to_thread 包装阻塞函数，避免卡住事件循环 |
| 08 | [`08_tcp_echo_server_client.py`](08_tcp_echo_server_client.py) | 本地 TCP echo server/client（不访问外网） |
| 09 | [`09_async_context_and_iter.py`](09_async_context_and_iter.py) | async with 与 async for 示例 |
| 10 | [`10_error_handling_and_return_exceptions.py`](10_error_handling_and_return_exceptions.py) | gather return_exceptions、后台任务异常处理 |
| 11 | [`11_fire_and_forget_caveats.py`](11_fire_and_forget_caveats.py) | fire-and-forget 风险，添加回调监控异常 |
| 12 | [`12_asyncio_vs_threads_brief.py`](12_asyncio_vs_threads_brief.py) | 协程 vs 线程选择指南 |
| 13 | [`13_chapter_summary.py`](13_chapter_summary.py) | 本章总结：规则清单与常见坑 |
| 14 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/17_Coroutines/Exercises/01_overview.py`

- `Exercises/02_run_two_coroutines.py`：并发运行两个 sleep，比较耗时
- `Exercises/03_use_gather_with_errors.py`：gather 处理异常（return_exceptions 对比）
- `Exercises/04_taskgroup_retry_on_failure.py`：TaskGroup 并发，失败任务打印日志
- `Exercises/05_queue_producer_consumer_async.py`：asyncio.Queue 生产消费，哨兵退出
- `Exercises/06_timeout_and_cancel_task.py`：wait_for 超时取消，捕获 CancelledError
- `Exercises/07_to_thread_blocking_io.py`：to_thread 包装阻塞函数，验证事件循环未被阻塞
- `Exercises/08_tcp_echo_roundtrip.py`：启动本地 async echo server，再用客户端验证回显
- `Exercises/09_fire_and_forget_safe_wrapper.py`：封装 create_task，记录异常/结果

---

## 5) 小贴士

- 不要在协程里调用阻塞 I/O/CPU；必要时用 `asyncio.to_thread` 或进程池
- `create_task` 后请保存/await；fire-and-forget 需加异常回调/监控
- `CancelledError` 是正常控制流，捕获后记得再抛出或妥善清理
- `asyncio.run` 负责创建/关闭事件循环；在已经运行的循环中不要再调用它
- `asyncio.Queue` 是线程协程安全的；不要把阻塞队列直接用在协程里
