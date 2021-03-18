#! /usr/bin/env python3

# Spoj task #4 - PESEL: https://pl.spoj.com/problems/JPESEL/ - Accepted

t = int(input())
#"Enter the number of tests: "

result = []

for i in range (0, t):
    pesel = list(input())
    #"Enter the Pesel number to check: "
    pesel[0] = int(pesel [0])
    pesel[1] = int(pesel [1]) * 3
    pesel[2] = int(pesel [2]) * 7
    pesel[3] = int(pesel [3]) * 9
    pesel[4] = int(pesel [4])
    pesel[5] = int(pesel [5]) * 3
    pesel[6] = int(pesel [6]) * 7
    pesel[7] = int(pesel [7]) * 9
    pesel[8] = int(pesel [8])
    pesel[9] = int(pesel [9]) * 3
    pesel[10] = int(pesel [10])
    total = sum(pesel)
    if total % 10 == 0:
        result += "D"
    else:
        result += "N"

for element in result:
    print(element)