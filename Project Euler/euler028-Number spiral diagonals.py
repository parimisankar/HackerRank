'''
Find the sum of diagonal numbers in the given odd NxN square
Hint: Ulam Spiral - https://en.wikipedia.org/wiki/Ulam_spiral
'''
'''
# From the diagram, 
# the top right corner always has the value n^2.
# the top left corner has the value n^2 - (n - 1),
# the bottom left corner has the value n^2 - 2(n - 1), 
# and the bottom right is n^2 - 3(n - 1).
# Adding all 4 corners, 4n^2 - 6(n - 1).

# Adding each square, i.e., for all odd n between 1 to n, sum(4n^2-6n+6)
# sum(4n^2-6n+6) = 4*sum(squares of first N odds) - 6*sum(first N odds) + 6*sum(N*1s)

# sum(squares of first N odds ) = (N*(2*N-1)*(2*N+1))/3 ## http://www.9math.com/book/sum-squares-first-n-odd-natural-numbers
# sum(first N odds) = (N)^2 # https://math.stackexchange.com/questions/639068/sum-of-odd-numbers-always-gives-a-perfect-square
# sum(N*1s) = N

# sum(4n^2-6n+6) = (4*(N*(2*N-1)*(2*N+1))/3) - (6*(N)^2) + (6*N)
# sum(4n^2-6n+6) = (16*pow(N,3) - 18*pow(N,2) + 14*N)/3
'''

diag_terms = []
for _ in range(int(input())):
    N = int(input())
    # there will be 2N-1 terms on the diagonals which will include sq(N)
    '''result = 1
    for n in range(3,N+1,2):
        result = result + 4*(n**2) - 6*(n - 1)
    '''
    N = (N+1)//2
    result = (16*pow(N,3) - 18*pow(N,2) + 14*N)//3
    # we are adding 1 in 1x1 square 4 times, reducing result by 3
    # when n = 1, 4n^2 - 6(n - 1) => 4
    result = result - 3
    print(result%(7+10**9))