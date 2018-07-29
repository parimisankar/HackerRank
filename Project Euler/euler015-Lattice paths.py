'''
Starting in the top left corner of a Nx M grid, and only being able to move to the right and down, there are exact number of routes to the bottom right corner.
How many such routes are there through a N x M grid? As number of ways can be very large, print it modulo (10**9+7).
'''
from math import factorial as fact

for i in range(int(input())):
    m, n = [int(j) for j in input().split(" ")]
	# Calculate nCm
    print((fact(m + n) // (fact(m) * fact(n))) % 1000000007)