# Given: Six positive integers. The integers correspond to the number of couples in a population possesing each genotype pairing for a given factor.
# (Order shown below)
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, assuming that each couple has exactly two offsprings

import sys

infile = sys.argv[1]
fin = open(infile, 'r')

for line in fin.readlines():
        line = line.strip().split(' ')
        c1, c2, c3, c4, c5, c6 = float(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5])

# c1 = AA-AA;   dom_prob = 1.0  
# c2 = AA-Aa;   dom_prob = 1.0
# c3 = AA-aa;   dom_prob = 1.0
# c4 = Aa-Aa;   dom_prob = 0.75
# c5 = Aa-aa;   dom_prob = 0.5
# c6 = aa-aa;   dom_prob = 0.0

# Assuming that each couple gives rise to exactly two offsprings; 
# E(X) = sigma(k = 1 to n) ((k * P(X = k))
expected_dominant_number = (2*c1*1.0) + (2*c2*1.0) + (2*c3*1.0) + (2*c4*0.75) + (2*c5*0.5)

print expected_dominant_number