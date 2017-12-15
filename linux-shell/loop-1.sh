#!/bin/bash

#for((i=20;i<=120;i=i+20));
for((i=200;i<=800;i=i+100));
#for((i=1000;i<=4000;i=i+200));
do
  mkdir $i
  cat INCAR.ini > $i/INCAR
  echo 'PSTRESS   = '$i >> $i/INCAR
  cp KPOINTS POSCAR job*pbs $i/
  cd $i
  ln -s ../POTCAR .
  qsub job*pbs
  cd ../
done

