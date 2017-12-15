
for q in `seq 1 1 10` ; do
echo $q >> modescale-energy.dat
cd $q; 
grep TOTEN OUTCAR >> ../modescale-energy.dat
cd ../
done

#for q in `seq 0.06 0.12 0.90` ; do
#echo $q >> modescale-energy.dat
#cd $q; 
#grep TOTEN OUTCAR >> ../modescale-energy.dat
#cd ../
#done
#
#for q in `seq  0.990 0.004 1.010` ; do
#echo $q >> modescale-energy.dat
#cd $q; 
#grep TOTEN OUTCAR >> ../modescale-energy.dat
#cd ../
#done
#
#for q in `seq 1.02 0.12 1.50` ; do
#echo $q >> modescale-energy.dat
#cd $q; 
#grep TOTEN OUTCAR >> ../modescale-energy.dat
#cd ../
#done
