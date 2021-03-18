#! /usr/bin/env python3

# output all prime numbers from 2 through n

import math

while True:
    try:
        n = int(input("Enter a positive value: "))
    except ValueError:
        print("Enter an integer value")
        continue
    if n < 2:
        print("Enter an integer higher than 1")
        continue
    break

array = [True for elem in range(n - 1)]

for number in range(2, math.isqrt(n) + 1):
    if array[number - 2]:
        for multiple in range(number ** 2, n + 1, number):
            array[multiple - 2] = False

enum_array = list(enumerate(array, 2))

for i, j in enum_array:
    if j:
        print(i)

#for elem in enum_array:
#    if elem[1]:
#        print(elem[0])

#print([i for i, j in enum_array if j])

#table = [True, True, False, True, False]
#enumer = list(enumerate(table, 2))
#print((enumer[2])[0])

# Other methods of filling an array:
# 1. array = [True] * (n - 1)
# 2. array = []
# for elem in range(2, n + 1):
#     array.append(True)