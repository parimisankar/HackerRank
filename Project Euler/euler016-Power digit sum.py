'''
What is the sum of the digits of the number (2**N) ?
'''
from math import pow
def sum_digits(n):
   sum = 0
   while n:
       sum, n = sum + n % 10, n // 10
   return sum

for _ in range(int(input())):
    print(sum_digits(pow(2,int(input()))))