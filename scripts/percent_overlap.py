from Bio import SeqIO
import pandas as pd
import re

gene_info = {}

gb_file = "../dependencies/sequence.gb"
for gb_record in SeqIO.parse(open(gb_file,"r"), "genbank") :
    for f in gb_record.features:
        if f.type == "CDS":
            if "gene" in f.qualifiers:
                gene_start = f.location._start.position
                gene_end = f.location._end.position
                genes = f.qualifiers["gene"]
                genes = ''.join(genes)
                gene_info[genes] = [tuple((gene_start,gene_end))]
            else:
                gene_start = f.location._start.position
                gene_end = f.location._end.position
                genes = f.qualifiers["locus_tag"]
                genes = ''.join(genes)
                gene_info[genes] = [tuple((gene_start,gene_end))]


#dictionary for bps impacted
bps_impacted = {}
bed_file = "../dependencies/recomb_gene.tbl"
df = pd.read_table("../dependencies/recomb_gene.tbl",header = None)

lengths = []
#loop through rows, extracting length data 
lengths = []
for index, row in df.iterrows():
    for i in range(len(re.findall(';Name=(.+?);',row[3]))):
        try:
            name = re.findall(';Name=(.+?);',row[3])[i]
        except:
            name = "NA"
        if name in bps_impacted:
            bps_impacted[name] = bps_impacted[name] + [tuple((int(row[1]),int(row[2])))]
            
        else:
            bps_impacted[name] = [tuple((int(row[1]),int(row[2])))]
            
    

#calculate percent impacted
print("Gene,Percent overlap of HR")
for key in bps_impacted:
    overlap = 0
    if len(bps_impacted[key]) > 1:
        uniq_overlap = list(set([i for i in bps_impacted[key]]))
        for i in range(len(uniq_overlap)):
            hr_start = uniq_overlap[i][0]
            hr_end = uniq_overlap[i][1]
            

            gene_start = gene_info[key][0][0]
            gene_end = gene_info[key][0][1]

            if hr_start < gene_start:
                start = gene_start
            else:
                start = hr_start
    
            if hr_end > gene_end:
                end = gene_end 
            else:
                end = hr_end 
    
            overlap = overlap + ((end - start))
            
    else: 
        uniq_overlap = bps_impacted[key]
        hr_start = uniq_overlap[0][0]
        hr_end = uniq_overlap[0][1]
    
        gene_start = gene_info[key][0][0]
        gene_end = gene_info[key][0][1]
        if hr_start < gene_start:
            start = gene_start
        else:
            start = hr_start
    
        if hr_end > gene_end:
            end = gene_end 
        else:
            end = hr_end 
    
        overlap = overlap + (end - start)
    print("{},{}".format(key,(overlap/(gene_end - gene_start))*100))


        
