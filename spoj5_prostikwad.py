#! /usr/bin/env python3

# Spoj task #5 - Prostokąty i Kwadraty: https://pl.spoj.com/problems/FR_12_05/

while True:
    lst = str.split(input())
    try:
        a = int(lst[0])
    except ValueError:
        print("Please provide a numerical value")
        continue
    try:
        b = int(lst[1])
    except IndexError:
        print("Please provide two values")
        continue
    big_sq_area = a ** 2
    if a >= b or a < 1 or b < 1 or a > (10 ** 4) or b > (10 ** 4):
        print ('Please provide input in format "a b", where both numbers are natural and meet 1 ≤ a < b ≤ 10⁴ condition')
        continue
    elif b <= 2 * a:
        side_diff = b - a
        small_sq_area = side_diff ** 2
        break
    else:
        small_sq_area = a ** 2
        break

total_area = big_sq_area + small_sq_area
print(total_area)

# QUESTION: Why is int() from a letter ValueError, not TypeError?
# QUESTION: Why does 55_55 (as opposed to other symbols) pass as numerical value (no ValueError)?