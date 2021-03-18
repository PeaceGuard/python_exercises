#! /usr/bin/env python3

# Spoj task #1 - EASY ADDITION: https://pl.spoj.com/problems/RNO_DOD/ - Accepted

t = int(input())
#"Enter the number of tests: "

numbers = []

for i in range(0, t):
    total = 0
    n = input()
    #"Enter the number of digits to be summed up: "
    numbers = list(input().split())
    #"Enter the digits to be summed up, separated by spaces: "
    for element in numbers:
        total += int(element)
    print(total)

# V2:
#    for j in range(0, n):
#        total += int(numbers[j])
#    print(total)
#    total = 0

# V3:
#    for element in numbers:
#        total += int(element)
#    totals.append(total)
#    total = 0
#for element in totals:
#    print(element)

#d = {
#    "key": "value",
#    "other": "special",
#    "num": 789
#}