#! /usr/bin/env python3

# Spoj task #10 - Tablice: https://pl.spoj.com/problems/PP0502B/ - Accepted

while True:
    try:
        t = int(input())
        #"Enter the number of tests: "
        if t < 1 or t > 100:
            print("Enter a number of at least 1 and at most 100")
            continue
    except ValueError:
        print("Enter a numeral value")
        continue
    break

for i in range(0, t):
    while True:
        try:
            digits_list = input().split()
            #"Enter the number of digits to reverse followed by those digits, all separated by spaces: "
            digit_num = digits_list[0]
            digits_list.pop(0)
            if int(digit_num) < 1 or int(digit_num) > 100 or int(digit_num) != len(digits_list):
                print("Enter the correct n (digit number) corresponding to the number of following digits")
                continue
        except ValueError:
            print("Enter a numeral value")
            continue
        except IndexError:
            print("Enter a non-empty value")
            continue
        else:
            digits_list.reverse()
            for element in digits_list:
                print(element, end=" ")
                continue
        break

print("")

# Do version with one-line printed result