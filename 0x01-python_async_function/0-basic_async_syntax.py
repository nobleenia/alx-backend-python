#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that
waits for a random amount of time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random time
    between 0 and max_delay seconds.

    Parameters:
    max_delay (int): The maximum delay time in seconds.

    Returns:
    float: The actual delay time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    # You can test this function directly by running this module,
    # but the actual testing should be
    # done through the `0-main.py` script.
    import asyncio
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
