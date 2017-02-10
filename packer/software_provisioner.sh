#!/bin/bash

wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O $HOME/miniconda.sh
bash $HOME/miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"

# Add to ec2-user's path
echo 'PATH="$HOME/miniconda/bin:$PATH"' >> $HOME/.bashrc

conda install -y star htseq fastqc

mkdir $HOME/bin
wget https://github.com/broadinstitute/picard/releases/download/2.8.3/picard.jar -O $HOME/bin/picard.jar
echo 'PATH="$PATH:$HOME/bin"' >> $HOME/.bashrc
