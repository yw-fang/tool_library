mkdir scf52
cp scf/INCAR scf52/ ;
cp scf/KPOINTS scf52/
cp CONTCAR scf52/POSCAR
cp job-osepv52.pbs scf52/
cd scf52
ln -s ../POTCAR .
#qsub  job-osepv52.pbs
#cd ../
