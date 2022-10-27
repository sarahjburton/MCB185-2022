#!/usr/bin/env python3
# 52digest.py

import re
import sys
import fileinput


#import bio

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments


fp = open(sys.argv[1])

for line in fp.readlines():
	print(line, end='')





'''	
#only read lines with nt
seq = []
for line in fileinput.input():
    if line.startswith(): continue
    seq.append(line)
    
#remove \n
for i,s in zip(range(len(seq)), seq):
	s = s.rstrip()
	seq[i] = s
	

#join list together
seq1 = ''.join(seq)
print(seq1)
'''


#EcoRI digest


seq1 = 'agtcgaattcagtgtagaattcgt' #index should be 4 and 16
restriction_pattern = 'gaattc'
	

#print(re.findall(restriction_pattern, seq1))
#patterns = ''.join(re.findall(restriction_pattern, seq1))
#print(patterns)

#print(seq1.index(re.findall(restriction_pattern, seq1)))

#print(seq1.index(restriction_pattern))

w = len(restriction_pattern)

for i in range(len(seq1) - w +1):
	win = seq1[i:i+w]
	if win == restriction_pattern:
		print(seq1.index(win))




"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
