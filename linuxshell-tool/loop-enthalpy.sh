#!/bin/bash
#Purpose display enthalpy from OUTCAR
#for i in  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
for i in 0
 do
	   echo -n $i'     ' >> ./enthalpy.dat; greptoten-fang.sh $i/scf/OUTCAR | gawk '{print $5}' >> ./enthalpy.dat
   done

   for((i=20;i<=120;i=i+20));
   do
	     echo -n $i'     ' >> ./enthalpy.dat; grep 'enthalpy' $i/scf/OUTCAR | gawk '{print $5}' >> ./enthalpy.dat
     done


     for((i=200;i<=800;i=i+100));
     do
	       echo -n $i'     ' >> ./enthalpy.dat; grep 'enthalpy' $i/scf/OUTCAR | gawk '{print $5}' >> ./enthalpy.dat
       done
