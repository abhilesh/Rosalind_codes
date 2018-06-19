# Given: A DNA string s
# Return: Every distinct candidate protein string that can be translated from ORFs of s.

import sys

infile = sys.argv[1]
fin = open(infile, 'r').read()
fout = open('rosalind_orf_out.txt', 'w')

sequences = ["".join(i.splitlines()[1:]) for i in fin.split('>')][1:]

# DNA Codon table

# TTT F      CTT L      ATT I      GTT V
# TTC F      CTC L      ATC I      GTC V
# TTA L      CTA L      ATA I      GTA V
# TTG L      CTG L      ATG M      GTG V
# TCT S      CCT P      ACT T      GCT A
# TCC S      CCC P      ACC T      GCC A
# TCA S      CCA P      ACA T      GCA A
# TCG S      CCG P      ACG T      GCG A
# TAT Y      CAT H      AAT N      GAT D
# TAC Y      CAC H      AAC N      GAC D
# TAA Stop   CAA Q      AAA K      GAA E
# TAG Stop   CAG Q      AAG K      GAG E
# TGT C      CGT R      AGT S      GGT G
# TGC C      CGC R      AGC S      GGC G
# TGA Stop   CGA R      AGA R      GGA G
# TGG W      CGG R      AGG R      GGG G 

bases = ['T', 'C', 'A', 'G']

DNA_codons = [a+b+c for a in bases for b in bases for c in bases]

amino_acids = ['F','F','L','L','S','S','S','S','Y','Y','*','*','C','C','*','W','L','L','L','L','P','P','P','P','H','H','Q','Q',
'R','R','R','R','I','I','I','M','T','T','T','T','N','N','K','K','S','S','R','R','V','V','V','V','A','A','A','A','D','D','E','E','G','G','G','G']

DNA_codon_table = dict(zip(DNA_codons, amino_acids))     # Dictionary representation of the DNA codon table

# Reverse Complement the given string to get the reverse reading frames
def reverse_complement(seq):
        base_complement = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
        letters = list(seq)
        letters = [base_complement[base] for base in letters]
        complement = ''.join(letters)
        rev_com = complement[::-1]
        return rev_com

# Translate the given string from a particular start site to a particular stop site
def translate(seq, start_site, stop_site):
        peptide = ''
        for i in range(start_site, stop_site, 3):
                codon = seq[i:i + 3]
                amino_acid = DNA_codon_table.get(codon, '')
                if amino_acid != '*':
                        peptide += amino_acid
                else:
                        break
        return peptide

seq = sequences[0]
rev_seq = reverse_complement(seq)

# Find all the start sites and stop sites in the DNA string in the forward direction.
fwd_index = 0
fwd_start_site = []
fwd_stop_site = []
while fwd_index < len(seq):
        if seq.find('ATG', fwd_index) not in fwd_start_site and (seq.find('ATG', fwd_index)) != -1:
                fwd_start_site.append(seq.find('ATG', fwd_index))
        if seq.find('TAA', fwd_index) not in fwd_stop_site and (seq.find('TAA', fwd_index)) != -1:
                fwd_stop_site.append(seq.find('TAA', fwd_index))
        if seq.find('TAG', fwd_index) not in fwd_stop_site and (seq.find('TAG', fwd_index)) != -1:
                fwd_stop_site.append(seq.find('TAG', fwd_index))
        if seq.find('TGA', fwd_index) not in fwd_stop_site and (seq.find('TGA', fwd_index)) != -1:
                fwd_stop_site.append(seq.find('TGA', fwd_index))
        fwd_index += 1

fwd_stop_site = sorted(fwd_stop_site)

# Find all the start sites and stop sites in the DNA string in the reverse direction
rev_index = 0
rev_start_site = []
rev_stop_site = []
while rev_index < len(rev_seq):
        if rev_seq.find('ATG', rev_index) not in rev_start_site and (rev_seq.find('ATG', rev_index)) != -1:
                rev_start_site.append(rev_seq.find('ATG', rev_index))
        if rev_seq.find('TAA', rev_index) not in rev_stop_site and (rev_seq.find('TAA', rev_index)) != -1:
                rev_stop_site.append(rev_seq.find('TAA', rev_index))
        if rev_seq.find('TAG', rev_index) not in rev_stop_site and (rev_seq.find('TAG', rev_index)) != -1:
                rev_stop_site.append(rev_seq.find('TAG', rev_index))
        if rev_seq.find('TGA', rev_index) not in rev_stop_site and (rev_seq.find('TGA', rev_index)) != -1:
                rev_stop_site.append(rev_seq.find('TGA', rev_index))
        rev_index += 1

rev_stop_site = sorted(rev_stop_site)

# Find all Open Reading Frames in the forward direction
fwd_reading_frames = []
for site_1 in fwd_start_site:
        for site_2 in fwd_stop_site:
                if (site_2 - site_1)%3 == 0 and site_2 ]]
>
 site_1:  # check that the frame is divisible by 3. This will identify which stop codon will be read
                        frame = (site_1, site_2)
                        fwd_reading_frames.append(frame)
                        break

# Find all Open Reading Frames in the reverse direction
rev_reading_frames = []
for site_1 in rev_start_site:
        for site_2 in rev_stop_site:
                if (site_2 - site_1)%3 == 0 and site_2 ]]
>
 site_1: # above condition plus check if the start site is upstream to the stop site
                        frame = (site_1, site_2)
                        rev_reading_frames.append(frame)
                        break

translated_proteins = []             # Empty list to hold the translated peptides

# Translating in the forward direction
for element in fwd_reading_frames:
        ini_site = element[0]
        ter_site = element[1]
        protein = translate(seq, ini_site, ter_site)
        if protein not in translated_proteins:
                translated_proteins.append(protein)

# Translating in the reverse direction
for element in rev_reading_frames:
        ini_site = element[0]
        ter_site = element[1]
        protein = translate(rev_seq, ini_site, ter_site)
        if protein not in translated_proteins:
                translated_proteins.append(protein)

# Writing the distinct peptide chains to a file
for element in translated_proteins:
        element += '\n'
        fout.write(element)

fout.close()           # close the output file