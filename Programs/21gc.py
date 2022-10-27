#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

GC_count = 0

for i in range(len(dna)):
	nt = dna[i]
	if nt == "G" or nt == "C":
		GC_count += 1

GC_content = GC_count/len(dna)
print(GC_content)


"""
python3 21gc.py
0.42
0.42
0.42
"""
