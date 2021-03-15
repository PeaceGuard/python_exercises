#! /usr/bin/env python3

# Spoj task #1 - EASY ADDITION: https://pl.spoj.com/problems/RNO_DOD/

print("Please provide the number of tests")
t = int(input())
table = []
total = 0

for num in range (0, t*2):
    table += list(str.split(input()))
print(table)

for elem in table:
    total += int(elem)
print(total)

d = {
    "key": "value",
    "other": "special",
    "num": 789
}

