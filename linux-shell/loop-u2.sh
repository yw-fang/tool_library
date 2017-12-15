#!/bin/bash

for((i=0;i<=120;i=i+20));
#for((i=200;i<=800;i=i+100));
#for((i=1000;i<=4000;i=i+200));
#for i in 0
do
  mkdir $i/u2
  cat INCAR-u2.ini > $i/u2/INCAR
  echo 'PSTRESS   = '$i >> $i/u2/INCAR
  cp KPOINTS job*pbs $i/u2/
  cp $i/CONTCAR $i/u2/POSCAR
  cd $i/u2
  ln -s ../POTCAR .
  qsub job*pbs
  cd ../../
done

#for((i=0;i<=120;i=i+20));
for((i=200;i<=800;i=i+100));
#for((i=1000;i<=4000;i=i+200));
#for i in 0
do
  mkdir $i/u2
  cat INCAR-u2.ini > $i/u2/INCAR
  echo 'PSTRESS   = '$i >> $i/u2/INCAR
  cp KPOINTS job*pbs $i/u2/
  cp $i/CONTCAR $i/u2/POSCAR
  cd $i/u2
  ln -s ../POTCAR .
  qsub job*pbs
  cd ../../
done
