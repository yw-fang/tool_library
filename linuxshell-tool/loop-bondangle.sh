#!/bin/bash 

for((i=0;i<=120;i=i+20));
do
	cp ../$i/scf/POSCAR ./POSCAR-$i.vasp
done

for((i=200;i<=400;i=i+100));
do
	cp ../$i/scf/POSCAR ./POSCAR-$i.vasp
done
