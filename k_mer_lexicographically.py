# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n(n <= 10)
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.

import sys

infile = sys.argv[1]
fin = open(infile, 'r')
lines = fin.readlines()

n = 0
counter = 0

for line in lines:
    line = line.strip()
    if counter == 0:
        alphabet = line.split(' ')
    else:
        n += int(line)
    counter += 1

def lex_order(alphabet, n):
    if n == 2:
        order = [a+b for a in alphabet for b in alphabet]
    if n == 3:
        order = [a+b+c for a in alphabet for b in alphabet for c in alphabet]
    if n == 4:
        order = [a+b+c+d for a in alphabet for b in alphabet for c in alphabet for d in alphabet]
    if n == 5:
        order = [a+b+c+d+e for a in alphabet for b in alphabet for c in alphabet for d in alphabet for e in alphabet]
    if n == 6:
        order = [a+b+c+d+e+f for a in alphabet for b in alphabet for c in alphabet for d in alphabet for e in alphabet for f in alphabet]
    if n == 7:
        order = [a+b+c+d+e+f+g for a in alphabet for b in alphabet for c in alphabet for d in alphabet for e in alphabet \
        for f in alphabet for g in alphabet]
    if n == 8:
        order = [a+b+c+d+e+f+g+h for a in alphabet for b in alphabet for c in alphabet for d in alphabet for e in alphabet \
        for f in alphabet for g in alphabet for h in alphabet]
    if n == 9:
        order = [a+b+c+d+e+f+g+h+i for a in alphabet for b in alphabet for c in alphabet for d in alphabet for e in alphabet \
        for f in alphabet for g in alphabet for h in alphabet for i in alphabet]
    if n == 10:
        order = [a+b+c+d+e+f+g+h+i+j for a in alphabet for b in alphabet for c in alphabet for d in alphabet for e in alphabet \
        for f in alphabet for g in alphabet for h in alphabet for i in alphabet for j in alphabet]
    for element in order:
        print element
    return

print lex_order(alphabet, n)