import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
w = list(map(int, sys.stdin.readline().split()))
wSum = 0
xwSum = 0
for i in range(n):
    wSum += w[i]
    xwSum += w[i]*x[i]
print(round(xwSum/wSum, 1))