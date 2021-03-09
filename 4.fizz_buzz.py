#! /usr/bin/env python3

# Fizz buzz

n_liczb = input()
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

for elem in range (1, int(n_liczb) + 1):
    if elem % 3 == 0 and elem % 5 != 0:
        print("Fizz")
        elem += 1
    elif elem % 3 != 0 and elem % 5 == 0:
        print("Buzz")
        elem += 1
    elif elem % 3 == 0 and elem % 5 == 0:
        print("Fizz Buzz")
        elem += 1
    else:
        print(elem)
        elem += 1