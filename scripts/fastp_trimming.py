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
print(logger("creating the read trimming submission script"))
qsub_script = open("read_trimming.sh","w")
qsub_script.write(
"""#!/bin/bash
#SBATCH --job-name=mbov_seq_trim         # Job name
#SBATCH --partition=batch             # Partition (queue) name
#SBATCH --nodes=1
#SBATCH --ntasks=10                    # Run on a single CPU
#SBATCH --mem=50gb                     # Job memory request
#SBATCH --time=2:00:00               # Time limit hrs:min:sec
#SBATCH --output=mbov_trim.%j.out    # Standard output log
#SBATCH --error=mbov_trim.%j.err     # Standard error log

#SBATCH --mail-type=FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=noahausxsapelo2xdump@gmail.com  # Where to send mail

R1=${r1}
R2=${r2}
R1_PAIRED_OUT=${r1_paired_out}
R2_PAIRED_OUT=${r2_paired_out}

cd $SLURM_SUBMIT_DIR

ml fastp

fastp -i $R1 -o $R1_PAIRED_OUT -I $R2 -O $R2_PAIRED_OUT -w 8 
"""
)
qsub_script.close()

#2. run a for loop that will submit every job with a different group of fastq reads
r1 = sorted(glob.glob('*_1.fastq'))
r2 = sorted(glob.glob('*_2.fastq'))
# something new i'm using. lambdas are anonymous functions that don't need a formal name. basically quick and dirty function creation
# saves LOC if the function is relatively simple. here, I'm creating a list of output directory names.
r1_paired = list(map(lambda raw: re.sub('_1.fastq','.paired.trimmed.R1.fastq',raw), r1))
r2_paired = list(map(lambda raw: re.sub('_2.fastq','.paired.trimmed.R2.fastq',raw), r2))

#qsub -v reference=/path/to/reference.fa bash.sh
for i in range(len(r1)):
    os.system("sbatch --export=\"r1={},r2={},r1_paired_out={},r2_paired_out={}\" read_trimming.sh".format(r1[i],r2[i],r1_paired[i],r2_paired[i]))
    print(logger("Read trimming performed on {} {}".format(r1[i],r2[i])))

os.remove("read_trimming.sh")
print(logger("All isolates submitted to the cluster"))
