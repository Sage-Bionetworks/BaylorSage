## Introduction

[Packer](https://www.packer.io/) automates the creation of any type of machine image. Here, we use Bash scripts to provision an Amazon AMI and install necessary software and data. This requires an [Amazon AWS account](https://aws.amazon.com).

This instance has two provisioners:

1. [Software](software_provisioner.sh) which uses [Miniconda](https://conda.io/docs/) to install `fastqc`, `htseq`, and `STAR`. Because of licensing restrictions, `Picard` is downloaded from the Broad Institute.
2. [Data](data_provisioner.sh) gets genomes and transcript gene models.

## Usage

1. Create an [Amazon AWS account](https://aws.amazon.com).
1. [Fork](http://help.github.com/fork-a-repo/) and clone this repository to your machine.
1. Install [packer](http://www.packer.io/docs/installation.html).
1. Amazon AWS credentials are required to be set as environment variables for `AWS_ACCESS_KEY` and `AWS_SECRET_KEY`. 
1. Change the root directory of the repository you cloned, and run:

  ```
  packer build packer/config.json
  ```

If successful, this will create an Amazon AMI in your account that can be used to launch an Amazon EC2 instance.

The system is designed to be used as a single user (`centos`). All software and data is installed for the this user.

## Debugging

If the build fails because an AMI cannot be found, check that source AMI is current, look here: https://github.com/awslabs/cfncluster/blob/master/amis.txt and update the `builders` section `source_ami` in [config.json](config.json).
