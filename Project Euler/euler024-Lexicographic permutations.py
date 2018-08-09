#!/bin/python3
'''
What is the Nth lexicographic permutation of the word 'abcdefghijklm'
Hint: Cantor's Expansion - https://www.programering.com/a/MDMwkDNwATc.html
'''

from math import factorial as fact

for _ in range(int(input())):
    N = int(input())
    # adjusting for zero-indexed
    N -= 1
    result = ""
    
    str = 'abcdefghijklm'
    k = len(str)

    # finding and substituting for each character in string
    for j in range(k):
        deno = fact(k - 1 - j)
        #print(N // deno)
        if N // deno == 0:
            result += str[0]
            str = str[1:]
        else:
            result += str[N // deno]
            str = str[0: N // deno] + str[N // deno + 1: ]
            N = N % deno
    print(result)