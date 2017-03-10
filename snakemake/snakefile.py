import os
import synapseclient
import synapseutils

#time snakemake --cluster qsub --jobs 10


#for synapse
#parent/project folder synapse ID
SYNPARENTID = "syn3270268"
syn = synapseclient.login()
#create a synapse folder for this BAM folder
#this is the synapse parent folder ID which has BAM folder synapse ID; for pilot use mouse BAM files
BAMFolderSynId = 'syn4486995'
#get all the BAM file IDs
walkedPath = synapseutils.walk(syn, BAMFolderSynId)
BAMNAMELIST = []
BAMIDLIST = []
nameIdDict = {}

#loop thru all the files in the BAM folder
for dirpath, dirname, filename in walkedPath:
	for (bamFileName,bamFileSynId) in filename:
		#for testing process one BAM file
		if bamFileName != '112-10.FCC5F7UACXX_L6_IGTCCGC.snap.bam':
				continue
		BAMNAMELIST.append(bamFileName)
		BAMIDLIST.append(bamFileSynId)
		nameIdDict[bamFileName] = bamFileSynId

print ('BAM ID list:', BAMIDLIST)

rule all:
	input:
		a=expand('/home/centos/p_2/{bamFile}_files_uploaded.txt', bamFile=BAMNAMELIST),

rule download_BAM_File:
	input:
		a='tmp.txt',
	output:
		a='/home/centos/p_2/bamFolderTest_2/{bamFile}'
	run:
		print ('Downloading file synapse ID:',wildcards.bamFile)
		downloadDir = 'bamFolderTest_2'
		entity = syn.get(nameIdDict[wildcards.bamFile], downloadLocation = downloadDir)
		

rule convert_BAM_to_Fastq:
	input:
		#create a results folder 'p_2, 'p_2 is the folder where the output results are directed
		a='/home/centos/p_2/bamFolderTest_2/{bamFile}'
		
	output:
		a = '/home/centos/p_2/{bamFile}.R1.fastq', 
		b = '/home/centos/p_2/{bamFile}.R2.fastq'
	params:
		samToFastqCmd='/home/centos/bin/picard.jar SamToFastq',fastqFolderPath = '/home/centos/p_2/fastqFiles'
	
	shell:
		"""
		java  -jar {params.samToFastqCmd} I={input.a} FASTQ={output.a} SECOND_END_FASTQ={output.b} VALIDATION_STRINGENCY=LENIENT 
		"""	

rule align_star:
	input:
		a = '/home/centos/p_2/{bamFile}.R1.fastq', 
		b = '/home/centos/p_2/{bamFile}.R2.fastq'
	output:
		a = '/home/centos/p_2/{bamFile}_STAR_Aligned.sortedByCoord.out.bam'
		#a = '{bamFile}_STAR_log'
		#b = 'synId_STAR_Log.progress.out'
		#c = 'synId_STAR_Log.final.out'
		#d = 'synId_STAR_SJ.out.tab'
		#e = 'synId_STAR_Log.out'
	params:
		starPath = '/home/centos/miniconda/bin/', outNamePrefix = '{bamFile}_STAR_', numThreads = '8',
		genomeDir='/home/centos/data_2/STAR_MM10'
	shell:
		"""
		{params.starPath}STAR --runThreadN {params.numThreads} --genomeDir {params.genomeDir} --outSAMtype BAM SortedByCoordinate --outFileNamePrefix {params.outNamePrefix} --readFilesIn {input.a} {input.b} ; \
		"""		

rule sort_by_read_name:
	input:
		a = '/home/centos/p_2/{bamFile}_STAR_Aligned.sortedByCoord.out.bam'
	output:
		a = '/home/centos/p_2/{bamFile}_STAR_Aligned.sortedByReadName.bam'		
	params:
		sortCmd = '/home/centos/miniconda/bin/samtools sort'
	shell:
		"""
		{params.sortCmd} -n -o {output.a} {input.a}
		"""
	
rule count_reads_HTSeq:
	input:
		a = '/home/centos/p_2/{bamFile}_STAR_Aligned.sortedByReadName.bam'	
	output:
		a='/home/centos/p_2/{bamFile}_counts.txt'
	params:
		TRANSCRIPTS = '/home/centos/data_2/mm10_ERCC92_tab.gtf', samToolsCmd = '/home/centos/miniconda/bin/samtools',htseqCmd = '/home/centos/miniconda/bin/htseq-count'
	shell:
		"""
		{params.samToolsCmd} view {input.a} |  {params.htseqCmd} -q -s no - {params.TRANSCRIPTS}  >  {output.a}
		"""

rule run_FastQC:
	input:
		a = '/home/centos/p_2/{bamFile}.R1.fastq', 
		b = '/home/centos/p_2/{bamFile}.R2.fastq',
		c = '/home/centos/p_2/{bamFile}_counts.txt'
	output:
		a = '/home/centos/p_2/{bamFile}_FastQC'
	params:
		fastQCCmd = '/home/centos/miniconda/FastQC/fastqc'
	shell:
		"""
		#make the directory
		mkdir {output.a} ;
		{params.fastQCCmd} {input.a} -o {output.a} ; 
		{params.fastQCCmd} {input.b} -o {output.a} ;
		"""

rule upload_files:
	input:
		a = '/home/centos/p_2/{bamFile}_FastQC'
	output:
		a = '/home/centos/p_2/{bamFile}_files_uploaded.txt'
	params:
		parentId = 'syn8395985', resDir='{bamFile}_RNAseq_res', bamId='{bamFile}', synapseCmd='/home/centos/miniconda/bin/synapse'
	shell:
		"""
		{params.synapseCmd} login -u USER -p PASSWORD --rememberMe;
		
		for f in *{params.bamId}*
		do 
			echo "Uploading $f file..";
			printf "Uploading $f file\n" >> {output.a};
			#store folder but will need to add annotations as well from original BAM file
			#synapse store $f --parentId {params.parentId}
			{params.synapseCmd} add $f --parentId {params.parentId};
			#delete file later 
			#rm $f
		done ;
		"""
		
