for i in $(seq 0 10 90)
do
  cp INCAR KPOINTS POSCAR job*pbs ./degree-energy/$i/ 
done
