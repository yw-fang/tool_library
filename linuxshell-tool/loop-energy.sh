#!/bin/bash

#for((i=0;i<=120;i=i+20));
for((i=0;i<=7;i=i+1));
do
  echo 'for Hubbard U = '$i
  greptoten-fang.sh $i/OUTCAR
done
