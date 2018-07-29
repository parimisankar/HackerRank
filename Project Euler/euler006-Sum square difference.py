#!/bin/python3
'''
Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.
'''
for _ in range(int(input().strip())):
    N = int(input().strip())
    
    # sum of the squares of the first N natural numbers
    sum_of_sq = (N * (N + 1) * (2 * N + 1)) / 6
    
    # square of sum of N naturals numbers
    sum = (N * (N + 1)) / 2
    sq_of_sum = sum ** 2
    
    # Absolute Difference between both
    print(int(abs(sum_of_sq - sq_of_sum)))