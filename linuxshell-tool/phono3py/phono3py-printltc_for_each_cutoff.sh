number_of_cutoff=$(ls -l structure_list* | wc -l)
echo $numer_of_cutoff
rm -rf tmp1.dat
for ((i=1; i<=$number_of_cutoff; i++))
do
line=$(gawk '/with\ tetrahedron\ method/{print NR}' $i/_scheduler-stdout.txt)  #locate the line with keyword 'xx'
echo $line
roomline=$(expr $line+32 | bc)  #locate the line with LTC at 300 K
echo $roomline
sed -n "$roomline p" $i/_scheduler-stdout.txt | gawk '{print $2" "$3" "$4}' >> tmp1.dat
done
#grep 300.0 {1..39}/_scheduler-stdout.txt | gawk '{print $3" "$4" "$5}' > tmp1.dat
paste -d '  ' list/tmp.dat tmp1.dat > cutoff-ltc.csv

