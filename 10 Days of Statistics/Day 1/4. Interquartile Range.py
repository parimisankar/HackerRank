import sys

_ = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
f = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(len(f)):
    for j in range(f[i]):
        l.append(x[i])
l = sorted(l)
q = [0, 0, 0]

def calc_quartile (x):
    n = len(x)
    if n%2 == 0:
        x_lower = x[:int(n/2)]
        x_upper = x[int(n/2):]
        q = (x_lower[-1]+x_upper[0])/2
    else:
        x_lower = x[:int((n-1)/2)]
        x_upper = x[int((n+1)/2):]
        q = float(x[int(n/2)])
    return x_lower, x_upper, round(q,1)

l_lower, l_upper, q[1] = calc_quartile(l)
_, _, q[0] = calc_quartile(l_lower)
_, _, q[2] = calc_quartile(l_upper)

print(q[2]-q[0])