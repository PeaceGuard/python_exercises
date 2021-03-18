#! /usr/bin/env python3

y = [1]
print(bool(y))
x = 3
print(3 == 3 & 2 == 2)
if ((0 == 0 and 1 == 1) and (2 == 2 or x == 3)):
    print("Yes")
else:
    print("No")

print(isinstance(y, list))

xx = []

print(bool(xx))