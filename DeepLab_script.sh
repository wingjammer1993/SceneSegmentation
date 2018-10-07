#!/bin/bash

# === 2. List of SBATCH arguements ===
#SBATCH --nodes=4
#SBATCH --time=00:59:00
#SBATCH --qos=normal
#SBATCH --partition=sgpu
#SBATCH --ntasks=1
#SBATCH --job-name=enet-hue-job
#SBATCH --output=deeplab-hue-job.%j.out

# === 3. Purge and load needed modules ===
module purge
module load intel/17.4
module load python/3.5.1

# === 4. Additional commands needed to run a program ===
source ./semseg/bin/activate

cd Pytorch-Deeplab-master

# === 5. Running the program ===
python ./evaluate.py --data-dir /projects/amra8468/VOCdevkit/VOC2012 --restore-from /projects/amra8468/VOC12_scenes_20000.pth



