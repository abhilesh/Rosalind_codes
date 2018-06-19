# Given: A collection of DNA strings in FASTA format
# Return: The adjacency list corresponding to O_3

# Overlap Graph (O_k) = A directed graph in which each string is represented by a node, and string s and connected to string t \
# with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s != t. 

import sys

infile = sys.argv[1]
fin = open(infile, 'r').read()
fout = open('rosalind_cons_output.txt', 'w')

sequences = ["".join(i.splitlines()[1:]) for i in fin.split(">")][1:]
names = ["".join(i.splitlines()[:1]) for i in fin.split(">")][1:]

seq_dict = dict(zip(sequences, names))

# Compare every sequence's suffix to every other sequence's prefix. Hence, j starts from 0
for i in range(len(sequences)):
        for j in range(len(sequences)):
                if i != j:
                        if (sequences[i][-3:]) == (sequences[j][:3]):
                                node_1 = seq_dict[sequences[i]]
                                node_2 = seq_dict[sequences[j]]
                                print node_1, node_2