'''
Given N, Check if there exists any Pythagorean triplet (a,b,c) for which a+b+c = N
Find maximum possible value of abc among all such Pythagorean triplets, If there is no such Pythagorean triplet print -1.
'''
#!/bin/python3

for _ in range(int(input().strip())):
    N = int(input().strip())
    py_triplet_prod = -1
	# since a<b<c and a+b+c = N, Max value of a must be less than N/3
    for a in range(1,round(N/3)):
		# solving equations, a**2 + b**2 = c**2 and a+b+c = N
        b = int((N*N-2*a*N)/(2*N-2*a))
        c = N-a-b
        #print(a,b,c)
		# for a,b,c to be a pythogorean triplet
        if a*a + b*b == c*c:
			# Finding the largest abc
            if a*b*c > py_triplet_prod:
                py_triplet_prod = a*b*c
            #print(a,b,c)
    print(py_triplet_prod)