#!/bin/sh
#
#SBATCH --verbose
#SBATCH --job-name=BeBa
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.err
#SBATCH --time=03:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=100GB
export I_MPI_ADJUST_REDUCE=3

module purge
module load intel/19.1.2
module load openmpi/intel/4.1.1

#sleep 1800s
#srun /home/yf1159/VASP/vasp.5.4.4/bin-general/vasp_std


\rm -f done

touch RUNNING

#srun /home/yf1159/VASP/vasp.5.4.4/bin-general/vasp_std

srun /home/yf1159/VASP/vasp.5.4.4/bin-general/vasp_std
sleep 2s
cp OUTCAR OUTCAR-relax
cp OSZICAR OSZICAR-relax
cp CONTCAR CONTCAR-relax
rm -rf vasprun.xml PROCAR DOSCAR
cp CONTCAR POSCAR
cp INCAR_ELF INCAR
srun /home/yf1159/VASP/vasp.5.4.4/bin-general/vasp_std
rm -rf DOSCAR EIGENVAL WAVECAR CHG* WAVECAR XDATCAR PROCAR IBZKPT
if [ -e ELFCAR ]
then
    gzip ELFCAR
else
    :
fi

touch done
\rm RUNNING
