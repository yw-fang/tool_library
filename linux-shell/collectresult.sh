for(( i=1; i<=50; i++ ));
do
  mv $i/CONTCAR ./CONTCAR_$i
  mv $i/OUTCAR ./OUTCAR_$i
done
