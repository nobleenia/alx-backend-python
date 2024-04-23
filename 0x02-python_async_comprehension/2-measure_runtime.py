#!/usr/bin/env python3
"""
This module provides a coroutine to measure the execution
time of running four async_comprehension calls in parallel
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel.

    Returns:
    float: The total runtime in seconds.
    """
    start_time = time.time()  # Start the timer
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)  # Run the comprehensions in parallel
    end_time = time.time()  # End the timer
    return end_time - start_time

if __name__ == "__main__":
    async def main():
        runtime = await measure_runtime()
        print(runtime)

    asyncio.run(main())
