#!/usr/bin/env python3
# 41files.py

import sys

# Move the triple quotes downward to uncover each segment of code


# The most common way to get data into a program is by reading a file
# Before reading a file you must open it first
# open() associates a file with a 'file pointer' variable
# A file pointer is its own kind of variable type

fp = open(sys.argv[0]) # opening this script itself
print(type(fp))

# You can read a line from a file with the readline() method

line = fp.readline()
print(line)

# Each time you call readline() it reads one more line

line = fp.readline()
for i in range(10):
	line = fp.readline()
	print(i, line, end='')

# If you want to read all of the lines in a file, use readlines()

for line in fp.readlines():
	print('>', line, end='')

# After you're done with a file, you should close it

fp.close()

# Another way to open & close a file is using the 'with' construction
# This creates an open() statement with block structure
# Here, the file pointer is automatically closed after leaving the block

with open(sys.argv[0]) as fp:
	count = 0
	for line in fp.readlines():
		count += 1
	print(count, 'lines in file')

# When you use an open() statement, the file is opened for reading by default
# But you can also write files if you use 'w' as the second argument
# This can be dangerous because it may overwrite a file that already exists

with open('dangerous.txt', 'w') as fp:
	fp.write('overwritten\n')

# Instead of writing named files, you can usually redirect stdout
# python3 your_program.py > your_output


