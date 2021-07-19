## Purpose 
To list the scripts that allow the analyses to occur

## Scripts 
1. *HR_Analysis.Rmd*: An Rmarkdown file that contains the R code that generated figures 
2. *download_fastq.py*: given a list of accession ids, download the accessions from NCBI's Sequence Read Archive
3. *fastp_trimming.py*: uses HPC resources to parallelize fastp read trimming 
4. *snippy_run.sh*: run isolates through the snippy workflow to generate a whole genome alignment
5. *gubbins.sh*: predict regions of homologous recombination amongst isolates 
6. *recom_heatmap.py*: converts gubbins output to a presence/absence heatmap dataframe 
7. *recom_stats.py*: extract stats regarding number of SNPs impacted and length of the recombination region
8. *subalignment.py*: given a full alignment and a list of isolates, create a subalignment of those isolates
