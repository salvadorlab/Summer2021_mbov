#Noah A. Legall
#Salvador Lab
#Description: Trim all the isolates using trimmomatic
#Last Update: April 16th 2021
import sys # use to access arguments
import os # use in order to call commands from the terminal script is called in
import glob # grabs files by name and puts them in a list
import re # we can do regular expression features with this
import time # for time stamps

#0. functions for script
logger = lambda message: "[{}] {}".format(time.strftime('%a %H:%M:%S'),message)

#1. create automatically the submission script for qsub
print(logger("use vsnp for each isolate"))
qsub_script = open("vsnp.sh","w")
qsub_script.write(
"""#!/bin/bash
#SBATCH --job-name=vsnp_run        # Job name
#SBATCH --partition=batch             # Partition (queue) name
#SBATCH --nodes=1
#SBATCH --ntasks=1             # Run on a single CPU
#SBATCH --mem=50gb                     # Job memory request
#SBATCH --time=2:00:00               # Time limit hrs:min:sec
#SBATCH --output=mbov_trim.%j.out    # Standard output log
#SBATCH --error=mbov_trim.%j.err     # Standard error log

#SBATCH --mail-type=FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=noahausxsapelo2xdump@gmail.com  # Where to send mail

R1=${r1}
R2=${r2}
name=${name}

ml Miniconda
ml SAMtools 
source activate /home/noahaus/conda_envs/vsnp_fixed
cd $SLURM_SUBMIT_DIR
mkdir $name
cp $R1 $R2 -t $name
cd $name 

vSNP_step1.py -r1 $R1 -r2 $R2 -skip_assembly -r ~/mbov_reference.fasta
"""
)
qsub_script.close()

#2. run a for loop that will submit every job with a different group of fastq reads
r1 = sorted(glob.glob('*R1.fastq.gz'))
r2 = sorted(glob.glob('*R2.fastq.gz'))
# something new i'm using. lambdas are anonymous functions that don't need a formal name. basically quick and dirty function creation
# saves LOC if the function is relatively simple. here, I'm creating a list of output directory names.
name = list(map(lambda raw: re.sub('.paired.trimmed.R1.fastq','',raw), r1))

#qsub -v reference=/path/to/reference.fa bash.sh
for i in range(len(r1)):
    os.system("sbatch --export=\"r1={},r2={},name={}\" vsnp.sh".format(r1[i],r2[i],name[i]))
    print(logger("snp calling performed on {} {}".format(r1[i],r2[i])))

os.remove("vsnp.sh")
print(logger("All isolates submitted to the cluster"))
