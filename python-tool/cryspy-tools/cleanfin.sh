#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] tar every folder in the current folder
#          History
#  HISTORY
#     2022/09/26 : Script creation
# ------------------------------------------------------------------
# compress each folder in current directory using tar
#

# delete files OUTCAR_* and vasprun.xml* in the subfolders begins with '0'

for i in `ls -d 0*/`
do
  j=${i::-1} # remove the last character '/'
  echo $j
  cd $j
  rm -rf OUTCAR_*
  rm -rf vasprun.xml*
  rm -rf CHG*
  rm -rf WAVECAR
  rm -rf EIGENVAL
  rm -rf PROCAR
  rm -rf DOSCAR
  rm -rf slurm* # delete slurm files
  rm -rf 2*.out # delete slurm files
  rm -rf KPOINTS*
  rm -rf IBZKPT
  rm -rf XDATCAR
  cd ..
done
