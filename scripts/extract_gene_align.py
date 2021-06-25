import Bio
from Bio.Seq import Seq
from Bio import AlignIO #to parse the FASTA alignment
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Phylo.PAML import codeml
import os
import argparse
from collections import namedtuple
import re
import string
import random 

### Section 0: set up arguments
parser = argparse.ArgumentParser()
parser.add_argument('-g','--gff',dest='gff',help='the file with gene coordinates')
parser.add_argument('-i','--input',dest='input',help='the FASTA multi-sequence alignment input')
args = parser.parse_args()

Region = namedtuple('Region',['name','start','end','id']) 
print("extracting genes from gff file") 

content = []
letters = string.ascii_lowercase
with open(args.gff) as f:
    for line in f:
        if line.startswith("##"):
            continue
        elif not line.strip():
            break
        else:
            region_parse = line.strip().split("\t")
            if region_parse[2] == 'gene':
                gene_name = re.findall(";Name=(.+);gbkey=",line)[0]
                rand_id = ''.join(random.choice(letters) for i in range(10))
                print("{},{},{}".format(gene_name,region_parse[3],region_parse[4]))
                content.append(Region(gene_name,region_parse[3],region_parse[4],rand_id))
            else:
                continue

print("reading in alignment")
align = AlignIO.read(args.input, "fasta")
#out = open(args.output,"w+")


print("creating nucleotide alignments + phylogenies")
for c in content:
    gene_align = align[:,int(c.start)-1:int(c.end)]
    gene_file = c.name + "_" + c.id + "_output.fna"
    SeqIO.write(gene_align,gene_file,"fasta")
