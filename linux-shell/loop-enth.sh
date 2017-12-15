#!/bin/bash

##for((i=20;i<=120;i=i+20));
#for((i=200;i<=800;i=i+100));
for i in  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
do
#          echo -n $i'     ' >> ./toten.dat; greptoten-fang.sh $i/OUTCAR | gawk '{print $5}' >> ./toten.dat
 echo -n $i'     ' >> ./en.dat; grep enth $i/OUTCAR |  gawk '{print $5}' >> ./en.dat
done
