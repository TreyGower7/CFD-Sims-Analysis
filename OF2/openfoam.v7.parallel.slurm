#!/bin/bash

# See https://portal.tacc.utexas.edu/user-guides/stampede2/#running 
# for more details

#SBATCH -J job      # Job name
#SBATCH -o job.o%j       # Name of stdout output file
#SBATCH -e job.e%j       # Name of stderr error file

### #SBATCH -p normal          # Queue (partition) name
#SBATCH -p development          # Queue (partition) name
### #SBATCH -p skx-normal          # Queue (partition) name

#SBATCH -N 1               # Total # of nodes
#SBATCH -n 2               # Total # of mpi tasks
#SBATCH -t 00:10:00        # Run time (hh:mm:ss)

###  #SBATCH --mail-user=youremail@utexas.edu
###  #SBATCH --mail-type=all    # Send email at begin and end of job

#SBATCH -A CTS24005       # Allocation name (req'd if you have more than 1)

# Other commands must follow all #SBATCH directives...

module purge
module load intel/19.1.1  libfabric/1.7.1  impi/19.0.9 openfoam/7.0
module list

pwd
date

./AllrunParallel

date
