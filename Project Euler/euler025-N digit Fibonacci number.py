#!/bin/python3
'''
What is the first term in the Fibonacci sequence to contain N digits?
'''
n_digit_fib =[1]
fib = [1,1,2]
count_fib = 1
for _ in range(int(input())):
    N = int(input())
    known_digits = len(n_digit_fib)
    
    while known_digits < N:
        known_digits = len(n_digit_fib)
        fib[0] = fib[1] + fib[2]
        fib[1] = fib[2] + fib[0]
        fib[2] = fib[0] + fib[1]
        count_fib += 3
        
        if len(str(fib[0])) >  known_digits:
            n_digit_fib.append(count_fib)
            known_digits = len(str(fib[0]))
        if len(str(fib[1])) >  known_digits:
            n_digit_fib.append(count_fib+1)
            known_digits = len(str(fib[1]))
        if len(str(fib[2])) >  known_digits:
            n_digit_fib.append(count_fib+2)
            known_digits = len(str(fib[2]))
            
    print(n_digit_fib[N-1])