#!/usr/bin/env python3

import sys
import fileinput

# Make a program that reports the amino acid composition in a file of proteins


fp = open(sys.argv[1])

misc = []
aaseq = []

for line in fileinput.input():
    if line.startswith('>'): continue
    aaseq.append(line)	

print(aaseq)
		

W_count = 0
C_count = 0
H_count = 0
M_count = 0
Y_count = 0
Q_count = 0
F_count = 0
N_count = 0
P_count = 0
T_count = 0
R_count = 0
I_count = 0
D_count = 0
G_count = 0
A_count = 0
K_count = 0
E_count = 0
V_count = 0
L_count = 0
S_count = 0

for i in aaseq:
	for x in i: 
		if x == 'W': W_count += 1
		elif x == 'C': C_count += 1
		elif x == 'H': H_count += 1
		elif x == 'M': M_count += 1
		elif x == 'Y': Y_count += 1	
		elif x == 'Q': Q_count += 1
		elif x == 'F': F_count += 1
		elif x == 'N': N_count += 1
		elif x == 'P': P_count += 1	
		elif x == 'T': T_count += 1
		elif x == 'R': R_count += 1
		elif x == 'I': I_count += 1
		elif x == 'D': D_count += 1
		elif x == 'G': G_count += 1	
		elif x == 'A': A_count += 1	
		elif x == 'K': K_count += 1
		elif x == 'E': E_count += 1
		elif x == 'V': V_count += 1
		elif x == 'L': L_count += 1	
		elif x == 'S': S_count += 1	
		else: misc.append([i])

totaa = W_count + C_count + H_count + M_count + Y_count + Q_count + F_count + N_count + P_count + T_count + R_count + I_count + D_count + G_count + A_count + K_count + E_count + V_count + L_count + S_count

print('W', W_count, W_count/totaa)
print('C', C_count, C_count/totaa)
print('H', H_count, H_count/totaa)
print('M', M_count, M_count/totaa)
print('Y', Y_count, Y_count/totaa)
print('Q', Q_count, Q_count/totaa)
print('F', F_count, F_count/totaa)
print('N', N_count, N_count/totaa)
print('P', P_count, P_count/totaa)
print('T', T_count, T_count/totaa)
print('R', R_count, R_count/totaa)
print('I', I_count, I_count/totaa)
print('D', D_count, D_count/totaa)
print('G', G_count, G_count/totaa)
print('A', A_count, A_count/totaa)
print('K', K_count, K_count/totaa)
print('E', E_count, E_count/totaa)
print('V', V_count, V_count/totaa)
print('L', L_count, L_count/totaa)
print('S', S_count, S_count/totaa)
										

"""
python3 40aacomp.py ../Data/at_prots.fa
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""


