#!/usr/bin/python3

# Fizz buzz

number = 1
fizz = []
buzz = []
fizz_buzz = []
fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)

# use while loop to iterate 100 numbers; if to divide numbers into corresponding lists & len to count them

while(fizzbuzz_count < 100):
    if number % 3 == 0 and number % 5 != 0:
        fizz.append(number)
        number += 1
        fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)
    elif number % 3 != 0 and number % 5 == 0:
        buzz.append(number)
        number += 1
        fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)
    elif number % 3 == 0 and number % 5 == 0:
        fizz_buzz.append(number)
        number += 1
        fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)
    else:
        number += 1
        fizzbuzz_count = len(fizz) + len(buzz) + len(fizz_buzz)

print("Fizz numbers are:", fizz, "- there are", len(fizz), "of us!")
print("Buzz numbers are:", buzz, "- there are", len(buzz), "of us!")
print("Fizz Buzz numbers are:", fizz_buzz, "- there are", len(fizz_buzz), "of us!")
print("There's a total of", fizzbuzz_count, "of us, Fizz buzz game numbers! :)")