# 0x01. Python - Async

0. 0-basic_async_syntax.py: An asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it
1. 1-concurrent_coroutines.py: An async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay
2. 2-measure_runtime.py: A measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n
3. 3-tasks.py: A function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task
4. 4-tasks.py: Take the code from wait_n and alter it into a new function task_wait_n