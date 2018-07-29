import sys

l = list(map(float, sys.stdin.readline().split()))
x = l[0]
y = l[1]

print(round((160 + 40*(x + (x**2))),3))
print(round((128 + 40*(y + (y**2))),3))