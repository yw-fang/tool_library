#!bin/bash
#author: Y.-W.Fang
#purpose: this script is used for collecting OUTCAR and CONTCAR
#date: Nov. 2017

for(( i=1; i<=50; i++ ));
do
  mv $i/CONTCAR ./CONTCAR_$i
  mv $i/OUTCAR ./OUTCAR_$i
done
