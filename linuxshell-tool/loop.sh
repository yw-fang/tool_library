#!/bin/bash

#for((i=0;i<=120;i=i+20));
##for i in 0
#do
#  mkdir $i
#    cat INCAR.ini > $i/INCAR
#      echo 'PSTRESS   = '$i >> $i/INCAR
#        cp KPOINTS POSCAR job*sh $i/
#	  cd $i
#	    ln -s ../POTCAR .
#	      qsub job*sh
#	        cd ../
#	done

for((i=500;i<=800;i=i+100));
#for i in 0
do
  mkdir $i
    cat INCAR.ini > $i/INCAR
      echo 'PSTRESS   = '$i >> $i/INCAR
        cp KPOINTS POSCAR job*sh $i/
	  cd $i
	    ln -s ../POTCAR .
	      qsub job*sh
	        cd ../
	done
