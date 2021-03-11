#! /usr/bin/env python3

import sys

result = 0
n_num = int(sys.argv[1])

def fibonacci(digit):
    if digit > 1:
        result = fibonacci(digit - 1) + fibonacci(digit - 2)
#        print(result) - why?
    elif digit == 1:
        result = 1
    elif digit == 0:
        result = 0
    return result

print(fibonacci(n_num))