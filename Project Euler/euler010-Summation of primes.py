'''
Find the sum of all the primes not greater than given N.
'''
#!/bin/python3
from math import sqrt
def isprime(n):
    '''
    Function to find if n is a prime or not
    Returns True if n is prime else False
    '''
    j = 2
    sq_rt_n = int(sqrt(n))
    while j <= sq_rt_n:
        # check if divisible by j
        if n%j == 0:
            return False
        # skipping even numbers
        if j > 2:
            j += 2
        else:
            j += 1
    return True

# list to store primes and their cumulative sums
prime_summation = [[0,0],[1,0],[2,2]]
for _ in range(int(input().strip())):
    N = int(input().strip())
    num = prime_summation[-1][0]
    while num < N:
        num = num + 1
        if isprime(num):
            sum = num + prime_summation[-1][1]
        prime_summation.append([num, sum])
    print(prime_summation[N][1])