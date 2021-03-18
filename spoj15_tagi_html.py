#! /usr/bin/env python3

# Spoj task #15 - Tagi HTML: https://pl.spoj.com/problems/JHTMLLET/

text = input("Enter the HTML code to be converted: ")

lines = text.splitlines()

for line in lines:
    start_count = line.count("<")
    end_count = line.count(">")
    if start_count != end_count:
        print("Incorrect input - matching opening or closing brackets missing")
    for i in range(0, start_count):
        start_index = int(str(line).find("<"))
        end_index = int(str(line).find(">"))
        for sign in line[start_index + 1 : end_index]:
            sign = sign.upper()
            print(sign)
        print(line)

# Line12: separating index ranges?

import re

for line in lines:
    for start_indexes in re.finditer("<", line):
        print(start_indexes.start())
    for end_indexes in re.finditer(">", line):
        print(end_indexes.start())