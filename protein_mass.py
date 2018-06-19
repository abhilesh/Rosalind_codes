# Given : A protein string
# Retun : The total weight of P, according to the monoisotopic mass table

import sys

amino_acids = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

weights = [71.03711,103.00919,115.02694,129.04259,147.06841,57.02146,137.05891,113.08406,128.09496,113.08406,131.04049,
114.04293,97.05276,128.05858,156.10111,87.03203,101.04768,99.06841,186.07931,163.06333]

protein_mass = dict(zip(amino_acids, weights))

def calculate_protein_mass(seq):
    weight = 0.0
    for i in range(0, len(seq)):
        residue = seq[i]
        mass = (protein_mass.get(residue, ''))
        weight += mass
    return weight
    
infile = sys.argv[1]
fin = open(infile, 'r')
seq = fin.read().strip()

protein_weight = calculate_protein_mass(seq)
print protein_weight

fin.close(