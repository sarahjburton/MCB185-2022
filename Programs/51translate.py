#!/usr/bin/env python3
# 51translate.py

import sys
import fileinput

# Make a program that translates coding sequences into proteins
# You have been provided with the genetic code as a dictionary
# Use the actin sequence in the Data directory

gcode = {
	'aaa' : 'K',	'aac' : 'N',	'aag' : 'K',	'aat' : 'N',
	'aca' : 'T',	'acc' : 'T',	'acg' : 'T',	'act' : 'T',
	'aga' : 'R',	'agc' : 'S',	'agg' : 'R',	'agt' : 'S',
	'ata' : 'I',	'atc' : 'I',	'atg' : 'M',	'att' : 'I',
	'caa' : 'Q',	'cac' : 'H',	'cag' : 'Q',	'cat' : 'H',
	'cca' : 'P',	'ccc' : 'P',	'ccg' : 'P',	'cct' : 'P',
	'cga' : 'R',	'cgc' : 'R',	'cgg' : 'R',	'cgt' : 'R',
	'cta' : 'L',	'ctc' : 'L',	'ctg' : 'L',	'ctt' : 'L',
	'gaa' : 'E',	'gac' : 'D',	'gag' : 'E',	'gat' : 'D',
	'gca' : 'A',	'gcc' : 'A',	'gcg' : 'A',	'gct' : 'A',
	'gga' : 'G',	'ggc' : 'G',	'ggg' : 'G',	'ggt' : 'G',
	'gta' : 'V',	'gtc' : 'V',	'gtg' : 'V',	'gtt' : 'V',
	'taa' : '*',	'tac' : 'Y',	'tag' : '*',	'tat' : 'Y',
	'tca' : 'S',	'tcc' : 'S',	'tcg' : 'S',	'tct' : 'S',
	'tga' : '*',	'tgc' : 'C',	'tgg' : 'W',	'tgt' : 'C',
	'tta' : 'L',	'ttc' : 'F',	'ttg' : 'L',	'ttt' : 'F', 'tcy' : 'X'
}


fp = open(sys.argv[1])



#only read lines with nt
seq = []
for line in fileinput.input():
    if line.startswith('>'): continue
    seq.append(line)	


#remove \n
for i,s in zip(range(len(seq)), seq):
	s = s.rstrip()
	seq[i] = s
	

#join list together
seq1 = ''.join(seq)
print(seq1)


#Translate

def translation(seq1):
	assert(len(seq1) % 3 == 0)
	pro = []
	for aa in range(0, len(seq1), 3):
		codon = seq1[aa:aa+3]
		pro.append(gcode[codon])
	return ''.join(pro)
	
print(translation(seq1))
		



"""
python3 51translate.py ../Data/act1.fa
MCDDEVAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQ
SKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKM
TQIMFETFNTPAMYVAIQAVLSLYASGRTTGVVLDSGDGVTHTVPIYEGYALPHAILRLD
LAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKX
YELPDGQVITVGNERFRCPEAMFQPSFLGMESAGIHETSYNSIMKCDIDIRKDLYANTVL
SGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISK
QEYDESGPSIVHRKCF*
"""


'''
#remove \n
for i in seq:
	for x in i: 
		if x == '\\': seq.strip('\\')
		elif x == 'n': seq.strip('n')		
#print(seq)
'''
