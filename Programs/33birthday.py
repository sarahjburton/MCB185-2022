#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Give them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random



'''
def birthdays(num_people, days):
	calendar = [0] * days
	for i in range(0,num_people):
		bday = random.randint(1,days)
		calendar[bday-1] += 1
		bdayrepeat = 0
		for j in calendar:
			if calendar[j] >= 2: bdayrepeat +=1
	probability = bdayrepeat / days
	print(calendar)
	return probability
	
print(birthdays(11,10))

'''

num_people = 25
days = 365
trials = 100



sameday = 0

for m in range(trials):
	calendar = []
	bdayrepeat = 0
	for i in range(days):
		calendar.append(0)
	for j in range(num_people):
		bday = random.randint(0,days-1)
		calendar[bday] += 1
	for x in calendar:
		if x > 1: bdayrepeat +=1
	if bdayrepeat > 0: 
		sameday += 1

probability = (sameday/trials)

print(calendar)
print(bdayrepeat)
print(sameday)

print(probability)






'''

for t in range(trials):
	calendar = []
	for j in range(days): calendar.append(0)
	for i in range(num_people):
		bday = random.randint(1, days)
		calendar[bday-1] += 1
	for x in calendar:
		bdayrepeat = 0
		if x > 1 : bdayrepeat +=1
		
		
list1 = []
for i in range(0,trials):
	list1.append(birthdays())
print(list1)


sum1 = 0
for i in list1:
	sum1 += list1[i]
print(sum1)	


trials = float(trials)

print(type(list1))
print(type(trials))

	
tot_probability = sum1 / trials
print(tot_probability)
	

'''
	








'''


for i in range(0,num_people):
	bday = random.randint(1,365)
	calendar[bday-1] += 1
	bdayrepeat = 0
	for j in calendar:
		if calendar[j] >= 2: bdayrepeat +=1
	
print(calendar)
print(bdayrepeat)

probability = bdayrepeat / days
print(probability)
'''
'''
for j in range(trials):
	for i in range(0,num_people):
		bday = random.randint(1,365)
		calendar[bday-1] += 1
		bdayrepeat = 0
		for j in calendar:
			if calendar[j] >= 2: bdayrepeat +=1
			
			

print(calendar)			
print(bdayrepeat)

'''




'''

mastercalendar = []

'''
'''
for i in range(trials):
	for j in range(0,num_people):
		bday = random.randint(1,365)
		calendar[bday-1] += 1
	mastercalendar.append(calendar)

print(mastercalendar)
'''
'''
count1 = 0
count2 = 0
count3 = 0



for t in range(trials):
	for i in range(num_people):
		bday = random.randint(1,365)
		calendar[bday-1] += 1
	for j in calendar:
		if calendar[j] > 1:
			count1 += 1
		else: count1 += 0
	count2.append(count1)
count3.append(count2)

print(count3)
'''




'''


def birthdays():
	count1 = 0
	for i in range(num_people):
		bday = random.randint(1,365)
		calendar[bday-1] += 1
	for j in calendar:
		if calendar[j] > 1: 
			count1 += 1
		else: count1 += 0
	count2.append(count1)

for i in range(trials):
	birthdays()
count3.append(count2)

print(count2)
print(count3)

	


'''





	
'''
	if calendar[bday-1] > 1
		count1 += 1
	
	
	for j in calendar:
		if calendar[j] > 1:
			count1 += 1
		else: count1 += 0
		count2.append(count1)
	
print(count2)

avg_count = sum(count2) / trials

print(avg_count / trials)

#print(count1)

#print(count1/trials)
'''

	



'''
for i in range(0, days)

#Check if calendar contains any duplicates
def duplicates(calendar):
	if len(calendar) == len(set(calendar)):
		return False
	else:
		return True


if duplicates(calendar) == True:
	num_same_bday += 1
else: num_same_bday += 0


print(overlap / trials)
  



"""
python3 33birthday.py
0.571
"""
'''

'''
num_people = 25
num_days = 365
num_trials = 100

def generate_bday():
	bday = random.randint(1,num_days)
	return bday

def generate_n_bdays(n):
	bdays = generate_bday() for i in range(n)
	return bdays

def aloc(bdays)
	unique_bdays = set(bdays)
	
	num_bdays = len(bdays)
	num_unique_bdays = len(unique_bdays)
	same_bday = (num_bdays != num_unique_bdays)
	
	return same_bday

def estimate_prob():
	num_same_bday = 0
	for i in range(num_trials)
		birthdays = generate_n_birthdays(num_people)
		same_bday = aloc(bdays)
'''

