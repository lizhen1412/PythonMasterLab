# Python 3.11+ 线程（Threads）学习笔记（第 16 章）

本章是一组“可运行的小脚本”，讲解线程的核心概念与实践：创建/start/join、daemon、竞争条件与同步原语（Lock/RLock/Semaphore/Event/Condition/Barrier）、线程安全通信（Queue）、线程池与 Future 超时/取消、异常与日志、定时任务、GIL 与性能、何时用线程 vs asyncio。附带练习题（每题一文件）。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/16_Threads/01_overview.py`
- 运行某个示例：`python3 01_Basics/16_Threads/02_thread_basics_start_join.py`
- 练习题索引：`python3 01_Basics/16_Threads/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单

### 2.1 基础与生命周期
- 线程 vs 进程：I/O 密集适合线程，CPU 密集受 GIL 限制
- 创建/start/join；daemon 与非 daemon；name/ident/is_alive
- `join(timeout)` 超时处理

### 2.2 同步原语与竞态防护
- 竞态反例 + Lock 修复；RLock（可重入）
- Semaphore/BoundedSemaphore：限流
- Event：通知/启动/停止
- Condition：等待条件 + notify/all
- Barrier：阶段同步；死锁风险、锁顺序、超时获取

### 2.3 通信与线程安全容器
- `queue.Queue` 生产者-消费者；`put/get/task_done/join`；哨兵值优雅退出
- list/dict 非线程安全对比

### 2.4 线程池与 Future
- ThreadPoolExecutor：`submit`/`map`/`as_completed`
- 结果/异常传播；`result(timeout)`；`cancel/cancelled`；`shutdown(wait, cancel_futures)`

### 2.5 资源清理与退出
- stop flag 或 Event 控制循环；try/finally 释放资源
- daemon 线程不适合做清理

### 2.6 异常、日志与调试
- logging 打印线程名；`threading.excepthook`（3.8+）
- 线程异常不会自动杀主线程，Future 取结果时会抛出

### 2.7 定时/周期任务
- `threading.Timer` 一次性；while+sleep+Event 周期；Timer 精度限制

### 2.8 GIL、性能与选择
- I/O 会释放 GIL；CPU 密集不提速，建议用 multiprocessing/扩展
- asyncio vs 线程：阻塞 I/O 库用线程；大量 async 友好 I/O 用 asyncio

### 2.9 其他提示
- 信号只送达主线程；random 共享状态，必要时每线程独立 Random

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_thread_basics_start_join.py`](02_thread_basics_start_join.py) | 创建/start/join、daemon、name/ident、join 超时 |
| 03 | [`03_race_condition_and_lock.py`](03_race_condition_and_lock.py) | 竞态反例 + Lock 修复 |
| 04 | [`04_reentrant_lock_and_semaphore.py`](04_reentrant_lock_and_semaphore.py) | RLock 重入示例；Semaphore 限制并发 |
| 05 | [`05_event_and_stop_flag.py`](05_event_and_stop_flag.py) | Event 启停信号，优雅退出循环 |
| 06 | [`06_condition_and_barrier.py`](06_condition_and_barrier.py) | Condition 等待/通知；Barrier 阶段同步 |
| 07 | [`07_queue_producer_consumer.py`](07_queue_producer_consumer.py) | Queue 生产者-消费者，哨兵退出 |
| 08 | [`08_threadpool_executor_basics.py`](08_threadpool_executor_basics.py) | ThreadPoolExecutor 提交/结果/异常/超时 |
| 09 | [`09_timeout_and_cancel.py`](09_timeout_and_cancel.py) | join 超时；Future 取消/超时处理 |
| 10 | [`10_thread_exceptions_and_logging.py`](10_thread_exceptions_and_logging.py) | 线程异常、excepthook、日志带线程名 |
| 11 | [`11_timer_and_periodic_tasks.py`](11_timer_and_periodic_tasks.py) | Timer 一次性；周期任务的替代方案 |
| 12 | [`12_gil_and_performance_notes.py`](12_gil_and_performance_notes.py) | GIL 说明：I/O vs CPU 密集对比 |
| 13 | [`13_asyncio_vs_threads_brief.py`](13_asyncio_vs_threads_brief.py) | 线程 vs asyncio 选择指南（简述） |
| 14 | [`14_random_per_thread.py`](14_random_per_thread.py) | 每线程独立 Random 避免共享状态干扰 |
| 15 | [`15_chapter_summary.py`](15_chapter_summary.py) | 本章总结：规则清单与常见坑 |
| 16 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/16_Threads/Exercises/01_overview.py`

- `Exercises/02_fix_race_with_lock.py`：修复计数竞态，使用 Lock
- `Exercises/03_use_semaphore_limit_concurrency.py`：Semaphore 限制并发任务数
- `Exercises/04_wait_with_event.py`：用 Event 控制工作线程开始/停止
- `Exercises/05_queue_worker_with_sentinel.py`：Queue 任务 + 哨兵退出，task_done/join
- `Exercises/06_executor_timeout_and_errors.py`：线程池运行多任务，处理异常与超时
- `Exercises/07_barrier_two_phase_task.py`：Barrier 同步两阶段工作
- `Exercises/08_timer_cancel_demo.py`：Timer 启动后在条件满足前取消
- `Exercises/09_log_thread_names.py`：配置 logging 打印线程名，观察输出顺序

---

## 5) 小贴士

- 不要指望线程提升 CPU 密集性能；I/O 多的场景更合适
- 避免共享可变对象；必须共享时用锁/队列
- daemon 线程不做清理工作；退出前确保资源释放（锁/文件/网络）
- 日志里打印线程名便于调试；必要时给线程命名
- 检测死锁：加锁顺序一致、获取时加 timeout、必要时用锁诊断工具
