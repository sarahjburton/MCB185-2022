#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

dna = ''
dna_len = 30
AT_count = 0

for i in range(dna_len):
	r = random.random()
	if r <= 0.3: 
		dna = dna + 'A'
		AT_count += 1
	elif 0.3 < r <= 0.6:
		dna = dna + 'T'
		AT_count += 1
	elif 0.6 < r <= 0.8:
		dna = dna + 'G'
	elif 0.8 < r <= 1:
		dna = dna + 'C'
			

print(len(dna))
print(AT_count / len(dna))
print(dna)

"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
