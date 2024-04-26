#!/usr/bin/env python3
"""
This module provides a function that wraps the wait_random
coroutine into an asyncio.Task.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task to execute the wait_random
    coroutine with a given max_delay.

    Parameters:
    max_delay (int): The maximum delay allowed for wait_random.

    Returns:
    asyncio.Task: A task that executes the wait_random coroutine.
    """
    # Create a Task from the wait_random coroutine
    task = asyncio.create_task(wait_random(max_delay))
    return task


if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
