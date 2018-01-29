#!/bin/bash
#Author: Y.-W.FANG
#Date:Jan 2018
#Puporse: tar the files and copy it from pylon5 to pylon2 on Briges
#fyuewen@gmail.com
echo 'usage: tarpylon5-2.sh filename ID'
echo 'example: tarpylon5-2.sh 1.txt ywfang'
echo 'the command compresses 1.txt and moves it to /pylon5/mr4s82p/ID'
tar -zcvf $1.tar.gz $1 > $1.log;
cp $1.tar.gz /pylon2/mr4s82p/$2 >> $1.log
