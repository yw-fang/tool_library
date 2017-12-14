#!/bin/bash

#for((i=20;i<=120;i=i+20));
for((i=0;i<=120;i=i+20));
do
	echo $i
	tail -1 $i/OUTCAR
	done

for((i=200;i<=400;i=i+100));
#for i in 0
do
	echo $i
	tail -1 $i/OUTCAR
	done
