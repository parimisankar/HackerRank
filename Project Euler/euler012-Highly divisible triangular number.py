'''
What is the value of the first triangle number to have over N divisors?
'''
from functools import reduce
from collections import Counter

def n_factors(n):
    # Returns number of factors of a number 'n'
    prime_factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            prime_factors.append(d)
            n /= d
        # skipping check for even numbers other than 2
        if d != 2:
            d = d + 2
        else:
            d = 3
        if d*d > n:
            # appending N, if N itself is a prime 
            if n > 1: prime_factors.append(int(n))
            break
    # Counting number of factors given list of all prime factors
    # Counter(prime_factors).values() gives number of times n is divisible by each prime
    primes = list(Counter(prime_factors).values())
    # add 1 to each of these values
    add_1 = list(map(lambda x: x+1, primes))
    # multiply each of the values in the list only if list is not empty
    product = reduce((lambda x, y: x * y), add_1) if add_1 != [] else 0
    # return the number of factors i.e., product
    return product

n_tri_divisors = []
for _ in range(int(input())):
    N = int(input())
    
    i = len(n_tri_divisors) + 1
    divisors = n_factors(i*(i+1)/2)
    
    while divisors <= N:
        i = i + 1
        tri = i*(i+1)/2
        divisors = n_factors(tri)
        n_tri_divisors.append([tri, divisors])
    
    # Filter out triangular numbers where no. of divisors is over N 
    valid_tri = list(filter(lambda i: i[1] > N, n_tri_divisors))
    # List out triangular numbers only
    tri_only = list(zip(*valid_tri))[0]
    # Print the minimum as an integer
    print(int(min(tri_only)))