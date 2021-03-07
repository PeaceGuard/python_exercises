#! /usr/bin/env python3

# Sum of first 100 natural numbers divisible by x divisor value provided by the user

print("Please provide a DIVISOR value (natural number) for which you'd like to see a sum of first 100 divisible natural numbers.")

x = int(input())
number = 100 * x
sum = 0

# use while loop to iterate downwards from 'number' until zero & if to sum only numbers divisible by x

if x <= 0:
    while(x <= 0):
        print("Enter a natural number > 0.")
        x = int(input())
else:
    while(number > 0):
        if number % x == 0:
            sum += number
            number -= 1
        else:
            sum = sum
            number -= 1
    print("The sum of first 100 natural numbers divisible by", x, "is",sum,".")
