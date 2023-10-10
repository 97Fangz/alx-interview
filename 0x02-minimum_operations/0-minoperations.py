#!/usr/bin/env python3

"""
Minimum Operations
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1

    while n > 1:
        if n % clipboard == 0:
            operations += 2
            n //= clipboard
        else:
            clipboard += 1
            operations += 1

    return operations
