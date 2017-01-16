# Place for RNAseq reprocessing Code

#come up with conventions for naming propagations


#FASTQ generation

BAM files were reverted to FASTQ using picard.

#FASTQ QC
Basic Fastqc
1) Number of repetitive elements
2) Sequencing quality

Use the outputs for trimming of reads if necessary.

#Alignment
##Human
FASTQ files were aligned to GRCh38 with Gencode24 gene models using STAR/2.5.1b.

##Mouse
FASTQ files were aligned to mm10 with ENSEMBL gene models using STAR/2.5.1b.

##Fruit fly
FASTQ files were aligned to dm6 with UCSC gene models using STAR/2.5.1b.

##iPSC
FASTQ files were aligned to GRCh38 with Gencode24 gene models using STAR/2.5.1b.

#Alignment Metrics
Output from STAR/TopHat

Quantitation
##Human and iPSC
Alignments were counted to Gencode 24 gene models using star - htseq

##Mouse
Alignments were counted to Ensembl gene models using star - htseq

##Fruit fly
Alignments were counted to UCSC gene models using star - htseq
