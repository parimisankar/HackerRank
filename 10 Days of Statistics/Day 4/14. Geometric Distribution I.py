import sys

x = list(map(int, sys.stdin.readline().split()))
p = x[0] / x[1]
N = int(sys.stdin.readline())

def geo_dist(n, p):
    geo_prob = ((1 - p) ** (n - 1)) * p
    return geo_prob

i = 1
sum = 0
while (i <= N):
    sum += geo_dist(i, p)
    i += 1

print(round(sum, 3))