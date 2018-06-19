def read_fasta(fp):
     order = []
     seq = {}
     for line in fp:
          if line.startswith('>'):
               name = line[1:].rstrip('\n')
               order.append(name)
               seq[name] = ''
          else:
               seq[name] += line.rstrip('\n').rstrip('*')
     return order, seq
    
fasta_file = open("f.fasta", 'r')
new_format = read_fasta(fasta_file)
name = new_format[0]
seq = new_format[1]

sequences = seq.values()

def gc_content(dna):
     g = dna.count("G")
     c = dna.count("C")
     gc = ((g + c)/float(len(dna)))*100
     gc = round(gc, 6)
     return gc

gc = []
    
for i in range(len(sequences)):
     gc.append(gc_content(sequences[i]))

maximum_gc = max(gc)
index = gc.index(maximum_gc)
print name[index]
print maximum_gc