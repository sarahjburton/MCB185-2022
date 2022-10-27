#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math
from math import sqrt


num = (sys.argv[1:6])
print(num)

for i,j in zip(num, range(len(num))):
	num[j] = int(i)

print(type(i))

print(num)




#Count
count1 = 0
for i in range(len(num)):
	count1 +=1
print(f'Count: {count1}')


#Mean
sum1 = 0
for i in range(len(num)):
	sum1 += num[i]
mean = sum1 / count1
print(f'Mean: {mean}')



#Std. Dev
for i in range(len(num)):
	std_dev = (num[i] - mean) * (num[i] - mean)
std_dev = sqrt(std_dev/(count1))


#Min & Max
num.sort()
print(f'Minimum: {num[0]}')
print(f'Maximum: {num[-1]}')


#Median
n = len(num)
num.sort() #this lists the numbers in ascending order
if n % 2 == 0: #if number is even, find 2 middle numbers and get avg
    median1 = num[n//2] 
    median2 = num[n//2 - 1]
    median = (median1 + median2)/2
else: #if odd, find just middle number
    median = num[n//2]
print(f'Median: {median}')
	

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""

