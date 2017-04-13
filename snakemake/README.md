To run the snakemake file using cfncluster compute nodes:
python run.py
This will call the jobscript.sh bash script which will copy the snakemake file to each computing node.

Will need to add the line in the cfncluster config file to force 
each compute node to run a single job only:

[cluster clusterName]
...
extra_json = { "cfncluster" : { "cfn_scheduler_slots" : "1" } }
...
