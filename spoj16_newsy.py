#! /usr/bin/env python3

# Spoj task #16 - Newsy: https://pl.spoj.com/problems/MWP4_2E/ - Time limit exceeded

test_num = int(input())
#"Enter the number of tests: "

for i in range(0, test_num):
    dataset = input().split()
    #"Enter the dataset: # of people, # of messages and # of source: "
    #num_people = dataset[0]
    num_messages = int(dataset[1])
    num_of_source = dataset[2]
    chain_members = [num_of_source]
    for j in range(0, num_messages):
        message = input().split()
        #"Enter the message sender and recipient, separated by space: "
        if message[0] in chain_members and message[1] not in chain_members:
            chain_members.append(message[1])
    for element in chain_members:
        print(element)