#!/usr/bin/env python3
"""
This module defines an asynchronous comprehension coroutine
that gathers values generated by an asynchronous generator.
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Use an asynchronous comprehension to collect 10 random numbers from an
    asynchronous generator and return them.

    Returns:
    list: A list of 10 random numbers generated by async_generator.
    """
    return [i async for i in async_generator()]

if __name__ == "__main__":
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
