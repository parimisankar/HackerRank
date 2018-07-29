import sys
import math

lambde = float(sys.stdin.readline())
k = int(sys.stdin.readline())

def calc_fact(x):
    factorial = 1
    for i in range(x):
        factorial *= i+1
    return factorial

def poisson_dist(lambde, k):
    poisson_prob = math.exp(-lambde)*(lambde**k)/calc_fact(k)
    return poisson_prob

poisson_prob = poisson_dist(lambde, k)
print(round(poisson_prob, 3))