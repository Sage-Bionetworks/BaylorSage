echo homo_sapiens mus_musculus drosophila_melanogaster | sed -e 's/\s\+/\n/g' | xargs -n 1 -I{} sh -c 'mkdir -p $HOME/data/genomes/{} $HOME/data/gene_models/{}'

# Get genomes
curl ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_24/GRCh38.p5.genome.fa.gz > $HOME/data/genomes/homo_sapiens/GRCh38.p5.genome.fa.gz
rsync -avzP rsync://hgdownload.cse.ucsc.edu/goldenPath/dm6/bigZips/dm6.fa.gz $HOME/data/genomes/drosophila_melanogaster
rsync -avzP rsync://hgdownload.cse.ucsc.edu/goldenPath/mm10/bigZips/chromFa.tar.gz $HOME/data/genomes/mus_musculus

# Get gene models
curl ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_24/gencode.v24.annotation.gff3.gz > $HOME/data/gene_models/homo_sapiens/gencode.v24.annotation.gff3.gz
curl ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_24/gencode.v24.annotation.gtf.gz > $HOME/data/gene_models/homo_sapiens/gencode.v24.annotation.gtf.gz
