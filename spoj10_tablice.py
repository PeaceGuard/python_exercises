#! /usr/bin/env python3

# Spoj task #10 - Tablice: https://pl.spoj.com/problems/PP0502B/

while True:
    try:
        test_num = int(input())
        if test_num < 1 or test_num > 100:
            print("Enter a number of at least 1 and at most 100")
            continue
    except ValueError:
        print("Enter a numeral value")
        continue
    else:
        for elem in range(0, test_num):
            while True:
                try:
                    digits = str.split(input())
                    digit_num = digits[0]
                    if int(digit_num) < 1 or int(digit_num) > 100:
                        print("Enter a number of at least 1 and at most 100")
                        continue
                except ValueError:
                    print("Enter a numeral value")
                    continue
                except IndexError:
                    print("Enter a non-empty value")
                    continue
                else:
                    digits.pop(0)
                    digits.reverse()
                    for component in digits:
                        print(component)
                        continue
                break
    break

# No proofing for digit_num != real number of submitted digits
# Do version with one-line printed result