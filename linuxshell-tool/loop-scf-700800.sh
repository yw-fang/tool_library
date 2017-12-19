
for((i=700;i<=800;i=i+100));
#for((i=200;i<=800;i=i+100));
#for((i=1000;i<=4000;i=i+200));
do
  mkdir $i/scf
  cat INCAR-scf > $i/scf/INCAR
  echo 'PSTRESS   = '$i >> $i/scf/INCAR
  cp KPOINTS job*pbs $i/scf/
  cp $i/CONTCAR $i/scf/POSCAR
  cd $i/scf
  ln -s ../POTCAR .
  qsub job*pbs
  cd ../../
done

