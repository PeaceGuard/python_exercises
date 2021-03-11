#! /usr/bin/env python3

# Spoj task #13 - Prawie jak Fibonacci: https://pl.spoj.com/problems/DDZ5/

num_count = int(input())
lst = str.split(input())
lst2 = []
count = 0

lst2.append(lst[0])
lst2.append(lst[1])
for elem in lst[2:num_count]:
    x = int(lst2[0])
    y = int(lst2[1])
    if int(elem) == x + y:
        count += 1
    lst2.append(elem)
    lst2.pop(0)

print(count)