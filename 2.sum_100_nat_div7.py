#! /usr/bin/env python3

# Sum of first 100 natural numbers divisible by 7

number = 700
sum = 0

# use while loop to iterate downwards from 'number' until zero & if to sum only numbers divisible by 7

while(number > 0):
    if number % 7 == 0:
        sum += number
        number -= 1
    else:
        sum = sum
        number -= 1
print("The sum of first 100 natural numbers divisible by 7 is",sum,".")
