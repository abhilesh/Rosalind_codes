bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'F F L L S S S S Y Y '' '' C C '' W L L L L P P P P H H Q Q R R R R I I I M T T T T N N K K S S R R V V V V A A A A D D E E G G G G'.split(' ')
codon_table = dict(zip(codons, amino_acids))

def translate (seq):
     peptide = ''
     for i in range(0,len(seq),3):
          codon = seq[i:i+3]
          amino_acid = codon_table.get(codon, '')
          if amino_acid != '':
               peptide += amino_acid
          else:
               break
     return peptide
    
seq = raw_input("Enter the DNA sequence: ")
print translate(seq)