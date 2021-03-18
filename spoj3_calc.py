#! /usr/bin/env python3

# Spoj task #3 - CALC: https://pl.spoj.com/problems/CALC/ - not uploaded (reading from file)

input_file = open("/home/marek-stoppel/it/git/python_projects/calc", "r")
text = input_file.read()
input_file.close()

list_calculations = list(text.split("\n"))
nr_lines = len(text.splitlines())
print(list_calculations)
list_calculations.pop(nr_lines)
result = 0

for element in list_calculations:
    calculation = list(element.split(" "))
    if calculation[0] == "+":
        result = int(calculation[1]) + int(calculation[2])
        print(result)
    elif calculation[0] == "-":
        result = int(calculation[1]) - int(calculation[2])
        print(result)
    elif calculation[0] == "*":
        result = int(calculation[1]) * int(calculation[2])
        print(result)
    elif calculation[0] == "/":
        result = int(calculation[1]) // int(calculation[2])
        print(result)
    elif calculation[0] == "%":
        result = int(calculation[1]) % int(calculation[2])
        print(result)
    else:
        print("unrecognized arithmetic operator")