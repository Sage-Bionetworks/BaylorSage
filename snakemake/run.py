import os
import synapseclient
import synapseutils
import glob
import re
import time
from synapseclient import Folder, File

#log in
syn = synapseclient.login()

BAMFolderSynId = 'syn4486995'
print ('BAM folder syn ID:', BAMFolderSynId)
#get all the BAM file IDs
walkedPath = synapseutils.walk(syn, BAMFolderSynId)

noList = []
	
BAMNAMELIST = []
BAMIDLIST = []
nameIdDict = {}
c = 0
for dirpath, dirname, filename in walkedPath:
	for (bamFileName,bamFileSynId) in filename:
		if bamFileName in noList:
			continue
		BAMNAMELIST.append(bamFileName)
		BAMIDLIST.append(bamFileSynId)
		nameIdDict[bamFileName] = bamFileSynId
		c +=  1
		#if c == 10:
			#break 

print ('BAM ID list:', BAMIDLIST)
print ('bam file list:', BAMNAMELIST)

jobScript = 'jobscript.sh'

for fileName in BAMNAMELIST:
	
	#ask for mem_free since STAR needs at least 28G
	cmd = 'qsub -pe smp 1 -l mem_free=28.37G ' + jobScript + ' ' + fileName
	print ('cmd:' + cmd)
	os.system(cmd)
	#sleep to allow job distribution correctly on compute nodes, might not be needed after updating the cfncluster config file
	time.sleep(1000)
