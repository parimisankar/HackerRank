import sys

_ = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

def calc_mean(x, n = len(x)):
    sum = 0
    for i in x:
        sum += i
    mean = sum/n
    return mean

def calc_stddev(x, n = len(x), mu = calc_mean(x)):
    smd = 0
    for xi in x:
        smd += ((xi-mu)**2)
    std_dev = (smd/n)**0.5
    return(round(std_dev,1))

std_dev = calc_stddev(x)
print(std_dev)