#!/bin/bash

##for((i=20;i<=120;i=i+20));
#for((i=200;i<=800;i=i+100));
for((i=0;i<=400;i=i+400));
do
  mkdir $i
  cat INCAR-scf > $i/INCAR-scf
  echo 'PSTRESS   = '$i >> $i/INCAR-scf
  cat INCAR-berry > $i/INCAR-berry
  echo 'PSTRESS   = '$i >> $i/INCAR-berry
  cp KPOINTS job*pbs $i/
  sed -n '1,19p' ../R3c/$i/scf/POSCAR >> $i/POSCAR-fer
  sed -n '1,19p'  ../R-3c/$i/scf/POSCAR > $i/POSCAR.ini
  cd $i
  getxyzdiff-fyw POSCAR-fer POSCAR.ini
  mv xyzdiff.out XYZDIFF.OUT
  ln -s ../POTCAR .
  qsub job*pbs
  cd ../
done
