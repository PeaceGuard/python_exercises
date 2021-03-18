#! /usr/bin/env python3

# Spoj task #7 - BMI: https://pl.spoj.com/problems/FR_02_06/ - Accepted

underweight_list = []
correctweight_list = []
overweight_list = []

test_num = int(input())
#"Enter the number of students to test: "
for i in range (0, test_num):
    person = str.split(input())
    #"Enter student's name, heigh, weight - all separated by spaces: "
    person_name = person[0]
    person_weight = person[1]
    person_height = int(person[2]) / 100
    bmi = int(person_weight) / (person_height ** 2)
    if bmi < 18.5:
        underweight_list.append(person_name)
    elif bmi >= 18.5 and bmi < 25:
        correctweight_list.append(person_name)
    elif bmi >= 25:
        overweight_list.append(person_name)

print("niedowaga")
for element in underweight_list:
    print(element)
print()

print("wartosc prawidlowa")
for element in correctweight_list:
    print(element)
print()

print("nadwaga")
for element in overweight_list:
    print(element)