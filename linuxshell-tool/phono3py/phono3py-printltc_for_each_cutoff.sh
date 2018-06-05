## This script prints the LTC at 300 K.
## Author: Y.-W.FANG at Kyoto University
number_of_cutoff=$(ls -l structure_list* | wc -l)
echo $numer_of_cutoff
#locate the line with keyword 'tetrahedron'
line=$(gawk '/with\ tetrahedron\ method/{print NR}' 1/_scheduler-stdout.txt)  
echo $line
roomline=$(expr $line+32 | bc)  #locate the line with LTC at 300 K
echo $roomline
rm -rf tmp1.dat
rm -rf  cutoff-ltc.csv
for ((i=1; i<=$number_of_cutoff; i++))
do
sed -n "$roomline p" $i/_scheduler-stdout.txt | gawk '{print $2" "$3" "$4}' >> tmp1.dat
done
#grep 300.0 {1..39}/_scheduler-stdout.txt | gawk '{print $3" "$4" "$5}' > tmp1.dat
paste -d '  ' list/tmp.dat tmp1.dat > cutoff-ltc.csv
