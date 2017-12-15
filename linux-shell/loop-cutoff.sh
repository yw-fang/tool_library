for i in 70 80 90 100 110 120 130 140 150
do
  mkdir $i
  sed -n '1,94p' BMO.dat > $i/BMO.dat
  echo 'scf.energycutoff           '$i'       # default=150 (Ry)'  >> $i/BMO.dat
  sed -n '96,179p' BMO.dat >> $i/BMO.dat 
  cp job*pbs $i/
  cd $i
  qsub job*pbs
  cd ../
done
