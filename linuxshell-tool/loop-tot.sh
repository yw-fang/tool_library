for i in 70 80 90 100 110 120 130 140 150
do
  cd $i
  greptot-omx BMO.std >> ../totenergy.dat
  cd ../
done
