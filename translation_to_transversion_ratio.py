# Given: Two DNA strings of equal length 
# Return: The transition to transversion ratio

import sys

infile = sys.argv[1]
fin = open(infile, 'r').read()

sequences = [''.join(i.splitlines()[1:]) for i in fin.split('>')][1:]

seq = sequences[0]
purines = ['A', 'G']
pyrimidines = ['C', 'T']
transitions = 0.0
transversions = 0.0

for i in range(len(seq)):
        for j in range(len(sequences) - 1):
                        if sequences[j][i] == sequences[j + 1][i]:
                                continue
                        elif (sequences[j][i] in purines and sequences[j + 1][i] in purines) or (sequences[j][i] in pyrimidines and sequences[j + 1][i] in pyrimidines):
                                transitions += 1
                        else:
                                transversions += 1

transition_to_transversion = (transitions)/(transversions)

print transition_to_transversion