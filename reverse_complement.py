# Given: A DNA string
# Return: The reverse complement of that string

seq = raw_input('Enter the DNA string: ')

def reverse_complement(seq):
        base_complement = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
        letters = list(seq)
        letters = [base_complement[base] for base in letters]
        complement = ''.join(letters)
        rev_com = complement[::-1]
        return rev_com

print reverse_complement(seq)