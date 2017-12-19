#!/bin/bash
#YWFANG
#2017-ECNU

for i in 0
do
	  echo $i'     0' >> ./AFM-PV.dat
  done

  for((i=20;i<=120;i=i+20));
  do
	    echo -n $i'     ' >> ./AFM-PV.dat; grep 'enthalpy' $i/AFM-scf/OUTCAR | gawk '{print $9}' >> ./AFM-PV.dat
    done


    for((i=200;i<=800;i=i+100));
    do
	      echo -n $i'     ' >> ./AFM-PV.dat; grep 'enthalpy' $i/AFM-scf/OUTCAR | gawk '{print $9}' >> ./AFM-PV.dat
      done
