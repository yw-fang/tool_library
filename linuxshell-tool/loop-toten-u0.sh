
## declare an array variable
declare -a arr=("FM-AFM" "Neel-AFM" "Zigzag-AFM" "Stripy-AFM")

echo "config eV-40atom moment" >> u0-toten.dat
## now loop through the above array
for i in "${arr[@]}"
do
 echo -n $i'     ' >> ./u0-toten.dat; greptoten-fang.sh u0/$i/OUTCAR |  gawk '{printf("%9.8f\n",$5/2.0000)}' >> ./u0-toten.dat
done
