#!/bin/bash

for((i=119813; i<=119825; i=i+1));
do
  qdel $i
done


#for((i=0;i<=360;i=i+15));
#do
#  cd $i
#  qsub job.sh
#  cd ../
#done
