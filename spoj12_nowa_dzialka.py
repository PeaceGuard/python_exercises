#! /usr/bin/env python3

# Spoj task #12 - Nowa działka: https://pl.spoj.com/problems/MWPZ06X/ - Accepted

import math

while True:
    try:
        test_num = int(input())
        #"Enter the number of tests: "
    except ValueError:
        print("Enter an integer value")
        continue
    if test_num < 1 or test_num > 500:
        print("Enter an integer between 1 and 500")
        continue
    break

area_list = []

for i in range(0, test_num):
    while True:
        try:
            side_length = int(input())
            #"Enter the steps number: "
        except ValueError:
            print("Steps number should be an integer")
            continue
        if side_length < 1 or side_length > 1000:
            print("Enter the steps number between 1 and 1000")
            continue
        else:
            area = int(math.pow(side_length, 2))
            area_list.append(area)
        break

for element in area_list:
    print(element)

#for elem in range(0, test_num):
#    side = int(input())
#    area = side ** 2
#    print(area)