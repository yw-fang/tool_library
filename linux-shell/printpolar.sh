for((i=0;i<=120;i=i+20));
do
echo $i >> ZnSnO3-polarization.dat
getpolar-new-fyw $i/OUTCAR-Berry-3-1.00 >> ZnSnO3-polarization.dat
getpolar-new-fyw $i/OUTCAR-Berry-3-.98 >> ZnSnO3-polarization.dat
done


for((i=200;i<=800;i=i+100));
do
echo $i >> ZnSnO3-polarization.dat
getpolar-new-fyw $i/OUTCAR-Berry-3-1.00 >> ZnSnO3-polarization.dat
getpolar-new-fyw $i/OUTCAR-Berry-3-.98 >> ZnSnO3-polarization.dat
done
