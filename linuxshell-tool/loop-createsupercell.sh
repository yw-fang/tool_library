#!/bin/bash

for((i=0;i<=120;i=i+20));
do
mkdir ../../BTO223/$i
cd $i
ln -s ../generate_supercell.py .
python generate_supercell.py
mv S223POSCAR ../../../BTO223/$i/POSCAR
rm -rf generate_supercell.py
cd ../
#  cat INCAR-scf > $i/INCAR-scf
#  echo 'PSTRESS   = '$i >> $i/INCAR-scf
#  cat INCAR-berry > $i/INCAR-berry
#  echo 'PSTRESS   = '$i >> $i/INCAR-berry
#  cp KPOINTS job*pbs $i/
#  cp ../R3c/$i/scf/POSCAR $i/POSCAR-fer
#  cp ../R-3c/$i/scf/POSCAR $i/POSCAR.ini
#  cd $i
#  ln -s ../POTCAR .
##  qsub job*pbs
done
