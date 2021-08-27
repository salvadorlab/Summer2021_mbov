#compute map for gene lengths of M. bovis
from Bio import SeqIO
import pandas as pd
import re

#dictionary for gene lengths
gene_lengths = {}

gb_file = "sequence.gb"
for gb_record in SeqIO.parse(open(gb_file,"r"), "genbank") :
    # now do something with the record
    print("Name %s, %i features" % (gb_record.name, len(gb_record.features)))
    for f in gb_record.features:
        if f.type == "CDS":
            if "gene" in f.qualifiers:
                genes = f.qualifiers["gene"]
                #print(''.join(genes))
                #print(len(f))
                gene_lengths[''.join(genes)] = len(f)
    
#print(gene_lengths)

#dictionary for bps impacted
bps_impacted = {}
bed_file = "recomb_gene.uniq.tbl"
df = pd.read_table("recomb_gene.uniq.tbl")
#print(hr_impact) 
#loop through rows, extracting length data 

for index, row in df.iterrows():
    name = re.search(';Name=(.+?);',row[3]).group(1)
    #print(name)
    length = int(row[2]) - int(row[1])
    #print(length)
    if name in bps_impacted:
        bps_impacted[name] = bps_impacted[name] + length
    else:
        bps_impacted[name] = length

#print(bps_impacted)   

#calculate percent impacted
for key in bps_impacted:
    try:
        if (bps_impacted[key]/gene_lengths[key])*100.0 <= 100.0:
            print("{},{}".format(key,(bps_impacted[key]/gene_lengths[key])*100))
        else:
            print("{},100.0".format(key))
    except:
        print("{},check".format(key))