for i in $(seq 0 10 90)
do
  cd $i; ln -s ../POTCAR .; cd ../
done
