## Purpose 
To list the scripts that allow the analyses to occur

## Scripts 
1. *HR_Analysis.Rmd*: An Rmarkdown file that contains the R code that generated figures for the analysis
2. *download_fastq.py*: given a list of accession ids, download the accessions from NCBI's Sequence Read Archive
3. *fastp_trimming.py*: uses HPC resources to parallelize fastp read trimming 
4. *vsnp.py*: run isolates through the USDA vSNP pipeline workflow to generate variants
5. *gubbins.sh*: predict regions of homologous recombination amongst isolates 
6. *recomb_heatmap.py*: converts gubbins output to a presence/absence heatmap dataframe 
7. *recom_stats.py*: extract stats regarding number of SNPs impacted and length of the recombination region
8. *hr_region_num.py*: this simple script goes through the recombination heatmap and sums the number of present recombination regions per sample
9. *subalignment.py*: given a full alignment and a list of isolates, create a subalignment of those isolates
10. *percent_overlap.py*: compute the overlap of HR regions with genes
