#! /usr/bin/env python3

# Sum of first 100 natural numbers divisible by x divisor value provided by the user, using 'while'

divisor = 0
while True:
    try:
        divisor = int(input("Enter a positive value: "))
    except ValueError:
        print("Non-integer value entered by the user, try again...")
        continue
    if divisor < 1:
        print("Non-positive value entered by the user, try again...")
        continue
    break

total = 0
number = divisor
i = 1

while i <= 100:
    total += number
    number += divisor
    i += 1

print("While: The sum of first 100 natural numbers divisible by", divisor, "is " + str(total) + ".")

# Sum of first 100 natural numbers divisible by x divisor value provided by the user, using 'for'

tot = 0
increm = divisor

for i in range(0, 100):
    tot += increm
    increm += divisor


#tot = 0
#for num in range(1, divisor * 100 + 1):
#    if num % divisor == 0:
#        tot += num

print("For: The sum of first 100 natural numbers divisible by " + str(divisor) + " is " + str(tot) + ".")

# While oraz for do przepisania w wersji bez else, continue i break
# Dwie wersje: zaczynająca od 7 oraz inna
