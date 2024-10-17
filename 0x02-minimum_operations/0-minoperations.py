#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    if n <= 1:
        return 0

    divisor = 2
    nOperations = 0
    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            nOperations = nOperations + divisor
        else:
            divisor += 1

    return nOperations
