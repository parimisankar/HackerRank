#!/bin/python3
'''
What is the Nth prime number?
'''

def isprime(num):
    '''
    Function to check if a number is prime or not
    '''
    j = 2
    while j <= int(sqrt(num)):
        if num % j == 0:
            return False
        if j == 2:
            j = 3
        else:
            j += 2
    return True

# list of primes
primes = [2]
for _ in range(int(input().strip())):
    N = int(input().strip())
    num = primes[-1]
    prime_count = len(primes)
    
	while prime_count < N:
        num += 1
		# Checking and storing primes
        if isprime(num):
            primes.append(num)
            prime_count += 1
    
	print(primes[N-1])