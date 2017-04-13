#!/bin/sh

#fileName=$1
#change home directory
homeDir='/home/centos/p_3'

#make a job dir in the tmp directory
#export TMPDIR=/tmp/$1'_results'
#mkdir -p $TMPDIR

export TMPDIR='/tmp'

#move to tmp dir
cd $TMPDIR

#cp the snake file to tmpdir
cp $homeDir'/Snakefile' $TMPDIR

#touch the need file
touch $TMPDIR/need.txt

source /home/centos/miniconda/envs/py3k/bin/activate py3k
#logFileName=$1'_snakemake.log'

snakemake --force  -j --nolock --config inFileName=$1 

exit 0
