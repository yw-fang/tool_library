#!/bin/bash

for((i=0;i<=120;i=i+20));
do
  mkdir $i/AFM-SOC-scf/
  cat INCAR-AFM-SOC-scf > $i/AFM-SOC-scf/INCAR
  echo 'PSTRESS   = '$i >> $i/AFM-SOC-scf/INCAR
  cp KPOINTS job*pbs $i/AFM-SOC-scf/
  cp $i/scf/POSCAR $i/AFM-SOC-scf/
  cd $i/AFM-SOC-scf/
  ln -s ../POTCAR .
  qsub job*pbs
  cd ../../
done

for((i=200;i<=400;i=i+100));
do
  mkdir $i/AFM-SOC-scf/
  cat INCAR-AFM-SOC-scf > $i/AFM-SOC-scf/INCAR
  echo 'PSTRESS   = '$i >> $i/AFM-SOC-scf/INCAR
  cp KPOINTS job*pbs $i/AFM-SOC-scf/
  cp $i/scf/POSCAR $i/AFM-SOC-scf/
  cd $i/AFM-SOC-scf/
  ln -s ../POTCAR .
  qsub job*pbs
  cd ../../
done
