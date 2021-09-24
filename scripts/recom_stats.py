import numpy as np
import pandas as pd
import re
import argparse

### arguments

parser = argparse.ArgumentParser()
parser.add_argument('-g','--gff',dest='gff',help='path to the recombination GFF file')

args = parser.parse_args()

### logic

gff_input = open(args.gff,"r")

gff_records = []
import_length = []
no_snps = []
for lines in gff_input:
    if lines.startswith("#"):
        continue
    else:
        gff_records.append(lines)
        info = lines.split("\t")
        import_length.append(int(info[4])-int(info[3]))
        no_snps.append(re.search(';snp_count="(.+?)"',lines).group(1))

pd.DataFrame({'Import Length':import_length,'No. SNPs':no_snps}).to_csv('recombination_stats.csv')
print(sum(import_length))