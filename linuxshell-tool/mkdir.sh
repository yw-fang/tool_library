for i in $(seq 0 10 90)
do
  mkdir $i
  cp INCAR KPOINTS POSCAR job*pbs ./$i/ 
done

for i in $(seq 0 10 90)
do
  cd $i; ln -s ../POTCAR .; cd ../
done

