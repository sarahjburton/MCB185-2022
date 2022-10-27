#!/usr/bin/env python3
# 50kmers.py

import sys
import fileinput

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

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
	

#join list together
seq1 = ''.join(seq)
print(seq1)



k = int(sys.argv[2])
#k = 2
print(k)


AA_count = 0
AC_count = 0
AG_count = 0
AT_count = 0
CA_count = 0
CC_count = 0
CG_count = 0
CT_count = 0
GA_count = 0
GC_count = 0
GG_count = 0
GT_count = 0
TA_count = 0
TC_count = 0
TG_count = 0
TT_count = 0

for nt in range(0, len(seq1), k):
	assert(len(seq1) % k == 0)
	kmer = seq1[nt:nt+k]
	if kmer == 'AA': AA_count += 1
	elif kmer == 'AC': AC_count += 1
	elif kmer == 'AG': AG_count += 1
	elif kmer == 'AT': AT_count += 1
	elif kmer == 'CA': CA_count += 1
	elif kmer == 'CC': CC_count += 1
	elif kmer == 'CG': CG_count += 1
	elif kmer == 'CT': CT_count += 1
	elif kmer == 'GA': GA_count += 1
	elif kmer == 'GC': GC_count += 1
	elif kmer == 'GG': GG_count += 1
	elif kmer == 'GT': GT_count += 1
	elif kmer == 'TA': TA_count += 1
	elif kmer == 'TC': TC_count += 1
	elif kmer == 'TG': TG_count += 1
	elif kmer == 'TT': TT_count += 1

tot_count = AA_count + AC_count + AG_count + AT_count + CA_count + CC_count + CG_count + CT_count + GA_count + GC_count + GG_count + GT_count + TA_count + TC_count + TG_count + TT_count

print('AA', AA_count, AA_count/tot_count)
print('AC', AC_count, AC_count/tot_count)
print('AG', AG_count, AG_count/tot_count)
print('AT', AT_count, AT_count/tot_count)
print('CA', CA_count, CA_count/tot_count)
print('CC', CC_count, CC_count/tot_count)
print('CG', CG_count, CG_count/tot_count)
print('CT', CT_count, CT_count/tot_count)
print('GA', GA_count, GA_count/tot_count)
print('GC', GC_count, GC_count/tot_count)
print('GG', GG_count, GG_count/tot_count)
print('GT', GT_count, GT_count/tot_count)
print('TA', TA_count, TA_count/tot_count)
print('TC', TC_count, TC_count/tot_count)
print('TG', TG_count, TG_count/tot_count)
print('TT', TT_count, TT_count/tot_count)


"""
python3 50kmers.py ../Data/chr1.fa 
AA	33657	0.1106
AC	15836	0.0520
AG	18244	0.0600
AT	27223	0.0895
CA	18965	0.0623
CC	10517	0.0346
CG	8147	0.0268
CT	18142	0.0596
GA	19994	0.0657
GC	9673	0.0318
GG	10948	0.0360
GT	16348	0.0537
TA	22344	0.0734
TC	19744	0.0649
TG	19624	0.0645
TT	34869	0.1146
"""
