#!/bin/python3
'''
Count number of days first of a month is sunday between 2 given days
'''
import datetime

for i in range(int(input())):
    count = 0
    Y1, M1, D1 = map(int, input().split())
    Y2, M2, D2 = map(int, input().split())
	
	# Cycle repeats every 1200 years
    if Y1 % 10000 > Y2 % 10000:
        Y1 -= 1200
        Y2 -= 1200
    
	Y1 = Y1 % 10000
    Y2 = Y2 % 10000
    
	D1 = datetime.date(Y1, M1, D1)
    D2 = datetime.date(Y2, M2, D2)
    
	while D1 <= D2:
        while D1.day != 1:
            D1 += datetime.timedelta(days = 1)
        if D1.weekday() == 6:
            count += 1
        if(D1.month == 12):
            D1 = D1.replace(year = D1.year + 1)
            D1 = D1.replace(month = 1)
        else:
            D1 = D1.replace(month = D1.month + 1)
    
	print(count)