#!/bin/bash

#Yue-Wen Fang
#ecnu-nyu
for((i=0;i<=120;i=i+20));
do
	  echo -n $i'     ' >> ./toten.dat; greptoten-fang.sh $i/scf/OUTCAR | gawk '{print $5}' >> ./toten.dat
  done


  for((i=200;i<=800;i=i+100));
  do
	    echo -n $i'     ' >> ./toten.dat; greptoten-fang.sh $i/scf/OUTCAR | gawk '{print $5}' >> ./toten.dat
    done
