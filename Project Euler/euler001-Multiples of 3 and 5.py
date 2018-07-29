#!/bin/python3
'''
Find the sum of all the multiples of 3 or 5 below N
'''
import sys

t = int(input().strip())
for _ in range(t):
    N = int(input().strip())
    ans = 0
	# Number of multiples of 3 below N
    temp = (N - 1) // 3
	# sum of all multiples of 3 below N
    ans += (temp * (3 + temp * 3)) // 2
	# Number of multiples of 5 below N
    temp = (N - 1) // 5
	# sum of multiples of 5 below N
    ans += (temp * (5 + temp * 5)) // 2
    # Number of common multiples of 3 or 5 below N
	temp = (N - 1) // 15
	# sum of common multiples of 3 or 5 below N
    ans -= (temp * (15 + temp * 15)) // 2
	'''
	1-line alternative
	ans = sum(x for x in range(N) if (x % 3 == 0 or x % 5 == 0))
	'''
    print(ans)