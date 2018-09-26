#!/bin/bash

# === 2. List of SBATCH arguements ===
#SBATCH --nodes=1
#SBATCH --time=00:59:00
#SBATCH --qos=normal
#SBATCH --partition=shas
#SBATCH --ntasks=1
#SBATCH --job-name=enet-hue-job
#SBATCH --output=enet-hue-job.%j.out

# === 3. Purge and load needed modules ===
module purge
module load intel/17.4
module load python/3.5.1

# === 4. Additional commands needed to run a program ===
source ./semseg/bin/activate

cd PyTorch-ENet-master
# === 5. Running the program ===
python ./super_main.py