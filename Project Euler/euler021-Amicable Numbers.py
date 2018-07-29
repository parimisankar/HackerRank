#!/bin/python3
'''
What is sum of all amicable numbers below N?
Hint: https://www.math.upenn.edu/~deturck/m170/wk3/lecture/sumdiv.html
'''
'''
Approach 1: 
# Step 1: Find all the amicable numbers below 10**5+1 i.e., [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856, 12285, 14595, 17296, 18416, 63020, 76084, 66928, 66992, 67095, 71145, 69615, 87633, 79750, 88730]
amicable_numbers = []

for i in range(1,100001):
    if i not in amicable_numbers:
        divisors_sum = int(sum_of_divisors(i) - i)
        sum_divisors = int(sum_of_divisors(divisors_sum) - divisors_sum)
        if sum_divisors == i and divisors_sum != i:
            amicable_numbers.append(i)
            amicable_numbers.append(divisors_sum)
# Step 2: sum all amicable numbers below N
amicable_numbers = [1, 0, 220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856, 12285, 14595, 17296, 18416, 63020, 76084, 66928, 66992, 67095, 71145, 69615, 87633, 79750, 88730]

for _ in range(int(input().strip())):    
    
    n = int(input().strip())
    print(sum([each for each in amicable_numbers if each < n])-1)
'''

from collections import Counter
from operator import mul
from functools import reduce

def prime_factors(i):
    '''
    Function returns a list of all prime factors of N    
    '''
    prime_factors = []
    k = 0
    d = master_primes[k]
    while i > 1:
        while i % d == 0:
            prime_factors.append(d)
            i /= d
        '''# skipping check for even numbers other than 2
        if d != 2:
            d = d + 2
        else:
            d = 3
        '''
        # skipping check for non-prime numbers if already in master_primes
        k = k+1
        if k < len(master_primes):
            d = master_primes[k]
        # skipping check for even numbers other than 2
        elif d !=2:
            d = d + 2
        else:
            d = 3
        if d*d > i:
            # appending N, if N itself is a prime 
            if i > 1: 
                prime_factors.append(i)
                if int(i) not in master_primes:
                    master_primes.append(int(i))
                #master_primes = sorted(set(master_primes))
            break

    # Returning prime factors and their powers
    #print(master_primes)
    return Counter(prime_factors)

def sum_of_divisors(i):
    '''
    Function returns the sum of all divisors of N
    '''
    # Get all prime factors and their powers for N
    primes = prime_factors(i)
    # Calculate the sum of each prime factor
    sum_primes = [(pow(each, (primes[each] + 1)) - 1)/(each - 1) for each in primes.keys()]
    # Return the sum of divisors
    return reduce(mul, sum_primes, 1)

amicable_numbers = []
master_primes = [2]
max_n = 2
for _ in range(int(input().strip())):    
    
    n = int(input().strip())
	# Continuing from precomputed max_n
    for i in range(max_n,n+1):
        if i not in amicable_numbers:
            # Find sum of proper divisors of i i.e., divisors_sum
            divisors_sum = int(sum_of_divisors(i) - i)
            # Find sum of proper divisors of divisors_sum
            sum_divisors = int(sum_of_divisors(divisors_sum) - divisors_sum)
            # Check if i = sum_divisors and avoid cases where sum of proper divisors of i is same as i
            if sum_divisors == i and divisors_sum != i:
                amicable_numbers.append(i)
                amicable_numbers.append(divisors_sum)
    # print the sum of all amicable_numbers below n
    print(sum([each for each in amicable_numbers if each < n]))
    #print(amicable_numbers)
    if max_n < n:
        max_n = n