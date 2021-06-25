#!/bin/bash
#SBATCH --job-name=group_specific_HR         # Job name
#SBATCH --partition=batch             # Partition (queue) name
#SBATCH --ntasks=10                    # Run on a single CPU
#SBATCH --mem=50gb                     # Job memory request
#SBATCH --time=120:00:00               # Time limit hrs:min:sec
#SBATCH --output=group_specific_HR.%j.out    # Standard output log
#SBATCH --error=group_specific_HR.%j.err     # Standard error log

#SBATCH --mail-type=BEGIN,END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=noahaus@uga.edu  # Where to send mail       

ml phipack/1.1
ml Biopython

cd $SLURM_SUBMIT_DIR

python extract_gene_align.py -i full.sub.fa.fa -g ../mbov_annot.gff3
python recombination_hotspots.py

