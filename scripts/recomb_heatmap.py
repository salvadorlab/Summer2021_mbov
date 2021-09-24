import numpy as np
import pandas as pd
import re
import argparse

### arguments

parser = argparse.ArgumentParser()
parser.add_argument('-g','--gff',dest='gff',help='path to the recombination GFF file')
parser.add_argument('-i','--isolates',dest='isolate',help='list of isolate ID\'s')

args = parser.parse_args()

gff_input = open(args.gff,"r")
isolate_input = open(args.isolate,"r")

#put the list of isolates into an actual python list
isolates = []
for lines in isolate_input:
    isolates.append(lines.strip())

gff_records = []
recomb_regions = []
for lines in gff_input:
    if lines.startswith("#"):
        continue
    else:
        gff_records.append(lines)
        info = lines.split("\t")
        recomb_regions.append("{} - {}".format(info[3],info[4]))

heatmap = pd.DataFrame(np.zeros((len(isolates), len(gff_records))),isolates,recomb_regions)
column = list(heatmap)
#print(heatmap.iloc[0:10,0:10])
isolate_region = []
i = 0
for lines in gff_records:
    try:
        isolates_recomb_list = re.search(';taxa="(.+?)"',lines).group(1)
    except:
        isolates_recomb_list = ""
    temp = isolates_recomb_list.split(" ")
    isolate_region = list(filter(lambda a: a != "", temp))
    for isolate in isolate_region:
        heatmap.at[isolate,column[i]] = 1
    i = i + 1
heatmap.to_csv("recombination_heatmap.csv")