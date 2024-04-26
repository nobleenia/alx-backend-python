#!/usr/bin/env python3
"""
This module defines an asynchronous generator
that yields random numbers between 0 and 10
following a delay of 1 second for each number generated.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that waits 1 second
    before yielding a random float
    between 0 and 10. This process repeats 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

if __name__ == "__main__":
    import asyncio

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
