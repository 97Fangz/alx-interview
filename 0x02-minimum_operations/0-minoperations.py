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


if __name__ == '__main__':
    from random import randint
    from time import time

    start_time = time()

    for _ in range(10):
        n = randint(2, 100)
        print("Min # of operations to reach {} char (original): {}".
              format(n, minOperations(n)))
        print("Min # of operations to reach {} char (modified): {}".
              format(n, minOperationsModified(n)))

    print(f'==> Program completed in {time() - start_time:.3f}s')
