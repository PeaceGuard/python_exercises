#! /usr/bin/env python3

# Spoj task #6 - Która godzina?: https://pl.spoj.com/problems/WWO_01_05/ - Accepted

while True:
    try:
        binary_numbers = input()
        #"Enter four binary numbers separated by space: "
        binary_list = str.split(binary_numbers)
        # if expr1 not in range(z, p) or expr2 not in range(s, t):
        # expr1, expr2 ~~~ (dowolne wyrażenie w tym zmienna) 
        hour = int(str(int(binary_list[0], 2)) + str(int(binary_list[1], 2)))
        minute = int(str(int(binary_list[2], 2)) + str(int(binary_list[3], 2)))
        if hour not in range(0, 24) or minute not in range(0, 60):
        #if int(binary_list[0], 2) not in range(0, 3) or int(binary_list[1], 2) not in range(0, 10) or int(binary_list[2], 2) not in range(0, 6) or int(binary_list[3], 2) not in range(0, 10) or (int(binary_list[0], 2) == 2 and int(binary_list[1], 2) not in range(0, 4)):
            print("Enter binary digits convertable to correct hour & minute values")
            continue
    except ValueError:
        print("Enter only positive binary digits")
        continue
    except IndexError:
        print("Enter four sequences of binary digits separated by spaces")
        continue
    else:
        # maksymalnie 25 znaków w linijce powyżej
        # 0 0 0 0 -> 00:00 a nie 0:0
        display_hour = str(hour).zfill(2)
        display_minute = str(minute).zfill(2)
        #hours = str(int(binary_list[0], 2)) + str(int(binary_list[1], 2))
        #minutes = str(int(binary_list[2], 2)) + str(int(binary_list[3], 2))
        print(f"{display_hour}:{display_minute}")
        break

# Use of zfill(other than 2)?
# Additional exception for -numbers?