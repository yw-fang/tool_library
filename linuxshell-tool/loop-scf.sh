#!/bin/bash

for((i=500;i<=800;i=i+100));
do
	  mkdir $i/scf
	    cat INCAR-scf > $i/scf/INCAR
	      echo 'PSTRESS   = '$i >> $i/scf/INCAR
	        cp KPOINTS job*sh $i/scf/
		  cp $i/CONTCAR $i/scf/POSCAR
		    cd $i/scf
		      ln -s ../POTCAR .
		        qsub job*sh
			  cd ../../
		  done



#for((i=0;i<=120;i=i+20));
#do
#	  mkdir $i/scf
#	    cat INCAR-scf > $i/scf/INCAR
#	      echo 'PSTRESS   = '$i >> $i/scf/INCAR
#	        cp KPOINTS job*sh $i/scf/
#		  cp $i/CONTCAR $i/scf/POSCAR
#		    cd $i/scf
#		      ln -s ../POTCAR .
#		        qsub job*sh
#			  cd ../../
#		  done
