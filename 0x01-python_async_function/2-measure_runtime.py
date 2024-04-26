#!/usr/bin/env python3
"""
This module provides functionality to measure
the runtime of the asynchronous
wait_n function from a previous module and
calculate the average runtime per operation.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n divided
    by n to find the average time per operation.

    Parameters:
    n (int): The number of times to call wait_random.
    max_delay (int): The maximum delay allowed for wait_random.

    Returns:
    float: The average time per operation in seconds.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Execute the asynchronous function
    end_time = time.time()  # Record the end time
    total_time = end_time - start_time  # Calculate total time
    return total_time / n  # Return the average time per operation


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
