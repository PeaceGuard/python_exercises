#! /usr/bin/env python3

# Spoj task #17 - Listonosz Franek: https://pl.spoj.com/problems/LISTFRAN/ - Rejected

dataset = input().split()
#"Enter the number of strets and starting point: "

num_streets = int(dataset[0])
start_point = dataset[1]
interm_point = start_point
#count = 0
street = []
hit = 0

for i in range(0, num_streets):
    street.append(input().split())
    #"Enter the start and end point of the street: "

while bool(street) == 1:
    street_len = len(street)
    for element in street:
        if element[0] == interm_point:
            interm_point = element[1]
            street.remove(element)
            print(street)
    if len(street) == street_len:
        break

#for i in range(0, num_streets):
#    while count < 6:
#        street = input("Enter the start and end point of the street: ").split()
#        if street[0] == interm_point:
#            interm_point = street[1]
#            break
#        count +=1

if interm_point == start_point and bool(street) == 0:
    print("TAK")
else:
    print("NIE")