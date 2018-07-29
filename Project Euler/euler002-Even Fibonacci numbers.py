#!/bin/python3
'''
Find the sum of all the even-valued fibonacci numbers below N
'''
for _ in range(int(input().strip())):
    N = int(input().strip())
    # Hardcoded three fibonacci terms from first even number
	a, b, c = 2, 3, 5
    ans = 0
    if N < 2:
        pass
    else:
        while a < N:
			ans += a
			# Advancing to next 3 fibonacci terms
			# a is always even-valued
            a = b + c
            b = c + a
            c = a + b
    print(ans)