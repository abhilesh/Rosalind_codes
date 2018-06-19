# Given: A DNA string s and a collection of substrings of s acting as introns. All strings are given in FASTA format.
# Output: A protein string resulting from transcribing and translating the exons of s

import sys
from translation import translate

infile = sys.argv[1]

fin = open(infile, 'r')

lines = fin.readlines()

counter = 0
sequence = ''
introns = []

for line in lines:
        line = line.strip('\n')
        if line[0] == '>':
                counter += 1
        if counter == 1 and line[0] != '>':
                sequence += line
        else:
                if line[0] != '>':
                        introns.append(line)

exons = sequence.replace(introns[0], '')

for i in range(1, len(introns)):
        exons = exons.replace(introns[i], '')

exons_RNA = exons.replace('T','U')

introns_len = 0
for i in range(len(introns)):
        introns_len += len(introns[i])
        
assert(introns_len == len(sequence) - len(exons))

peptide = translate(exons_RNA)
print peptide