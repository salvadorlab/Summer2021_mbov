#recombination_hotspots.py

import glob
import os
import re
import subprocess

gene_alignments = sorted(glob.glob("*_output.fna"))
out = open("phi_output.csv","w")
out.write("gene,phi\n")
for gene in gene_alignments:
    #phi = os.popen("Phi -f {} | grep \"PHI (Normal):\"".format(gene)).read()
    com_str = ["Phi","-f",gene]
    com_str2 = ["grep", "PHI (Normal):"]
    pre_phi = subprocess.run(com_str,capture_output=True)
    #print(pre_phi.stdout)
    phi = subprocess.run(com_str2,capture_output=True,input=pre_phi.stdout)
    #print(phi.stdout.decode())
    phi = re.sub("PHI*(Normal):","",phi.stdout.decode())
    gene_name = re.sub("_output.fna","",gene)
    #print("{},{}".format(gene_name,phi))
    out.write("{},{}".format(gene_name,phi))
out.close()
