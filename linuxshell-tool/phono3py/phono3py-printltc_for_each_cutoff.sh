##a=$(ls -l structure_list* | wc -l)
##echo $a
grep 300.0 {1..39}/_scheduler-stdout.txt | gawk '{print $3" "$4" "$5}' > tmp1.dat
paste -d '  ' list/tmp.dat tmp1.dat > cutoff-ltc.csv

