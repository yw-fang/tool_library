for i in $(seq -s " " -f %05g 1 1728); #1728
do
	file="POSCAR-$i"
if [ -f "$file" ]
then
	cd  disp-${i};
	if grep -q 'Voluntary' OUTCAR
	then
		    true
	    else
		        echo 'failure', $i
		fi
		cd ../
fi
done
