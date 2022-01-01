#!/usr/bin/env python3

import math
import random

# Move the triple quotes downward to uncover each segment of code

"""

# A function is created with the def keyword, a name, and a colon
# All of the statements in a function are indented
# Functions are generally declared at the top of the file
# In this tutorial, they are spread throughout the file

def greeting():
	print('hello')

greeting()

# Functions can take arguments

def greeting1(person):
	print(f'hello {person}')

greeting1('Ian')

# Functions can take multiple arguments

def greeting2(person1, person2):
	print(f'hello {person1} and {person2}')

greeting2('Nigel', 'Derek')

# Functions often return values

def anti(dna):
	seq = ''
	for c in dna[::-1]:
		if   c == 'A': seq += 'T'
		elif c == 'C': seq += 'G'
		elif c == 'G': seq += 'C'
		elif c == 'T': seq += 'A'
		else: seq += 'N'
	return seq

s = 'AAAACGT'
print(s, anti(s))

# Functions can return multiple values

def composition(dna):
	a = dna.count('A') / len(dna)
	c = dna.count('C') / len(dna)
	g = dna.count('G') / len(dna)
	t = dna.count('T') / len(dna)
	return a, c, g, t

nts = composition(s) # returns a tuple
print(nts)
a, c, g, t = composition(s) # unpacking the tuple in named variables
print(a, c, g, t)

# Functions can call themselves!
# This is called recursion
# Recursion can wind your brain into knots at first

def factorial(n):
	if   n == 0: return 1
	elif n == 1: return n
	else:        return n * factorial(n-1)

print(factorial(0), factorial(5))


# ------------------------ Floating Point Math Warning ------------------------

# Numbers in a computer aren't always what they appear

h1 = [0.4, 0.3, 0.2, 0.1]
h2 = [0.1, 0.2, 0.3, 0.4]
s1 = sum(h1)
s2 = sum(h2)
if s1 != s2: print(f'oh no: {s1} {s2}')

# You can use == when comparing integers, but
# NEVER use == when dealing with floating point numbers!
# Instead, ask if the difference between them is small

if math.isclose(s1, s2): print('good enough')
if math.isclose(1.0, 1.1): print('not good enough')

# You can choose your own tolerance between the numbers if you like

if math.isclose(1.0, 1.0, abs_tol=0.01): print('acceptable')


# -------------------------------- Assertions ---------------------------------

# The assert() function is useful for debugging
# It demands that something is true or kills the program
# Last lesson, you made an entropy calculator
# Here's how to make it into a function
# Note the use of assert() and math.isclose()

def entropy(p):
	assert(math.isclose(sum(p), 1.0))
	h = 0
	for v in p:
		h -= v * math.log2(v)
	return h

print(entropy(h1))
#print(entropy([0.2, 0.2, 0.3, 0.4])) # remove comment to observe error


# ------------------------- Advanced Function Syntax --------------------------

# The content below is considered OPTIONAL
# You don't need to program using advanced function syntax
# However, you will run into these concepts, so it's good to know about them


# ----------------------------- Named Parameters ------------------------------

# Functions usually have a fixed number of positional arguments
# But they may also take named arguments
# For example, you have seen this with print() statements

for c in 'acgt':
	print(c, end='-') # prints - instead of finishing line
print() # prints blank line at the end

# Your functions can also have named parameters

def get_codons(seq, frame=0):
	codons = []
	for i in range(frame, len(seq) - 2, 3):
		codons.append(seq[i:i+3])
	return codons

tx = 'ATGCGATAGATACCAGATATAT'
print(get_codons(tx))           # no frame, assumed to be 0
print(get_codons(tx, frame=1))  # use named parameter


# ---------------------------- Variable Parameters ----------------------------

# Functions can take a variable number of parameters

def squares(*values):
	squared = []
	for v in values: squared.append(v * v)
	return squared

print(squares(1))
print(squares(1, 2, 0.5))

# You can even mix variable parameters and named parameters

def pow(*values, power=2):
	results = []
	for v in values: results.append(v ** power)
	return results

print(pow(1, 2, 0.5))
print(pow(1, 2, 0.5, power=3))

# You can even have variable named parameters...
# But not today


# ---------------------------- Generator Functions ----------------------------

# There are times when you want to generate a list of data
# Here's a function that returns a list of random sequences

def randseq(count, length):
	seqs = []
	for i in range(count):
		seq = []
		for j in range(length):
			seq.append(random.choice('ACGT'))
		seqs.append(''.join(seq))
	return seqs

seqs = randseq(5, 7)
print(seqs)

# A list of a few sequences isn't a big deal
# But imagine we want a function to create many large sequences
# The following code may cause your computer to run out of memory!
# Kill it with control-C and comment it out!

seqs = randseq(3000, 1000000) # size of human genome in 1M chunks

# Holding all of those sequences in memory is a lot of work
# Instead of creating all sequences up-front, generate them as needed
# Any function with a 'yield' statement is a generator function
# A 'yield' temporarily stops execution to return value(s)
# Generators improve performance by reducing memory

def seqgen(count, length):
	for i in range(count):
		seq = []
		for j in range(length):
			seq.append(random.choice('ACGT'))
		yield ''.join(seq)

# This works, but it takes a long time to run
# So ^C it and comment it out after trying it

for seq in seqgen(3000, 1000000): print(seq)

# In addition to generator functions, there are generator expressions
# These look a lot like list comprehension
# Except with parentheses instead of square brackets
# This is doubly optional

for r in (random.random() for i in range(10)):
	print(r)

"""
