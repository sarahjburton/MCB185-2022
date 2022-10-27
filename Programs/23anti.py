#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional



dna = 'ACTGAAAAAAAAAAA'

reverse = ''

for i in dna:
    if i == 'A': reverse = reverse + 'T'
    elif i == 'C': reverse = reverse + 'G'
    elif i == 'G': reverse = reverse + 'C'
    elif i == 'T': reverse = reverse + 'A'
print("DNA:", dna)
print("Complement:", reverse)
print("Reverse Complement:", reverse[::-1])



"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
