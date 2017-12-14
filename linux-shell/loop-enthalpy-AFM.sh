#!/bin/bash
for i in 0
 do
	   echo -n $i'     ' >> ./AFM-enthalpy.dat; greptoten-fang.sh $i/AFM-scf/OUTCAR | gawk '{print $5}' >> ./AFM-enthalpy.dat
   done

   for((i=20;i<=120;i=i+20));
   do
	     echo -n $i'     ' >> ./AFM-enthalpy.dat; grep 'enthalpy' $i/AFM-scf/OUTCAR | gawk '{print $5}' >> ./AFM-enthalpy.dat
     done


     for((i=200;i<=800;i=i+100));
     do
	       echo -n $i'     ' >> ./AFM-enthalpy.dat; grep 'enthalpy' $i/AFM-scf/OUTCAR | gawk '{print $5}' >> ./AFM-enthalpy.dat
       done
