#Author: Yue-Wen FANG
#Date: 2018 May 25
#If you have a lot of POSCAR files like POSCAR_1, POSCAR_2 ...
#You can use this script to rename them into POSCAR_1.vasp ...

for i in POSCAR_{1..30}
do
	mv $i $i.vasp
done
