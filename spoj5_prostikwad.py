#! /usr/bin/env python3

# Spoj task #5 - Prostokąty i Kwadraty: https://pl.spoj.com/problems/FR_12_05/ - Accepted

while True:
    try:
        side_lengths = input().split()
        #"Enter two integers separated by space, for a and b rectangle side lengths: "
        a = int(side_lengths[0])
        b = int(side_lengths[1])
    except ValueError:
        print("Non-integer value entered")
        continue
    except IndexError:
        print("Enter two positive integers separated by space")
        continue
    if a >= b or a < 1 or b < 1 or a > 10000 or b > 10000:
        print('Please provide input in format "a b", where both numbers are natural and meet 1 ≤ a < b ≤ 10⁴ condition')
        continue
    else:
        break

big_sq_area = a ** 2

if b <= 2 * a:
    side_diff = b - a
    small_sq_area = side_diff ** 2
else:
    small_sq_area = a ** 2

total_area = big_sq_area + small_sq_area
print(total_area)

# QUESTION: Why is int() from a letter ValueError, not TypeError?
# QUESTION: Why does 55_55 (as opposed to other symbols) pass as numerical value (no ValueError)?