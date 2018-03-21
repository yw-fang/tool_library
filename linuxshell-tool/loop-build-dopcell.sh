#!/bin/bash

for((i=0;i<=120;i=i+20));
do
cd $i
sed -i '6s/.*/La Ba Ti O/' POSCAR
sed -i '7s/.*/1 11 12 36/' POSCAR
cd ../
done
