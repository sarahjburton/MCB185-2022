#!/usr/bin/env python3
# 61dust.py

import argparse
import random
import math
import gzip
from Bio import SeqIO

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(
	description='Low complexity sequence masker')

parser.add_argument(
	'--file', '-f', required=True, type=str, metavar='<path>', 
	help='path to sequence file')

parser.add_argument('--window', required=False, type=int, default=15,
	metavar='<int>', help='optional integer argument [%(default)i]')
	
parser.add_argument('--threshold', required=False, type=float, default=1.100000,
	metavar='<float>', help='Entropy Threshold')
	
parser.add_argument('--lowercase', required=False, type=str, default='N',
	metavar='<str>', help='report lower case instead of N [%(default)s]')
	
arg = parser.parse_args()

def entropy(seq, w):
	for i in range(len(seq) -w +1):
		win = seq[i: i+ w]
		a_ct = 0.00001
		c_ct = 0.00001
		g_ct = 0.00001
		t_ct = 0.00001
		for nt in win:
			p = []
			if nt == 'A': a_ct += 1
			elif nt == 'C': c_ct += 1
			elif nt == 'G': g_ct += 1
			elif nt == 'T': t_ct += 1
			aprob = float(a_ct/w)
			p.append(aprob)
			cprob = float(c_ct/w)
			p.append(cprob)
			gprob = float(g_ct/w)
			p.append(gprob)
			tprob = float(t_ct/w)
			p.append(tprob)
			h = 0
		for i in range(len(p)):
			h -= p[i] * math.log2(p[i])
			if h < 0.0001:
				h = 0
	return h
	
def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

for name, seq in read_fasta(arg.file):
	seq_list = []
	for nt in seq:
		seq_list.append(nt)
	for i in range(len(seq) - arg.window +1):
		win = seq[i:i + arg.window]
		if entropy(win, arg.window) < arg.threshold:
			for j in range(i, i+arg.window):
				seq_list[j] = 'N'
	seq_final = ''.join(seq_list)
	print(f'>{name}')
	print(seq_final)

DNA = f'>Sequence \n{seq_final}'
print(DNA)

saveFASTA = open(r'maskedsequence.fa','w+')
saveFASTA.write(DNA)
saveFASTA.close


# python3 61dust.py --file ../Data/chr1.fa.gz --window 15 --threshold 1.1000
