#!/bin/bash

for i in 0
do echo $i >> ./enthalpy.dat
greptoten-fang.sh $i/scf/OUTCAR  >> ./enthalpy.dat
done

for((i=20;i<=120;i=i+20));
do
#  echo 'for pressure of '$i'kbar' >> ./enthalpy.dat
  echo $i >> ./enthalpy.dat
  grep 'enthalpy' $i/scf/OUTCAR  >> ./enthalpy.dat
done


for((i=200;i<=800;i=i+100));
do
  #echo 'for pressure of '$i'kbar' >> ./enthalpy.dat
  echo $i >> ./enthalpy.dat
  grep 'enthalpy' $i/scf/OUTCAR  >> ./enthalpy.dat
done
