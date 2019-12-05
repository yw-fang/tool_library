#awk FNR-1  tot-DOS1 > tmp && mv tmp tot-DOS1
awk 'NR > 2 { print }' tot-DOS1 > tmp && mv tmp tot-DOS1
	for((i=2;i<=8;i=i+1));
	do 
		awk FNR-1  tot-DOS$i > tmp && mv tmp tot-DOS$i
	done
