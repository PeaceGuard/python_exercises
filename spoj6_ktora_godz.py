#! /usr/bin/env python3

# Spoj task #6 - Która godzina?: https://pl.spoj.com/problems/WWO_01_05/

while True:
    binary_numbers = input()
    binary_sequence = binary_numbers.replace(" ", "")
    lst = str.split(binary_numbers)
    if str.isdigit(binary_sequence) == False:
        print("Please provide only digits")
        continue
    try:
        #
        # if expr1 not in range(z, p) or expr2 not in range(s, t):
        # expr1, expr2 ~~~ (dowolne wyrażeie w tym zmienna) 
        #
        if int(lst[0], 2) not in range(0, 3) or int(lst[1], 2) not in range(0, 10) or int(lst[2], 2) not in range(0, 6) or int(lst[3], 2) not in range(0, 10) or (int(lst[0], 2) == 2 and int(lst[1], 2) not in range(0, 4)):
            print("Please provide binary digits convertable to correct hour & minute values")
            continue
    except ValueError:
        print("Please provide only binary digits")
        continue
    except IndexError:
        print("Please provide four sequences of binary digits separated by spaces")
        continue
    else:
        # maksymalnie 25 znaków w linijce powyżej
        # 0 0 0 0 -> 00:00 a nie 0:0
        print(f"{h}:{m}")
        print(str(int(lst[0], 2)) + str(int(lst[1], 2)) + ":" + str(int(lst[2], 2)) + str(int(lst[3], 2)))
        break

# Additional exception for -numbers?
# QUESTION: Why fail when continuing script after meeting if condition or after quit()?