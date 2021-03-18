#! /usr/bin/env python3

# Sum of first 100 natural numbers, using 'while'

number = 1
total = 0

while number <= 100:
    total += number
    number += 1

print("While: The sum of first 100 natural numbers is " + str(total) + ".")

# Sum of first 100 natural numbers, using 'for'

tot = 0

for num in range(1, 101):
    tot += num

print("For: The sum of first 100 natural numbers is " + str(tot) + ".")


#   Different ways to use print function:
# print("The sum of first 100 natural numbers is " + str(total) + ".")
# print(f"The sum of first 100 natural numbers is {total}.")
# print("The sum of first 100 natural numbers is ", total , ".", sep="")
# print("The sum of first 100 natural numbers is {} {}.".format(-total, "kotek"))
# print("The sum of first 100 natural {yy} numbers is {xx}.".format(xx = total, yy = "kotek"))

#   Different ways to print separate list elements
# sequence = [1, 2, 3, 4, 5, 6]
# print(f"""The sum of first 100 natural numbers is {total} >>> {" ".join(map(str, sequence))}.""")
# print(f'{" ".join(map(str, sequence))}')
# sequence_elements = " ".join(map(str, sequence))
# print(sequence_elements)

#   \ sign deactivates the next sign within the code