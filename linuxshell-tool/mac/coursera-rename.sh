 for i in $(seq -s " " -f %02g 1 8);  #1728
# for i in *;
do
	echo ${i}
#	cd ${i}
 cd ${i}_*
    for f in * ; do mv -- "$f" "C02${i}_$f" ; done
 echo 'hello'
cd ../
done
