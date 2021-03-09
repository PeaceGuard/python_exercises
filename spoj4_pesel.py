#! /usr/bin/env python3

# Spoj task #4 - PESEL: https://pl.spoj.com/problems/JPESEL/

print("Please provide the number of tests")
t = int(input())
table = []
total = 0
result = []

for num in range (0, t):
    table = list(input())
    table[0] = int(table [0])
    table[1] = int(table [1]) * 3
    table[2] = int(table [2]) * 7
    table[3] = int(table [3]) * 9
    table[4] = int(table [4])
    table[5] = int(table [5]) * 3
    table[6] = int(table [6]) * 7
    table[7] = int(table [7]) * 9
    table[8] = int(table [8])
    table[9] = int(table [9]) * 3
    table[10] = int(table [10])
    total = sum(table)
    if total % 10 == 0:
        result += "D"
    else:
        result += "N"
for elem in result:
    print(elem)