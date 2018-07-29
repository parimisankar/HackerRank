#!/bin/python3
'''
Given N, print YES if N can be expressed as sum of two abundant numbers, else print NO.
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
            
        # skipping check for non-prime numbers if already in master_primes
        # skipping check for even numbers other than 2
        k = k+1
        d = master_primes[k] if k < len(master_primes) else d+2 if d != 2 else 3

        if d*d > i:
            # appending N, if N itself is a prime 
            if i > 1: 
                prime_factors.append(i)
                if int(i) not in master_primes:
                    master_primes.append(int(i))
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

abundant_numbers = [12]
master_primes = [2]
max_N = 2
for _ in range(int(input())):
    N = int(input())
    if N > 28123:
        flag = True
    else:
        for i in range(max_N, N+1):
            if i not in abundant_numbers and i not in master_primes:
                # Find sum of proper divisors of i i.e., divisors_sum
                # Check if i < sum_divisors
                if int(sum_of_divisors(i) - i) > i:
                    abundant_numbers.append(i)
        #print(abundant_numbers)
        
        flag = False
        for i in range(int(len(abundant_numbers)/2)+1):
            if N - abundant_numbers[i] in abundant_numbers:
                flag = True
                break
                
        max_N = N if max_N < N else max_N
            
    print('YES' if flag else 'NO')