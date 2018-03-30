#!/bin/bash
#After vasp calculations, this script can list all the vasprun.xml in the current folders. 
for i in `ls POSCAR-0*|sed s/POSCAR-//`;do echo disp-$i/vasprun.xml;done > file_list.dat
	echo 'the vasprun.xml list isin file_list.dat'
	echo "plese use it through 'phono3py --cf3_file file_list.dat' "
