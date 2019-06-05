# This example shows how to print the DOS at E_F for each atom from tot-DOS* files
# Author: Y.-W. FANG, 2019 June 5th
for((i=1;i<=49;i=i+1));
do
	#The first column is the atom index, the second column is the DOS at EF
echo -n $i'  '; sed -n '2341p' tot-DOS"$i" | gawk '{print $2}' # you can change 2341 according to the line number in DOS* files
done
