#!/usr/bin/env python3
# 52digest.py

import re
import sys
import fileinput
from Bio import SeqIO

#import biopython

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments


#set file path
file_path = sys.argv[1]


# read genbank file
gb_obj=SeqIO.read(file_path,'gb')

#extract all gene sequences
genes=[]
for feature in gb_obj.features:
    if feature.type=='gene':
        genes.append(feature)
#len(genes)

#define gene of interest
gene_of_interest='ORF1ab'
#create empty list to store the extracted gene of interest
hits=[]
#iterate through the genes and select the gene of interest 
for gene in genes:
    if 'gene' in gene.qualifiers.keys():
        if gene_of_interest == gene.qualifiers['gene'][0]:
            hits.append(gene)
            print('gene found')
#len(hits)

rpoB=hits[0]
extracted_sequence=rpoB.extract(gb_obj)
#len(extracted_sequence.seq)

extracted_sequence.id='ORF1ab'


#save the gene sequence to an output fasta file
outputfile='../Data/sars-cov2.fa'
SeqIO.write(extracted_sequence,outputfile,'fasta')



#READ FASTA
#only read lines with nt
var = sys.argv[2]
fp = open(var, 'r')

seq = []
for line in fp:
    if line.startswith('>'): continue
    seq.append(line)

#remove \n
for i,s in zip(range(len(seq)), seq):
	s = s.rstrip()
	seq[i] = s
#join list together
seq1 = ''.join(seq)
#print(seq1)



#EcoRI digest

restriction_pattern = sys.argv[3]

w = len(restriction_pattern)

indexes = []
for i in range(len(seq1) - w +1):
	win = seq1[i:i+w]
	if win == restriction_pattern:
		print(seq1.index(win))
		indexes.append(seq1.index(win))

print(indexes)


seq2 = [*seq1]
print(seq2)

for i in seq2:
	if [i] == indexes[0]:
		segment1 = seq2.split()
	else: continue




indexes1 = [*set(indexes)]
print(indexes1)


x = slice(0,indexes1[0])
y = slice(indexes1[0],len(seq1))
segment1 = (seq1[x])
segment2 = (seq1[y])
print(segment1)
print(segment2)

print(len(segment1))
print(len(segment2))





'''
print(type(seq1))
splits = seq1.split([indexes1])
print(splits)



#parts = [seq1[i:j] for i,j in zip(indexes1, indexes1[1:]+[None])]
#print(parts)

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

'''


"""
python3 52digest.py ../Data/sars-cov2.gb ../Data/sars-cov2.fa GAATTC
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
