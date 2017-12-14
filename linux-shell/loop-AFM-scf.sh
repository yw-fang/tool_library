#!/bin/bash

for((i=500;i<=800;i=i+100));
do
	  mkdir $i/AFM-scf
	    cat INCAR-AFM-scf > $i/AFM-scf/INCAR
	      echo 'PSTRESS   = '$i >> $i/AFM-scf/INCAR
	        cp KPOINTS job*sh $i/AFM-scf/
		  cp $i/CONTCAR $i/AFM-scf/POSCAR
		    cd $i/AFM-scf
		      ln -s ../POTCAR .
		        qsub job*sh
			  cd ../../
		  done



#for((i=0;i<=120;i=i+20));
#do
#	  mkdir $i/AFM-scf
#	    cat INCAR-AFM-scf > $i/AFM-scf/INCAR
#	      echo 'PSTRESS   = '$i >> $i/AFM-scf/INCAR
#	        cp KPOINTS job*sh $i/AFM-scf/
#		  cp $i/CONTCAR $i/AFM-scf/POSCAR
#		    cd $i/AFM-scf
#		      ln -s ../POTCAR .
#		        qsub job*sh
#			  cd ../../
#		  done
