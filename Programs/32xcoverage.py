#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random


#convert inputs into integers
num = (sys.argv[1:5])
for i,j in zip(num, range(len(num))):
	num[j] = int(i)
	
print(num)
print(type(num))

#generate random seq
genome_size = int(sys.argv[1])
print(genome_size)

one_quart = (0.25)*float(genome_size)
half = (0.50)*float(genome_size)
thr_quart = (0.75)*float(genome_size)

one_quart_int = int(one_quart)
half_int = int(half)
thr_quart_int = int(thr_quart)

seq = []

for i in range(1,genome_size):
	r = random.randint(1,genome_size)
	if r in range(1,one_quart_int): seq.append('A')
	elif r in range(one_quart_int, half_int): seq.append('C')
	elif r in range(half_int, thr_quart_int): seq.append('T')
	else: seq.append('G')

#print(seq)


#generate 100 random chunks of genome 100 times

def get_random_read(seq, read_length):
	idx = random.randrange(0, len(seq) - read_length + 1)
	return seq[idx : (idx + read_length)]

read_length = int(sys.argv[2])
read_number = int(sys.argv[3])

all_random_reads = []
for i in range(0,read_number):
	random_read = get_random_read(seq,read_length)
	all_random_reads.append(random_read)

print(all_random_reads)

#index list
for i in range(0,)



for i in all_random_reads:
	indexing = seq.find(all_random_reads[i])

print(indexing)
	

	


# Find function
start_index_Arrays = string_to_index.find("Arrays")
print(start_index_Arrays)
#output is six


"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
