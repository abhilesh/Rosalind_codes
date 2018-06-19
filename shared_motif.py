# Given: A collection of k DNA strings
# Return: A longest common substring of the collection

import sys

infile = sys.argv[1]
fin = open(infile, 'r').read()

sequences = [''.join(i.splitlines()[1:]) for i in fin.split('>')][1:]

# Start with the longest motif and keep reducing motif length till a common substring is found. Assuming that the sequences are of equal length

motif_length = len(sequences[0]) - 1 
seq_length = len(sequences[0])

while motif_length ]]
>
 1:
        for i in range(seq_length - 1):
                motif = sequences[0][i:i + motif_length]
                if len(motif) == motif_length:
                        temp_var = [element.find(motif) for element in sequences]
                        if -1 not in temp_var:
                                print motif
                                # This break statement does not do what it is intended to do
                                break
        motif_length = motif_length - 1