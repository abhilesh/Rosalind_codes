def fasta_parse(fp):
     names = []
     sequences = []
     seq = ''
     lines = fp.readlines()
     for line in lines:
          if line.startswith('>'):
               names.append(line.split('|')[1].strip())
               seq = ''
          else:    
               seq = seq + line.rstrip('\n')
               sequences.append(seq)
              
     return names, sequences

open_file = raw_input("Name of the fasta file: ")
fasta_file = open(open_file, 'r')
seq = fasta_parse(fasta_file)
seq_dict = dict(zip(seq[0], seq[1]))

identifiers = seq_dict.keys()
sequences = seq_dict.values()

print identifiers
print sequences