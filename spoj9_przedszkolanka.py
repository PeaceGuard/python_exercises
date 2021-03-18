#! /usr/bin/env python3

# Spoj task #9 - Przedszkolanka: https://pl.spoj.com/problems/PRZEDSZK/ - Accepted

while True:
    try:
        test_num = int(input())
        #"Enter the number of tests: "
    except ValueError:
        print("Enter an integer value")
        continue
    if test_num < 1 or test_num > 20:
        print ("Enter a number between 1 and 20")
        continue
    break

for i in range(0, test_num):
    while True:
        try:
            kid_numbers = input().split()
            #"Enter the numbers of kids in classes separated by space: "
            group_a = int(kid_numbers[0])
            group_b = int(kid_numbers[1])
        except ValueError:
            print("Enter an integer value")
            continue
        except IndexError:
            print("Enter two positive integers separated by space")
            continue
        if group_a not in range(10, 31) or group_b not in range(10, 31):
            print("Enter a number between 10 and 30")
            continue
        else:
            if group_a > group_b:
                bigger_num = group_a
            else:
                bigger_num = group_b
            while bigger_num % group_a != 0 or bigger_num % group_b != 0:
                bigger_num += 1
            lcm = bigger_num
            print(lcm)
        break