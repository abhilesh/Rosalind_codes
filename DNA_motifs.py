# Given: A DNA sequence and a smaller DNA motif
# Return: All locations of the motif as a subsequence of the DNA sequence

seq = raw_input("Enter the DNA sequence: ")
motif = raw_input("Enter the DNA motif: ")

index = 0
while index < len(seq):
        index = seq.find(motif, index)
        if index == -1:
            break
        print (index + 1)
        index += 1      # Since repeats may overlap