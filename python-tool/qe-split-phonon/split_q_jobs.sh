#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
# [Usage] ./split_q_jobs.sh
# [Purpose] split phonon calculations for quantum espresso (pwscf)
#          History
#  HISTORY dd/mm/yy
#     2018 : Script creation
#  10/08/2022: preparation of the input and job script, and sbatch jobs in one shot
# -----------------------------------------------------------------

#---------------------------------------------------------------------------------------

# Warn the users to examine their script again
while true; do
    read -p "Did you check your script carefully? " yn
    case $yn in
        [Yy]* ) break;; # exit the loop
        [Nn]* ) echo "check q-points, prefix, fildvscf, tr2_ph, job names, cpu cores, etc"; exit 1;;  # exit the entire \
          # script of split_q_jobs.sh
        * ) echo "Please answer yes or no.";;
    esac
done

# prepare input file for ph.x
prefix_name='BeBaH4'
cwd=$(pwd)
TEMP=$cwd'/tmp'
echo $TEMP
 for q in `seq 1 2 ` ; do
 #for q in 3 6 9 13 ; do
 cat > input.$q << EOF
 LOO
  &inputph
   verbosity = 'high'
   tr2_ph=1.0d-16,
   prefix = $prefix_name,
   fildvscf='loodv',
   alpha_mix(1) = 0.3,
   outdir = './tmp/$q'
   fildyn=$prefix_name'.dyn',
 !  trans=.true.,
   ldisp=.true.
   nq1=4, nq2=4, nq3=3
   start_q=$q
   last_q=$q
   electron_phonon='interpolated',
   el_ph_sigma=0.005,
   el_ph_nsigma=10,
 /
EOF
#note that the spacing before EOF must be removed, otherwise EOF cannot be recognized by shell

cat > job-split-$q.sh << EOF
#!/bin/sh
#SBATCH --verbose
#SBATCH --job-name=50G
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.err
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=180GB

module purge
module load intel/19.1.2
module load openmpi/intel/4.1.1
#module load intel/17.0.1 # this removed, instead use 19.1.2
#module load openmpi/intel/20190119 # this seems removed, instead 4.1.1 is used.

# srun /home/yf1159/VASP/vasp.5.4.4/bin/vasp_std
#srun /home/yf1159/VASP/vasp.5.4.4/bin-relax-Z/vasp_std
QE=/home/yf1159/qe-7.0-bin
PWEXE=\$QE/pw.x
PHEXE=\$QE/ph.x
DOSEXE=\$QE/dos.x
PDOSEXE=\$QE/projwfc.x

#srun \$PWEXE < nscf.in > nscf.out
srun \$PHEXE  < input.$q > $q.output
touch done

EOF

mkdir $TEMP/$q
cp -r $TEMP/$prefix_name* $TEMP/$q
sbatch job-split-$q.sh
done