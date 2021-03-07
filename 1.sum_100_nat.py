#! /usr/bin/env python3

# Sum of first 100 natural numbers

number = 100
sum = 0

# use while loop to iterate downwards from 'number' until zero

while (number > 0):
    
    sum += number
    number -= 1
print("The sum of first 100 natural numbers is",sum,".")
print("The sum of first 100 natural numbers is " + str(sum) + ".")
#sum == 5050
print("The sum of first 100 natural numbers is " + str(5050) + ".")
print("The sum of first 100 natural numbers is 5050.")
print("The sum of first 100 natural numbers is {} -- {} xxx {} *** {}.".format(sum, -sum, 222, "kotek"))
print("The sum of first 100 natural {yyy} numbers is {xxx}.".format(xxx=sum, yyy="kotek"))
print(f"The sum of first 100 natural numbers is {sum}.")
#print(f"The sum of first 100 natural numbers is {sum}.",end="")


