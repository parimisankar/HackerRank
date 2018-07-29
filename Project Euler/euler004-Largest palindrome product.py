#!/bin/python3
'''
Find the largest palindrome made from the product of two 3-digit numbers which is less than given number N.
'''
# Pre-computing list of palindromes of product of 3 digit numbers
palindrome = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        k = i*j
        # Check if the product is 
            # A palindrome, 
            # greater than lowest 6-digit palindrome (101101)
            # lower than largest 6-digit palindrome (999999)
        if int(str(k)[::-1]) == k and k > 101100 and k < 999999:
            palindrome.append(k)

# create a list of unique palindromes and sort it in descending order
palindrome = sorted(list(set(palindrome)),reverse=True)

for _ in range(int(input().strip())):
    N = int(input().strip())
    largest = 0
    for i in range(999,100,-1):
        for j in palindrome:
            # j is a palindrome and product of two 3-digit numbers
            # Check if j is 
                # divisible by i, 
                # quotient is a 3-digit number (between 100 and 1000)
                # less than the input number N
                # the largest valid palindrome
            if j%i == 0 and j//i < 1000 and j//i > 100 and j > largest and j < N:
                largest = j
                break
    print(largest)