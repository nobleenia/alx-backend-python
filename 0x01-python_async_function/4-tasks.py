#!/usr/bin/env python3
"""
This module modifies the original wait_n function to use asyncio.
Task objects, created through task_wait_random,
and collects their results in the order of completion.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay,
    and awaits their completion.

    Parameters:
    n (int): The number of tasks to spawn.
    max_delay (int): The maximum delay allowed for each task.

    Returns:
    List[float]: A list of float values representing the delays,
    sorted by completion order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results

if __name__ == "__main__":
    import asyncio

    async def main():
        n = 5
        max_delay = 6
        print(await task_wait_n(n, max_delay))

    asyncio.run(main())
