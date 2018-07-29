import sys

x = list(map(int, sys.stdin.readline().split()))
p = x[0]/100
N = x[1]

def calc_fact(x):
    factorial = 1
    for i in range(x):
        factorial *= i+1
    return factorial

def calc_ncr(x, n, p):
    ncr = calc_fact(n)/(calc_fact(x)*calc_fact(n-x))
    return ncr

def calc_binomial(x, N, p, atmost):

    if atmost:
        i = 0
    else:
        i = x
        x = N

    binomial = 0
    while (i <= x):
        ncr = calc_ncr(i, N, p)
        binomial += ncr*(p**i)*((1-p)**(N-i))
        i += 1
    return binomial

rejects = 2
atmost_rejects = calc_binomial(rejects, N, p, atmost=True)
atleast_rejects = calc_binomial(rejects, N, p, atmost=False)

print(round(atmost_rejects,3)) # atmost - no more than #rejects
print(round(atleast_rejects,3)) # atleast