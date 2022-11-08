#!/usr/bin/env python3
# 60seqstats.py

import argparse
import mcb185
import sys
import gzip
import statistics

# Write a program that computes statistics about a fasta file (e.g. assembly)
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library


# setup
parser = argparse.ArgumentParser(description='Compute statistics about a fasta file')


parser.add_argument(
	'--file', '-f', required=True, type=str, metavar='<path>', 
	help='path to sequence file')
	
# finalization
arg = parser.parse_args()


name = mcb185.read_fasta(arg.file)
print(name)
print(next(name))

names = []
seqs = []

#number of sequences
num_sequences = 0
for name, seq in mcb185.read_fasta(arg.file):
	names.append(name)
	seqs.append(seq)
	print(names)
	print(seqs)
	num_sequences += 1
print(num_sequences)

#total length
tot_length = 0
for i in seqs:
	tot_length += len(i)
print(tot_length)

#minimum and maximum lengths
lengths = []
for i in seqs:
	lengths.append(len(i))

minimum = min(lengths)	
print(minimum)

maximum = max(lengths)
print(maximum)


#N50 length (median length of sequence)
median = statistics.median(lengths)
print(median)



#python3 60seqstats.py -f ../Data/chr1.fa.gz


