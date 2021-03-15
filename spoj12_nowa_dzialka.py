#! /usr/bin/env python3

# Spoj task #12 - Nowa działka: https://pl.spoj.com/problems/MWPZ06X/

while True:
    try:
        test_num = int(input())
        if test_num < 1 or test_num > 500:
            print("D value should be not lower than 1 and not higher than 500")
            continue
    except ValueError:
        print("D value should be a natural number")
        continue
    else:
        lst = []
        for elem in range(0, test_num):
            while True:
                try:
                    side = int(input())
                    if side < 1 or side > 1000:
                        print("X value should be not lower than 1 and not higher than 1000")
                        continue
                    else:
                        area = side ** 2
                        lst.append(area)
                except ValueError:
                    print("X value should be a natural number")
                    continue
                break
    break

for component in lst:
    print(component)

#test_num = int(input())

#for elem in range(0, test_num):
#    side = int(input())
#    area = side ** 2
#    print(area)