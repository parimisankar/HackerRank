'''
Find the greatest product of K consecutive digits in the N digit number.
'''
#!/bin/python3

for _ in range(int(input().strip())):
    N, K = input().strip().split(' ')
    N, K = int(N), int(K)
    num = input().strip()
	
    prod = []
    for i in range(len(num) - K + 1):
        product = 1
        for j in range(K):
            product = product*int(num[i+j])
        prod.append(product)
		
    print(max(prod))