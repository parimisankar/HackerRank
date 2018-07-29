'''
Which starting number, less than or equal to N produces the longest Collatz chain? If many possible such numbers are there print the maximum one.
'''

# Python code not passed all test cases due to space and time limitations.
# Dictionary takes too much space change it to list

# Create a dictionary to memorize(cache) the collatz lengths of each number during calculation
memo = {}                               # initialize the memo dictionary
def collatz_seq(n):
    if not n in memo:                   # check if already computed
        if n == 1:                      # if not compute it
            memo[n] = 1                 # cache it
        elif n % 2 == 0:
            memo[n] = collatz_seq(n // 2) + 1
        else:
            memo[n] = collatz_seq(3*n + 1) + 1
    return memo[n]                      # and return it

# Create a list to save the length of collatz_seq of n
list = [0]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(list),n+1):
        list.append(collatz_seq(i))
	# print answer
    print(max([i for i,x in enumerate(list[:n+1]) if max(list[:n+1]) == x]))