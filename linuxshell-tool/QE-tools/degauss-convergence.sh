#!/bin/bash

# replace the line including "degauss" in scf.in with "degauss=0.01" using sed, and copy to scf.in.1
# for loop from 0.005 to 0.1 with step 0.005

export LC_NUMERIC="en_US.UTF-8" # in order to properly show decimals using dot as decimal separator
for i in $(seq 0.005 0.005 0.1);
do
  mkdir $i
    sed -e "s/degauss.*/degauss=$i/" scf.in > scf.in.tmp
    # run pw.x with scf.in.1
    mv scf.in.tmp $i/scf.in
    cat job.sh > $i/job.sh; echo "mpirun -np 20 \$PWEXE  -npool 4 < scf.in > scf.out" >> $i/job.sh
    # print $i and energy from scf.out to converence.dat
    echo "grep ! scf.out | tail -1 | awk '{print $i, \$5}' >> ../convergence.dat" >> $i/job.sh
    echo "touch done" >> $i/job.sh
    cd $i/
    sbatch job.sh
    cd ../
done