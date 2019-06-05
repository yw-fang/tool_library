# This example shows how to print the DOS at E_F for each atom from tot-DOS* files
# Author: Y.-W. FANG, 2019 June 5th
for((i=1;i<=49;i=i+1));
do
sed -n '2341p' tot-DOS"$i" # you can change 2341 according to the line number in DOS* files
done
