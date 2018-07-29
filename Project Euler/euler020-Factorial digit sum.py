'''
What is the sum of the digits of the factorial of N ?
'''
from math import factorial

def sum_digits(n):
   sum = 0
   while n:
       sum, n = sum + n % 10, n // 10
   return sum

for _ in range(int(input())):
    print(sum_digits(factorial(int(input()))))