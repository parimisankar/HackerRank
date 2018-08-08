#!/bin/python3
'''
How many perfect right-angled triangles with c less than or equal to n exist that are not super-perfect?
'''
# Just print 0 for every query
# Answer: Every perfect triangle is also super-perfect
# Proof: https://luckytoilet.wordpress.com/2010/06/20/on-some-number-theoretic-properties-of-right-triangles-project-euler-218/
for _ in range(int(input())):
    print('0')

'''
from math import gcd, sqrt

def is_square(n):
	# returns True if an integer is a perfect square i.e., square root of N is an integer.
    if int(sqrt(n) + 0.5) ** 2 == n: 
        return True
    else:
        return False
    
for _ in range(int(input())):
    a = 0
    b = 0
    c = 0
    count = 0
    u = 2
    limit = int(input())
    while c <= limit:
        for v in range(1,u):
            a = u*u - v*v
            b = 2*u*v
            c = u*u + v*v
            area = 0.5*a*b
            if is_square(c) and gcd(gcd(a,b),c) == 1 and area%6 !=0 and area%28 !=0:
                count += 1
        u += 1
    print(count)
'''