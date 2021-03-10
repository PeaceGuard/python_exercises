#! /usr/bin/env python3

# Fizz buzz

import sys

digit_number = int(sys.argv[1])

for elem in range (1, int(digit_number) + 1):
    if elem % 3 == 0 and elem % 5 != 0:
        print("Fizz")
    elif elem % 3 != 0 and elem % 5 == 0:
        print("Buzz")
    elif elem % 3 == 0 and elem % 5 == 0:
        print("Fizz Buzz")
    else:
        print(elem)

#fizz = []
#buzz = []
#fizz_buzz = []
#fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)

# use while loop to iterate 100 numbers; if to divide numbers into corresponding lists & len to count them

#while (fizzbuzz_count < 100):
#    if number % 3 == 0 and number % 5 != 0:
#        fizz.append(number)
#        number += 1
#        fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)
#    elif number % 3 != 0 and number % 5 == 0:
#        buzz.append(number)
#        number += 1
#        fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)
#    elif number % 3 == 0 and number % 5 == 0:
#        fizz_buzz.append(number)
#        number += 1
#        fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)
#    else:
#        number += 1
#        fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)
#print (fizz)
#print (buzz)
#print (fizz_buzz)
#print (fizzbuzz_count)