#! /usr/bin/env python3

# Spoj task #3 - CALC: https://pl.spoj.com/problems/CALC/

file = open("./it/git/python_projects/calc", "r")
text = file.read()
file.close()

table = list(text.split("\n"))
lines = len(text.splitlines())
table.pop(lines)
result = 0

for elem in table:
    table2 = list(elem.split(" "))
    if table2[0] == "+":
        result = int(table2[1]) + int(table2[2])
        print(result)
    elif table2[0] == "-":
        result = int(table2[1]) - int(table2[2])
        print(result)
    elif table2[0] == "*":
        result = int(table2[1]) * int(table2[2])
        print(result)
    elif table2[0] == "/":
        result = int(table2[1]) // int(table2[2])
        print(result)
    elif table2[0] == "%":
        result = int(table2[1]) % int(table2[2])
        print(result)
    else:
        print("unrecognized arithmetic operator")