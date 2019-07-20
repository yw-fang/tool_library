#!/bin/bash
#author: Y.-W. Fang contact: fyuewen@gmail.como
#This shell script accepts two input parameters, the first one ($1) is Fermi level;
#the second one ($2) is the operation system.
EF=$1
OS=$2

tar -zcvf vasprun.tar.gz vasprun.xml # make a compressed backup

if [ $OS == 'mac' ]
then 
	echo $OS
	sed -i '' 's/.*efermi.*/\ \ \ \<i\ name=\"efermi\"\>\ \ \ \ \ \ '$EF' \<\/i\>/' vasprun.xml
else
	sed -i 's/.*efermi.*/\ \ \ \<i\ name=\"efermi\"\>\ \ \ \ \ \ '$EF' \<\/i\>/' vasprun.xml
fi


# sed -i '' 's/.*efermi.*/\ \ \ \<i\ name=\"efermi\"\>\ \ \ \ \ \ 3.672 \<\/i\>/' vasprun.xml

####for mac#####
#sed -i '' 's/.*efermi.*/\ \ \ \<i\ name=\"efermi\"\>\ \ \ \ \ \ '$EF' \<\/i\>/' vasprun.xml

####for linux#####
#sed -i 's/.*efermi.*/\ \ \ \<i\ name=\"efermi\"\>\ \ \ \ \ \ '$EF' \<\/i\>/' vasprun.xml
