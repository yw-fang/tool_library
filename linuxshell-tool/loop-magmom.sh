#!/bin/bash

#for((i=345;i>=0;i=i-15));
for((i=0;i<=345;i=i+15));
do
  mkdir alpha-$i
  cp KPOINTS POSCAR job*pbs alpha-$i/
  sed -n '1,9p' ./INCAR  > alpha-$i/INCAR
  j=$(($i/15+1))
  sed -n "$j p" ./magmom-fixtheta90.dat >> alpha-$i/INCAR
  sed -n '11,66p' ./INCAR >> alpha-$i/INCAR
  cd alpha-$i
  ln -s ../POTCAR .
  qsub job*pbs
  cd ../
done