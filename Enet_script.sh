#!/bin/bash

# === 2. List of SBATCH arguements ===
#SBATCH --nodes=4
#SBATCH --time=00:59:00
#SBATCH --qos=normal
#SBATCH --partition=sgpu
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
python ./super_main.py --dataset-dir $1

python ./super_main.py --dataset-dir $1 --color_space GS

python ./super_main.py --dataset-dir $1 --hue_value 10

python ./super_main.py --dataset-dir $1 --hue_value 15

python ./super_main.py --dataset-dir $1 --hue_value 20

python ./super_main.py --dataset-dir $1 --hue_value 25

python ./super_main.py --dataset-dir $1 --hue_value 50

python ./super_main.py --dataset-dir $1 --hue_value 55

python ./super_main.py --dataset-dir $1 --hue_value 60

python ./super_main.py --dataset-dir $1 --hue_value 65

python ./super_main.py --dataset-dir $1 --hue_value 70

python ./super_main.py --dataset-dir $1 --hue_value 75

python ./super_main.py --dataset-dir $1 --hue_value 80

python ./super_main.py --dataset-dir $1 --hue_value 85

python ./super_main.py --dataset-dir $1 --hue_value 90

python ./super_main.py --dataset-dir $1 --hue_value 95

python ./super_main.py --dataset-dir $1 --hue_value 100

python ./super_main.py --dataset-dir $1 --hue_value 105

python ./super_main.py --dataset-dir $1 --hue_value 110

python ./super_main.py --dataset-dir $1 --hue_value 120

python ./super_main.py --dataset-dir $1 --hue_value 125

python ./super_main.py --dataset-dir $1 --hue_value 130

python ./super_main.py --dataset-dir $1 --hue_value 135

python ./super_main.py --dataset-dir $1 --hue_value 140

python ./super_main.py --dataset-dir $1 --hue_value 145

python ./super_main.py --dataset-dir $1 --hue_value 150

python ./super_main.py --dataset-dir $1 --hue_value 155

python ./super_main.py --dataset-dir $1 --hue_value 160

python ./super_main.py --dataset-dir $1 --hue_value 165

python ./super_main.py --dataset-dir $1 --hue_value 170

python ./super_main.py --dataset-dir $1 --hue_value 175

python ./super_main.py --dataset-dir $1 --hue_value 180

python ./super_main.py --dataset-dir $1 --hue_value 185

python ./super_main.py --dataset-dir $1 --hue_value 190

python ./super_main.py --dataset-dir $1 --hue_value 195

python ./super_main.py --dataset-dir $1 --hue_value 200

