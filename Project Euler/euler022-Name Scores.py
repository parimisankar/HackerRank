#!/bin/python3
'''
Calculate the Name Score of given name?
Name Score = position of the name in a sorted list multiply by sum of alphabetic positions of each character in name
'''
names = []
for _ in range(int(input())):
    names.append(input().strip())

names.sort()

for _ in range(int(input())):
    name = input().strip()
    name_score = (names.index(name) + 1) * sum([ord(c)-96 for c in name.lower()])
    print(int(name_score))