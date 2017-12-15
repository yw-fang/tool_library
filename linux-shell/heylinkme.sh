mkdir scf
cd scf
cp ../CONTCAR ./POSCAR
ln -s ../POTCAR .
ln -s ../job-osep.pbs .
cp ../../relax-allin/scf/INCAR .
cp ../KPOINTS .
grep MAGM ../INCAR >> INCAR
