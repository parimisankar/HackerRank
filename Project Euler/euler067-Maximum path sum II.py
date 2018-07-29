#!/bin/python3
'''
Find the maximum total from top to bottom of the triangle given in input.
Same as Euler 018
'''
for _ in range(int(input())):
    N = int(input())
    if N > 1:
		l= []
        for __ in range(N):
            l.append(list(map(int,input().split(" "))))
        for i in range(N-1,0,-1):
            k, m = l[i-1], l[i]
            for j in range(len(k)):
                k[j] = max((k[j]+m[j]),(k[j]+m[j+1]))
        print(k[0])
    else:
        print(int(input()))