#!/bin/bash
#SBATCH --job-name=snippy_run         # Job name
#SBATCH --partition=batch             # Partition (queue) name
#SBATCH --ntasks=20                    # Run on a single CPU
#SBATCH --mem=20gb                     # Job memory request
#SBATCH --time=24:00:00               # Time limit hrs:min:sec
#SBATCH --output=snippy_run.%j.out    # Standard output log
#SBATCH --error=snippy_run.%j.err     # Standard error log

#SBATCH --mail-type=BEGIN,END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=noahaus@uga.edu  # Where to send mail	

cd $SLURM_SUBMIT_DIR

sh ./runme.sh
snippy-clean_full_aln core.full.aln > clean.full.aln

