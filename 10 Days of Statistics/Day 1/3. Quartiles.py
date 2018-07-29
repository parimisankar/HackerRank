import sys

_ = int(sys.stdin.readline())
x = sorted(list(map(int, sys.stdin.readline().split())))
q = [0, 0, 0]
#print(x)
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
    return x_lower, x_upper, int(q)

x_lower, x_upper, q[1] = calc_quartile(x)
_, _, q[0] = calc_quartile(x_lower)
_, _, q[2] = calc_quartile(x_upper)

print(q[0])
print(q[1])
print(q[2])