#Author: Yue-Wen FANG
#Purpose: Change PBE to PS for POTCAR used in VASP
sed -i 's/LEXCH  = PE/LEXCH  = PS/' $1
echo 'LEXCH in POTCAR chaged to PS'
head 10 $1
