#! /usr/bin/env python3

# Spoj task #2 - POŁOWA: https://pl.spoj.com/problems/POL/

t = int(input())
table = []

for num in range (0, t):
    table += list(str.split(input()))
#print(table)

half = ""
x = 0
y = ""

for elem in table:
    half = int(len(elem)/2)
    for x in range(0,half):
        y += elem[x]
    print(y)
    y = ""