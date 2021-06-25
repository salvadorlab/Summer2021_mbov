#!/bin/bash
#SBATCH --job-name=gubbins_run         # Job name
#SBATCH --partition=batch             # Partition (queue) name
#SBATCH --ntasks=20                    # Run on a single CPU
#SBATCH --mem=50gb                     # Job memory request
#SBATCH --time=24:00:00               # Time limit hrs:min:sec
#SBATCH --output=gubbins_run.%j.out    # Standard output log
#SBATCH --error=gubbins_run.%j.err     # Standard error log

#SBATCH --mail-type=BEGIN,END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=noahaus@uga.edu  # Where to send mail       

cd $SLURM_SUBMIT_DIR

ml Miniconda3/4.7.10

source activate /home/noahaus/conda_envs/gubbins
run_gubbins.py clean.full.aln -v -p mbov_align -o "Reference"
