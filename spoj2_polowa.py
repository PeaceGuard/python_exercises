#! /usr/bin/env python3

# Spoj task #2 - POŁOWA: https://pl.spoj.com/problems/POL/ - Accepted

t = int(input())
#"Enter the number of tests: "
words = []

for i in range (0, t):
    words += list(input().split())
    #"Enter a word to halve: "

for element in words:
    half_word = ""
    half_length = int(len(element) / 2)
    for j in range(0, half_length):
        half_word += element[j]
    print(half_word)