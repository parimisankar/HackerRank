#!/bin/python3
'''
Find the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N.
'''
from math import gcd
from functools import reduce

for _ in range(int(input().strip())):
    n = int(input().strip())
    print(reduce(lambda x,y: x*y//gcd(x,y), range(1,n+1)))