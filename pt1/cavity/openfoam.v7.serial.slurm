#!/bin/bash

# See https://docs.tacc.utexas.edu/hpc/frontera/#scripts 
# for more details

#SBATCH -J job      # Job name
#SBATCH -o job.o%j       # Name of stdout output file
#SBATCH -e job.e%j       # Name of stderr error file

### #SBATCH -p normal          # Queue (partition) name

#SBATCH -p development          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes
#SBATCH -n 1               # Total # of mpi tasks
#SBATCH -t 01:00:00        # Run time (hh:mm:ss)

###  #SBATCH --mail-user=youremail@utexas.edu
###  #SBATCH --mail-type=all    # Send email at begin and end of job

#SBATCH -A CTS24005       # Allocation name (req'd if you have more than 1)

# Other commands must follow all #SBATCH directives...

module load openfoam/7.0
module list

pwd
date

./Allrun

date

