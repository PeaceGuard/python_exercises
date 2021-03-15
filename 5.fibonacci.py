#! /usr/bin/env python3

import sys

result = 0
n = int(sys.argv[1])

def fibonacci_recur(digit):
    if digit == 0:
        result = 0
    elif digit == 1:
        result = 1
    elif digit > 1:
        result = fibonacci_recur(digit - 1) + fibonacci_recur(digit - 2)
    return result

def fibonacci_iter(digit):
    a = 0
    b = 1
    for elem in range(0, digit):
        a, b = b, a + b
    return a

print(fibonacci_recur(n))

print(fibonacci_iter(n))
