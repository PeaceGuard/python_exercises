#! /usr/bin/env python3

# Spoj task #13 - Prawie jak Fibonacci: https://pl.spoj.com/problems/DDZ5/ - Accepted

number_count = int(input())
#"Enter the number of following digits: "
number_list = input().split()
#"Enter the digit sequence: "

consecutive_triple = []
count = 0

consecutive_triple.append(number_list[0])
consecutive_triple.append(number_list[1])
for element in number_list[2:number_count]:
    elem_1back = int(consecutive_triple[0])
    elem_2back = int(consecutive_triple[1])
    if int(element) == elem_1back + elem_2back:
        count += 1
    consecutive_triple.append(element)
    consecutive_triple.pop(0)

print(count)

# Search for Python queue structure and try using it ; consecutive_triple --> sliding_window