#!/usr/bin/env python3
# 70datastructures.py

import json

# Move the triple quotes downward to uncover each segment of code



# In a 2D list, each element of a list contains another list

list2d = [
	[1, 3, 5],
	[2, 4, 6],
	[3, 6, 9],
]
row = [4, 8, 12]
list2d.append(row)

print(list2d)

# It is common for 2D lists to be rectangular, like the ones above
# But you can have non-rectangular shapes easily

list2d.append([5])
print(list2d)

# A common form of data is the spreadsheet, which might look like this:

# Name  Age   Job
# Ian   54    Professor
# Chris 20    Student
# Jo    31    Developer

# One way to store this is in a 2D list

sheet = [
	['Name', 'Age', 'Job'], # the title line isn't really data though...
	['Ian', 54, 'Professor'],
	['Chris', 20, 'Student'],
	['Jo', 31, 'Developer'],
]

print(sheet[1][1]) # this doesn't feel right...

# Another way to store this is a list of dictionaries
# Each row is a "record"

sheet = [
	{'Name': 'Ian', 'Age': 54, 'Job': 'Professor'},
	{'Name': 'Chris', 'Age': 20, 'Job': 'Student'},
	{'Name': 'Jo', 'Age': 31, 'Job': 'Developer'},
]

for person in sheet:
	print(person['Name']) # much better

# A good way to visualize multidimensional data is in JSON format

print(json.dumps(sheet, indent=4))

# You can also start with JSON and turn it into python

js = '''
{
	"Class": "MCB185",
	"Title": "Programming for Biologists",
	"Instructor": "Ian Korf",
	"Students": [
		{"Name": "Sue D. Monas", "Year": 3},
		{"Name": "Mike R. Cocus", "Year": 4},
		{"Name": "Earl N. Meyer", "Year": 2}
	]
}
'''

jd = json.loads(js)
print(json.dumps(jd, indent=4))


