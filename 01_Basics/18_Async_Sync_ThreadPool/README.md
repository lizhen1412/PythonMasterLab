# Python 3.11+ 异步 + 同步 + 线程池协作（第 18 章）

本章是一组“可运行的小脚本”，讲解同步/线程池/asyncio 的协作：线程池基础与适用场景、CPU vs I/O 性能对比、在协程中调用阻塞函数（`asyncio.to_thread`/`run_in_executor`）、并发限流、超时与取消、混合生产者-消费者（async + 线程池）、日志与清理、常见反例与退出策略。附带练习题（每题一文件）。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/18_Async_Sync_ThreadPool/01_overview.py`
- 运行某个示例：`python3 01_Basics/18_Async_Sync_ThreadPool/02_threadpool_basics.py`
- 练习题索引：`python3 01_Basics/18_Async_Sync_ThreadPool/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单

- 模型对比：同步 vs 线程池 vs asyncio；阻塞 I/O vs CPU 密集 vs async I/O
- 线程池基础：`ThreadPoolExecutor` 的 submit/map/as_completed，异常传播、超时/取消、`shutdown(cancel_futures)`
- CPU vs I/O：线程池对 CPU 密集无益，I/O 可获并发
- asyncio 调用阻塞代码：`asyncio.to_thread`、`loop.run_in_executor`（可自建线程池），并发数控制（线程池大小/Semaphore）
- 超时与取消：`asyncio.wait_for`/`asyncio.timeout` + to_thread；CancelledError 清理
- 混合管线：async 生产者 + 线程池消费者（阻塞函数），backpressure/哨兵退出
- 日志与清理：线程名日志；try/finally 释放；`cancel_futures` 行为
- 反例警示：在线程池任务里调用 `asyncio.run`、无节制创建任务导致爆炸
- 退出策略：优雅停机，取消未开始任务，已运行任务检查停止信号

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_threadpool_basics.py`](02_threadpool_basics.py) | ThreadPoolExecutor 提交/结果/异常/超时/取消 |
| 03 | [`03_cpu_vs_io_in_threadpool.py`](03_cpu_vs_io_in_threadpool.py) | CPU 密集 vs I/O 模拟：线程池收益对比 |
| 04 | [`04_async_to_thread_basics.py`](04_async_to_thread_basics.py) | async 中用 asyncio.to_thread 包装阻塞函数 |
| 05 | [`05_run_in_executor_legacy.py`](05_run_in_executor_legacy.py) | loop.run_in_executor（自建线程池）兼容旧代码 |
| 06 | [`06_limit_concurrency_with_semaphore.py`](06_limit_concurrency_with_semaphore.py) | Semaphore + to_thread 限制阻塞调用并发 |
| 07 | [`07_timeout_and_cancel_bridge.py`](07_timeout_and_cancel_bridge.py) | wait_for/asyncio.timeout + to_thread，取消与清理 |
| 08 | [`08_async_producer_threadpool_consumer.py`](08_async_producer_threadpool_consumer.py) | async 生产 + 线程池消费阻塞任务，哨兵退出 |
| 09 | [`09_threadpool_logging_and_cleanup.py`](09_threadpool_logging_and_cleanup.py) | 线程名日志，shutdown(cancel_futures) 行为与清理 |
| 10 | [`10_what_not_to_do.py`](10_what_not_to_do.py) | 反例：线程池里 asyncio.run、无限制任务堆积 |
| 11 | [`11_chapter_summary.py`](11_chapter_summary.py) | 本章总结：规则清单与常见坑 |
| 12 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/18_Async_Sync_ThreadPool/Exercises/01_overview.py`

- `Exercises/02_submit_io_tasks.py`：线程池并发假 I/O，收集结果
- `Exercises/03_compare_cpu_io_threadpool.py`：对比线程池处理 CPU vs I/O 耗时
- `Exercises/04_async_to_thread_wrapper.py`：封装 to_thread，限流并记录异常
- `Exercises/05_run_in_executor_limit.py`：自建线程池 + run_in_executor 提交多任务，限制并发
- `Exercises/06_wait_for_timeout_cleanup.py`：wait_for 包装 to_thread，超时后清理
- `Exercises/07_async_producer_thread_consumer.py`：asyncio.Queue 生产、线程池消费（阻塞），哨兵退出
- `Exercises/08_shutdown_cancel_futures.py`：演示 shutdown(cancel_futures=True) 对未开始任务的影响
- `Exercises/09_logging_thread_names_async.py`：logging 打印线程名与 async 上下文，运行混合任务

---

## 5) 小贴士

- 线程池适合阻塞 I/O，不提升 CPU 密集性能；CPU 密集用多进程/扩展
- 协程里调用阻塞函数请用 to_thread/run_in_executor，否则会卡住事件循环
- 控制并发：限制线程池大小或加 Semaphore，避免任务爆炸
- 超时/取消后记得清理资源，CancelledError 是正常控制流
- 退出时可使用 shutdown(cancel_futures=True) 取消未开始任务；已运行任务需自行检查停止信号
