#!/usr/bin/env python3
# 50dictionaries.py

import math
import random

# Move the triple quotes downward to uncover each segment of code



# A dictionary is like a list, but with text instead of numeric indicies

mylist = [3, 4, 7]  # create a list with square brakets
print(mylist[1])    # index with numbers in square brackets

mydict = {'cat': 3, 'dog': 4, 'pig': 7} # create a dict with curly braces
print(mydict['dog'])                    # index with text in square brackets

# Dictionaries have key:value pairs
# You can get all of the keys or values with function

print(mydict.keys())
print(mydict.values())

# There are several ways to loop through a dictionary

for key in mydict: print(key)

for key, val in mydict.items(): print(key, val)

# You can add values to a dictionary by assigning new key:value pairs

mydict['newkey'] = 'newvalue'
print(mydict)

# You can also delete key:value pairs from a dictionary with 'del'

del mydict['newkey']
print(mydict)

# You cannot access a key if it does not yet exist

# print(mydict['foo']) # uncomment this line to see the error

# To check if a key exists, use the 'in' keyword
if 'word' in mydict: print('yes')
else:                print('no')

# Previously, we used the count() function with strings

dna = 'ACGATATACAGATATACYTAT'
a = dna.count('A')
c = dna.count('A')
g = dna.count('A')
t = dna.count('A')
print(a, c, g, t)

# An alternative is to count with a dictionary of letters
# This has the advantage of counting letters you didn't expect

count = {} # create a blank dictionary
for nt in dna:
	if nt not in count: count[nt] = 0
	count[nt] += 1
print(count)

# Dictionaries are really good for looking up values
# They are both very tidy and very efficient
# Let's compare the use of a list and dictionary using a couple functions

# Here's the list-based function
# It computes the Kyte-Doolittle hydropathy of a peptide

def kd_hydropathy1(seq):
	kd = 0
	for aa in seq:
		if   aa == 'I': kd += 4.5
		elif aa == 'V': kd += 4.2
		elif aa == 'L': kd += 3.8
		elif aa == 'F': kd += 2.8
		elif aa == 'C': kd += 2.5
		elif aa == 'M': kd += 1.9
		elif aa == 'A': kd += 1.8
		elif aa == 'G': kd += -0.4
		elif aa == 'T': kd += -0.7
		elif aa == 'S': kd += -0.8
		elif aa == 'W': kd += -0.9
		elif aa == 'Y': kd += -1.3
		elif aa == 'P': kd += -1.6
		elif aa == 'H': kd += -3.2
		elif aa == 'E': kd += -3.5
		elif aa == 'Q': kd += -3.5
		elif aa == 'D': kd += -3.5
		elif aa == 'N': kd += -3.5
		elif aa == 'K': kd += -3.9
		elif aa == 'R': kd += -4.5
	return kd

# Here's the dictionary equivalent

aa2kd = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
	'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
	'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_hydropathy2(seq):
	kd = 0
	for aa in seq: kd += aa2kd[aa]
	return kd

seq = 'MVQYNFKRITVVPNGKEFVDIILSRTQRQTPTVVHKGYKINRLRQFYMRKVKYTQTNFHA'
print(kd_hydropathy1(seq))
print(kd_hydropathy2(seq))

# Now here's a thought question for you
# Where should the aa2kd dictionary be defined?
#    1. outside the function and used globally (as it is here)
#    2. inside the function
#    3. outside the function and passed in as an argument
# There is no single correct answer for this: it depends on the situation

# Sometimes you want to sort a dictionary by keys
# This is done easily with the sorted() function

for k in sorted(aa2kd):
	print(k)

# If you want to sort by value, it's only a little more complicated
for k, v in sorted(aa2kd.items(), key=lambda item: item[1]):
	print(k, v)


