#!/bin/bash

# === 2. List of SBATCH arguements ===
#SBATCH --nodes=4
#SBATCH --time=20:00:00
#SBATCH --qos=normal
#SBATCH --partition=smem
#SBATCH --ntasks=1
#SBATCH --job-name=map-job
#SBATCH --output=map-job.%j.out

# === 3. Purge and load needed modules ===
module purge
module load intel/17.4
module load python/3.5.1

# === 4. Additional commands needed to run a program ===
source ./semseg/bin/activate

cd utils

# === 5. Running the program ===
python ./mapillary_val_gen.py $1
