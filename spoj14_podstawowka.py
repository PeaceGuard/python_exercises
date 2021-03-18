#! /usr/bin/env python3

# Spoj task #14 - Podstawówka: https://pl.spoj.com/problems/PPODST/ - cannot check, only Perl possible

while True:
    try:
        student_num = int(input("Enter the number of students: "))
    except ValueError:
        print("Enter an integer value")
        continue
    if student_num < 1:
        print("Enter a positive integer value")
        continue
    break

average_sum = 0

for i in range(0, student_num):
    while True:
        try:
            student_list = input("Enter student name, surname and average, separated by spaces: ").split()
#            if not student_list[2].isdecimal:
#                print("Student average should be a floating point number")
#                continue
            average_sum += float(student_list[2],)
        except IndexError:
            print("Enter three arguments separated by spaces")
            continue
        except ValueError:
            print("Student average should be a floating point number")
            continue
        break

average = average_sum / student_num

print("%.2f" % average)

