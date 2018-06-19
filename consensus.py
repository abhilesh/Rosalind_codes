# Given: A collection of DNA strings of equal length in FASTA format
# Return: A consensus string and profile matrix for the collection.

import sys
import re

infile = sys.argv[1]
fin = open(infile, 'r').read()
fout = open('rosalind_cons_output.txt', 'w')

# Find all continuous stretches of ATGC
#sequences = ["".join(i.splitlines()[1:]) for i in fin.split(">")][1:]
sequences = re.findall("[ATGC]+",fin.replace("\n",""))

profile_matrix = [['A:'],['C:'],['G:'],['T:']]

count_A = count_C = count_G = count_T =  0

seq = sequences[0]

for i in range(len(seq)):
        for j in range(len(sequences)):
                count_A += sequences[j][i].count('A')
                count_C += sequences[j][i].count('C')
                count_G += sequences[j][i].count('G')
                count_T += sequences[j][i].count('T')
        profile_matrix[0].append(count_A)
        profile_matrix[1].append(count_C)
        profile_matrix[2].append(count_G)
        profile_matrix[3].append(count_T)
        count_A = count_C = count_G = count_T = 0

temp_list = []
consensus_seq = ''
for i in range(1,len(profile_matrix[0])):
        for j in range(len(profile_matrix)):
                temp_list.append(profile_matrix[j][i])
        base = max(temp_list)
        index = temp_list.index(base)
        if index == 0:
                consensus_seq += 'A'
        elif index == 1:
                consensus_seq += 'C'
        elif index == 2:
                consensus_seq += 'G'
        else:
                consensus_seq += 'T'
        temp_list = []

fout.write(consensus_seq + '\n')

output = ''

for i in range(len(profile_matrix)):
        for element in profile_matrix[i]:
                output += str(element) + ' '
        fout.write(output + '\n')
        output = ''