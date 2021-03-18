#! /usr/bin/env python3

# Spoj task #11 - Liczby pierwsze: https://pl.spoj.com/problems/PRIME_T/ - Accepted

import math

test_num = int(input())
result_list = []

for i in range(0, test_num):
    number = int(input())
    divisor = 2
    number_sq = math.sqrt(number)
    while (divisor <= number_sq):
        if number % divisor == 0:
            result_list.append("NIE")
            break
        else:
            divisor += 1
    if number == 1:
        result_list.append("NIE")
        continue
    if divisor > number_sq:
        result_list.append("TAK")

for element in result_list:
    print(element)

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