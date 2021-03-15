#! /usr/bin/env python3

# Sum of first 100 natural numbers divisible by 7, using 'while'

total = 0
number = 7
i = 1

while i <= 100:
    total += number
    number += 7
    i += 1

#while (number <= 700):
#    if number % 7 == 0:
#        total += number
#        number += 1
#    else:
#        number += 1

print("While: The sum of first 100 natural numbers divisible by 7 is " + str(total) + ".")

# Sum of first 100 natural numbers divisible by 7, using 'for' - v1

tot = 0
num = 7

for i in range(0, 100):
    tot += num
    num += 7

# for num in range(1, 701):
#    if num % 7 == 0:
#        tot += num

print("For#1: The sum of first 100 natural numbers divisible by 7 is " + str(tot) + ".")

# Sum of first 100 natural numbers divisible by 7, using 'for' - v2

tot2 = 0

for num2 in range(7, 701, 7):
    tot2 += num2
print("For#2: The sum of first 100 natural numbers divisible by 7 is " + str(tot2) + ".")

# Warunek pętli ma być zdefiniowany przez sumę 100 liczb + jeszcze coś do usunięcia (else & continue w for-if?)