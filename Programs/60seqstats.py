#!/usr/bin/env python3
# 60seqstats.py

import argparse
import mcb185
import sys
import gzip

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

# required arguments
parser.add_argument('file', type=argparse.FileType('r'))
	
# finalization
arg = parser.parse_args()


fp = mcb185.read_fasta(arg.file)

num_sequences = 0
for line in fp:
	if line.startswith('>'): num_sequences += 1
	else: num_sequences += 0
print(num_sequences)




'''
var = sys.argv[1]
fp = open(var, 'r')


#only read lines with nt
seq = []
for line in fp:
    if line.startswith('>'): continue
    seq.append(line)
    

#remove \n
for i,s in zip(range(len(seq)), seq):
	s = s.rstrip()
	seq[i] = s
'''
'''
fp = open(arg.file, 'r')

num_sequences = 0
for line in fp:
	if line.startswith('>'): num_sequences += 1
	else: num_sequences += 0
print(num_sequences)

print(arg.file.readlines())
'''



#python3 60seqstats.py ../Data/chr1.fa 


