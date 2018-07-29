'''
Work out the first ten digits of the sum of N 50-digit numbers.
'''
sum = 0
for _ in range(int(input())):
    sum += int(input())
print(str(sum)[0:10])