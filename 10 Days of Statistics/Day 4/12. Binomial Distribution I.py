p = 1.09/2.09
n = 6
x = [3, 4, 5, 6]

def calc_fact(x):
    factorial = 1
    for i in range(x):
        factorial *= i+1
    return factorial

def calc_ncr(x, n, p):
    ncr = calc_fact(n)/(calc_fact(x)*calc_fact(n-x))
    return ncr

binomial = 0
for i in x:
    ncr = calc_ncr(i, n, p)
    binomial += ncr*(p**i)*((1-p)**(n-i))
print(round(binomial,3))