import Bio
#from Bio import AlignIO #to parse the FASTA alignment
from Bio import SeqIO
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input',dest='input',help='the FASTA multi-sequence alignment input')
parser.add_argument('-s','--samples',dest='samples',help='ids to subset the alignment')
parser.add_argument('-o','--output',dest='output',help='prefix of the subset FASTA alignment')
args = parser.parse_args()

#Just simply, can I get the isolates I want from a list?
#records = (r for r in SeqIO.parse(input_file, "fasta") if r.id.split('|')[2] in wanted)
print("reading in the ids")
content = []
with open(args.samples) as f:
    for line in f:
        content.append(line.strip())

print("reading in alignment")
filtered = []
for record in SeqIO.parse("clean.full.aln","fasta"):
    if record.id in content:
        filtered.append(record)

print("writing sub-alignment")
SeqIO.write(filtered, str(args.output)+".fa", "fasta")
