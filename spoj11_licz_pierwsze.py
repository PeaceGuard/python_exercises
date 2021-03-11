#! /usr/bin/env python3

# Spoj task #11 - Liczby pierwsze: https://pl.spoj.com/problems/PRIME_T/

#test_num = int(input())

#for elem in range(0, test_num):
#    number = int(input())
#    divisor = 2
#    num_sq = number ** (1/2)
#    while (divisor <= num_sq):
#        if number % divisor == 0:
#            print("NIE")
#            break
#        else:
#            divisor += 1
#    if number == 1:
#        continue
#    if divisor > num_sq:
#        print("TAK")

test_num = int(input())
lst = []

for elem in range(0, test_num):
    number = int(input())
    divisor = 2
    num_sq = number ** (1/2)
    while (divisor <= num_sq):
        if number % divisor == 0:
            lst.append("NIE")
            break
        else:
            divisor += 1
    if number == 1:
        lst.append("NIE")
        continue
    if divisor > num_sq:
        lst.append("TAK")

for component in lst:
    print(component)

#for elem in range(0, test_num):
#    number = int(input())
#    divisor = 2
#    while (divisor < number):
#        if number % divisor == 0:
#            print("NIE")
#            break
#        else:
#            divisor += 1
#    if number == divisor:
#        print("TAK")
#    if number == 1:
#        print("NIE")

# QUESTION: How to make YES in an easier way?