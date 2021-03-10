#! /usr/bin/env python3

# Spoj task #6 - Która godzina?: https://pl.spoj.com/problems/WWO_01_05/

while True:
    binary_numbers = input()
    binary_sequence = binary_numbers.replace(" ", "")
    lst = str.split(binary_numbers)
    if str.isdigit(binary_sequence) == False:
        print("Please provide only digits divided by spaces")
        continue
    try:
        if int(lst[0], 2) not in range(0, 3) or int(lst[1], 2) not in range(0, 10) or int(lst[2], 2) not in range(0, 6) or int(lst[3], 2) not in range(0, 10):
            print("Please provide binary digits correct for hours and minutes")
            continue
    except ValueError:
        print("Please provide only binary digits")
        continue
    else:
        print(str(int(lst[0], 2)) + str(int(lst[1], 2)) + ":" + str(int(lst[2], 2)) + str(int(lst[3], 2)))
        break

# Missing proofing for hours > 23 & minutes > 59
# QUESTION: Why fail when continuing script after meeting if condition or after quit()?