import sys # use to access arguments
import os # use in order to call commands from the terminal script is called in
import time # for time stamps

print("[{}] beginning the accession list download".format(time.strftime('%a %H:%M:%S')))
sbatch_script = open("download_fastq.sh","w")
sbatch_script.write(
"""
#!/bin/bash
#SBATCH --job-name=mbov_seq_download         # Job name
#SBATCH --partition=batch             # Partition (queue) name
#SBATCH --nodes=1
#SBATCH --ntasks=1                    # Run on a single CPU
#SBATCH --mem=50gb                     # Job memory request
#SBATCH --time=2:00:00               # Time limit hrs:min:sec
#SBATCH --output=mbov_seq.%j.out    # Standard output log
#SBATCH --error=mbov_seq.%j.err     # Standard error log

#SBATCH --mail-type=BEGIN,END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=noahaus@uga.edu  # Where to send mail

ACC=${accession}
cd $SLURM_SUBMIT_DIR
ml SRA-Toolkit/2.9.1-centos_linux64
fastq-dump --split-3 $ACC
"""
)
sbatch_script.close()

acc_file = sys.argv[1].strip()
acc_list = []
acc = open(acc_file,'r')

for line in acc:
    acc_list.append(line.strip())


#qsub -v reference=/path/to/reference.fa bash.sh
for accession in acc_list:
    os.system("sbatch --export=accession={} download_fastq.sh".format(accession))
    print("[{}] accession {} has been submitted".format(time.strftime('%a %H:%M:%S'),accession))

os.remove("download_fastq.sh")
print("[{}] all accessions are submitted to the cluster".format(time.strftime('%a %H:%M:%S')))
