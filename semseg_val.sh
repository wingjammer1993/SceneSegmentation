#!/bin/bash

# === 2. List of SBATCH arguements ===
#SBATCH --nodes=4
#SBATCH --time=20:00:00
#SBATCH --qos=normal
#SBATCH --partition=sgpu
#SBATCH --ntasks=1
#SBATCH --job-name=semseg-val-job
#SBATCH --output=semseg-val-job.%j.out

# === 3. Purge and load needed modules ===
module purge
module load intel/17.4
module load python/3.5.1

# === 4. Additional commands needed to run a program ===
source ./semseg/bin/activate

cd pytorch-semseg-master

# === 5. Running the program ===
python ./validate.py --config ./configs/$1 --hue -0.5
python ./validate.py --config ./configs/$1 --hue -0.4
python ./validate.py --config ./configs/$1 --hue -0.3
python ./validate.py --config ./configs/$1 --hue -0.2
python ./validate.py --config ./configs/$1 --hue -0.1
python ./validate.py --config ./configs/$1
python ./validate.py --config ./configs/$1 --hue 0.1
python ./validate.py --config ./configs/$1 --hue 0.2
python ./validate.py --config ./configs/$1 --hue 0.3
python ./validate.py --config ./configs/$1 --hue 0.4
python ./validate.py --config ./configs/$1 --hue 0.5

python ./validate.py --config ./configs/$1 --contrast 0
python ./validate.py --config ./configs/$1 --contrast 0.2
python ./validate.py --config ./configs/$1 --contrast 0.4
python ./validate.py --config ./configs/$1 --contrast 0.6
python ./validate.py --config ./configs/$1 --contrast 0.8
python ./validate.py --config ./configs/$1
python ./validate.py --config ./configs/$1 --contrast 1.2
python ./validate.py --config ./configs/$1 --contrast 1.4
python ./validate.py --config ./configs/$1 --contrast 1.6
python ./validate.py --config ./configs/$1 --contrast 1.8
python ./validate.py --config ./configs/$1 --contrast 2.0

python ./validate.py --config ./configs/$1 --gamma 0
python ./validate.py --config ./configs/$1 --gamma 0.2
python ./validate.py --config ./configs/$1 --gamma 0.4
python ./validate.py --config ./configs/$1 --gamma 0.6
python ./validate.py --config ./configs/$1 --gamma 0.8
python ./validate.py --config ./configs/$1
python ./validate.py --config ./configs/$1 --gamma 1.2
python ./validate.py --config ./configs/$1 --gamma 1.4
python ./validate.py --config ./configs/$1 --gamma 1.6
python ./validate.py --config ./configs/$1 --gamma 1.8
python ./validate.py --config ./configs/$1 --gamma 2.0

python ./validate.py --config ./configs/$1 --saturation 0
python ./validate.py --config ./configs/$1 --saturation 0.2
python ./validate.py --config ./configs/$1 --saturation 0.4
python ./validate.py --config ./configs/$1 --saturation 0.6
python ./validate.py --config ./configs/$1 --saturation 0.8
python ./validate.py --config ./configs/$1
python ./validate.py --config ./configs/$1 --saturation 1.2
python ./validate.py --config ./configs/$1 --saturation 1.4
python ./validate.py --config ./configs/$1 --saturation 1.6
python ./validate.py --config ./configs/$1 --saturation 1.8
python ./validate.py --config ./configs/$1 --saturation 2.0

python ./validate.py --config ./configs/$1 --brightness 0
python ./validate.py --config ./configs/$1 --brightness 0.2
python ./validate.py --config ./configs/$1 --brightness 0.4
python ./validate.py --config ./configs/$1 --brightness 0.6
python ./validate.py --config ./configs/$1 --brightness 0.8
python ./validate.py --config ./configs/$1
python ./validate.py --config ./configs/$1 --brightness 1.2
python ./validate.py --config ./configs/$1 --brightness 1.4
python ./validate.py --config ./configs/$1 --brightness 1.6
python ./validate.py --config ./configs/$1 --brightness 1.8
python ./validate.py --config ./configs/$1 --brightness 2.0