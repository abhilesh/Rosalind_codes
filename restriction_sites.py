# Given: A DNA string
# The position and length of every reverse palindrome in the string having length between 4 and 12

import sys

infile = sys.argv[1]
fin = open(infile, 'r')
fout = open('rosalind_revp_out.txt', 'w')

sequence = ''

lines = fin.readlines()
for line in lines:
        if line.startswith('>'):
                sequence = ''
        else:
                sequence += line.rstrip('\n')    # CHECK THIS FASTA PARSER, HOW TO SEPARATE SEQUENCES (THIS WORKS FOR ONE SEQUENCE, NOT FOR MULTIPLE)
seq = sequence

def reverse_complement(seq):
        base_complement = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
        letters = list(seq)
        letters = [base_complement[base] for base in letters]
        complement = ''.join(letters)
        rev_com = complement[::-1]
        return rev_com

index = 0
for i in range(4,13):
        for index in range((len(seq) - i) + 1):
                site = seq[index:index+i]
                site_rev_com = reverse_complement(site)
                if site == site_rev_com:
                        print index + 1, i

fin.close()