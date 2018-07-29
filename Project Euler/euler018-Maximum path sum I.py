#!/bin/python3
'''
Find the maximum total from top to bottom of the triangle given in input.
Same as Euler 067
'''
for _ in range(int(input())):
    N = int(input())
    if N > 1:
		l= []
		# read the triangle
        for __ in range(N):
            l.append(list(map(int,input().split(" "))))
		# take the bottom most row and the prev row in triangle. for N = 1, there is only one row
        for i in range(N-1,0,-1):
            k, m = l[i-1], l[i]
			# create a new row that contains the max of possible sums for each element
            for j in range(len(k)):
                k[j] = max((k[j]+m[j]),(k[j]+m[j+1]))
        print(k[0])
    else:
        print(int(input()))