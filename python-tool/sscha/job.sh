#!/bin/bash


#SBATCH --job-name="p1"
#SBATCH --output="%j.%N.out"
#SBATCH --partition=share,parallel
#SBATCH --nodes=1
#SBATCH -n 20
#SBATCH --export=ALL
#SBATCH -t 48:00:00
#SBATCH --mem=180000

module purge
module load intel2018/icc
module load mkl/19.0.2
module load openmpi/intel/3.1.3


PWEXE=/gpfsnyu/home/yf1159/qe-7.0/bin/pw.x
DOSEXE=/gpfsnyu/home/yf1159/qe-7.0/bin/dos.x
PDOSEXE=/gpfsnyu/home/yf1159/qe-7.0/bin/projwfc.x
PHEXE=/gpfsnyu/home/yf1159/qe-7.0/bin/ph.x


#mpirun -np 20 $PWEXE  -npool 4 < scf.in > scf.out
#touch done

