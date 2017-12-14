#!/bin/bash

for((i=0;i<=120;i=i+20));
do
#  echo 'for pressure of '$i'kbar' >> ./enthalpy.dat
  echo $i >> ./toten.dat
  greptoten-fang.sh $i/scf/OUTCAR  >> ./toten.dat
done


for((i=200;i<=800;i=i+100));
do
  #echo 'for pressure of '$i'kbar' >> ./enthalpy.dat
  echo $i >> ./toten.dat
  greptoten-fang.sh $i/scf/OUTCAR  >> ./toten.dat
done

#for((i=1000;i<=4000;i=i+200));
#do
#  #echo 'for pressure of '$i'kbar' >> ./enthalpy.dat
#  echo $i >> ./enthalpy.dat
#  greptoten-fang.sh $i/scf/OUTCAR  >> ./energy.dat
#done
#
