#!/bin/bash
#YWFANG
#2017-ECNU

for i in 0
do
	  echo $i'     0' >> ./PV.dat
  done

  for((i=20;i<=120;i=i+20));
  do
	    echo -n $i'     ' >> ./PV.dat; grep 'enthalpy' $i/scf/OUTCAR | gawk '{print $9}' >> ./PV.dat
    done


    for((i=200;i<=800;i=i+100));
    do
	      echo -n $i'     ' >> ./PV.dat; grep 'enthalpy' $i/scf/OUTCAR | gawk '{print $9}' >> ./PV.dat
      done
