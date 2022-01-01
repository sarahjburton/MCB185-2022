#!/usr/bin/env python3

import sys

###############################################################################
#
# Note, you have to run this tutorial with a fasta file on the command line
# python3 10_module.py ../Data/hs_rna.fa
#
###############################################################################

# Move the triple quotes down to uncover new code

"""

# Let's define a useful function

def longest_orf(seq):
	max_start  = None
	max_stop   = None
	max_length = 0
	for frame in range(0, 3):
		for i in range(frame, len(seq)-2, 3):
			codon = seq[i:i+3]
			if codon == 'ATG':
				start = i
				stop = None
				for j in range(i+3, len(seq)-2, 3):
					codon = seq[j:j+3]
					if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
						stop = j
						break
				if stop != None:				
					length = stop - start + 1
					if length > max_length:
						max_length = length
						max_start  = start
						max_stop   = stop
	if max_length > 0:
		return seq[max_start:max_stop+3]
	else:
		return ''

# Let's apply that function to a whole bunch of mRNAs
# Instead of writing code to read a fasta file, let's import it

import mcb185

for name, seq in mcb185.read_fasta(sys.argv[1]):
	print(name, longest_orf(seq))

# The power of modules (libraries) is reusing the same code again and again
# What if you wanted the longest_orf() function in more than one program?
# Put it in a library and import it!
# Go ahead, try that now
# Cut the function out of this program and paste it into the library
# Then replace the print() line above with the line below

#	print(name, mcb185.longest_orf(seq))

"""
