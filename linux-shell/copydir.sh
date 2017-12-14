for(( i=1; i<=50; i++ ));
do
#	mkdir $i
#	cp INCAR_*  $i
#	cp KPOINTS_* $i/
	cp POSCAR_$i $i/POSCAR
#	cp job-boston.pbs $i
	cd $i/
#	ln -s ../POTCAR .
	qsub job-comet.pbs
	cd ../
done
