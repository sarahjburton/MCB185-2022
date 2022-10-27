#!/usr/bin/env python3
# 30lists.py

import math
import random

# Move the triple quotes downward to uncover each segment of code



# ---------------------------------- Tuples ---------------------------------- #

# Sometimes we want to work with multiple variables at the same time
# A convenient way to do this is a 'tuple'
# Any time you have comma separated values, you have a 'tuple'
# Tuples are often in parentheses but need not be
# Tuples can mix data types

tup = 1, 2.0, 'three' # no parentheses
print(tup)
tup = (1, 2.0, 'three') # same thing with or without parentheses
print(tup)

# You can access any element with square bracket context
# Counting starts at zero, not 1, just like for string indexes

print(tup[0])
print(tup[2])

# Tuples are 'immutable', meaning you can't change their contents

#tup[2] = 3 # uncomment this line to try it out

# ----------------------------------- Lists ---------------------------------- #

# Lists are like tuples, but are mutable (you can change their contents)
# Create lists with square brackets instead of parentheses

arr = [1, 2.0, 'three']
print(arr)

# You can change the content of each item in a list

arr[2] = 3
print(arr)

# You can get a slice of a list, which should look familiar

print(arr[0:2])

# You can change the length of a list with append(), pop(), and insert()

arr.append('four') # adds 'four' to the end of a list
print(arr)

last = arr.pop() # removes the last element of a list and returns it
print(last, arr)

arr.insert(2, 'ok')  # inserts 'ok' at position 2
print(arr)

# Many lists contain numbers, like the following probability distribution

p = [0.2, 0.1, 0.4, 0.3]
print(p)

# sorting is done with the sort() function
p.sort()
print(p)

# sorting also works with text
strings = ['dog', 'cat', 'mouse', 'elephant']
strings.sort()
print(strings)

# sorting doesn't work so well if you mix types
stuff = p + strings
print(stuff)
#stuff.sort() # uncomment this line out to see error

# --------------------------------- sys.argv --------------------------------- #

# The command line is a list

import sys
print(sys.argv) # not very interesting, program name is first item

# Try running this tutorial with some extra words on the command line
# python3 30lists.py 1 3.14

# This is one way you get data from outside your program to inside
# Note that the list is a bunch of strings
# You have to convert them to numbers if you want to do math with them

unit = int(sys.argv[1])
pi = float(sys.argv[2])

# ---------------------------- split() and join() ---------------------------- #

# Strings can be split into lists
t = 'the quick brown fox jumps over the lazy dog'
words = t.split() # default split is on spaces
print(words)

# Lists can be joined into strings
t = '-'.join(words)
print(t)

# --------------------------- Iterating over Lists --------------------------- #

# Note the two ways of iterating over a list
# This should be familiar from strings

sum1 = 0
for x in p:
	sum1 += x

sum2 = 0
for i in range(len(p)):
	sum2 += p[i]

print(sum1, sum2)

# ---------------------------- enumerate() Function ----------------------------

# The enumerate() function returns a tuple of index and item
# when enumerating over a list

dna = 'ACGT'
for thing in enumerate(dna):
	print(thing, thing[0], thing[1]) # pay attention here!

# for i in range(len(dna)):
	#print(i, dna[0], dna[1])
	#difference?

# The 'thing' can be unpacked explicitly into named variables

for i, nt in enumerate(dna):
	print(i, nt)


# ------------------------------- zip() Function -------------------------------

# The zip() function lets you loop through iterables in parallel
# The zip() ends when the first container ends
# This isn't used very often

names = ('Nigel', 'David', 'Derek') # tuple
ages = [52, 53, 49, 1, 2, 3]        # list

for (name, age) in zip(names, ages):
	print(name, age)

# ----------------------------- List Comprehension -----------------------------

# List comprehension is a little confusing and entirely optional

# Consider the following initialization code:

data = []
for i in range(10): data.append(0)
print(data)

# You can write this more succinctly with the * operator

data = [0] * 10
print(data)

# Another alternative is list comprehension

data = [0 for i in range(10)]
print(data)

# List comprehension gets even more interesting...
# Here's a slightly more complex initialization

squares = []
for i in range(10):
	squares.append(i ** 2)
print(squares)

# List comprehension turns 3 lines into 1

squares = [i ** 2 for i in range(10)]
print(squares)

# You can also include a conditional
# First the longer syntax

square3 = []
for i in range(10):
	if i % 3 == 0:
		square3.append(i ** 2)
print(square3)

# Now list comprehension

square3 = [i ** 2 for i in range(10) if i % 3 == 0]
print(square3)

