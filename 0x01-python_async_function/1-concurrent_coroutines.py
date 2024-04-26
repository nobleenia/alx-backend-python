#!/usr/bin/env python3
"""
This module includes the wait_n coroutine that
manages multiple instances of
wait_random concurrently and collects their results
in ascending order of completion.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Parameters:
    n (int): The number of times to call wait_random.
    max_delay (int): The maximum delay allowed for wait_random.

    Returns:
    List[float]: A list of float values representing the delays,
    sorted by completion order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results


if __name__ == "__main__":
    import asyncio
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
