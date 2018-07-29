#!/bin/python3
'''
What is the largest prime factor of a given number N?
'''
for _ in range(int(input().strip())):
    N = int(input().strip())
    prime_factors = []
    d = 2
    while N > 1:
        while N % d == 0:
            prime_factors.append(d)
            N /= d
		# skipping check for even numbers other than 2
        if d != 2:
			d = d + 2
		else:
			d = 3
        if d*d > N:
			# appending N, if N itself is a prime 
            if N > 1: prime_factors.append(N)
            break
    print(int(max(prime_factors)))