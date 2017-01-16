# Place for RNAseq reprocessing Code


#FASTQ generation

BAM files were reverted to FASTQ using picard.

#Alignment
##Human
FASTQ files were aligned to GRCh38 with Gencode24 gene models using STAR/2.5.1b.

##Mouse
FASTQ files were aligned to mm10 with ENSEMBL gene models using STAR/2.5.1b.

##Fruit fly
FASTQ files were aligned to dm6 with UCSC gene models using STAR/2.5.1b.

##iPSC
FASTQ files were aligned to GRCh38 with Gencode24 gene models using STAR/2.5.1b.

Quantitation
##Human and iPSC
Alignments were counted to Gencode 24 gene models using star.

##Mouse
Alignments were counted to Ensembl gene models using star

##Fruit fly
Alignments were counted to UCSC gene models using star
