#! /usr/bin/env python3

# Spoj task #8 - kot: https://pl.spoj.com/problems/FR_12_09/ - Accepted

sequence = input()
#"Enter a text sequence: "

sequence_len = len(sequence)
times_found = 0

t = 0

while True:
    try:
        k = sequence.index("k", t)
        o = sequence.index("o", k)
        t = sequence.index("t", o)
        times_found += 1
    except ValueError:
        break

if times_found == 0:
    print("NIE")
else:
    print(times_found)

#for sequence.index("k"):
#print(sequence.index("k"))

#for element in sequence:

#enum_sequence = enumerate(sequence, 0)
#for index, element in enum_sequence:
#    if element == "k":
#        hit += 1
        #for index2, element2 in enum_sequence[index, sequence_len]:
        #    if element2 == "o":
        #        hit += 1
        #        for index3, element3 in enum_sequence[index2, sequence_len]:
        #            if element3 == "t":
        #                hit += 1