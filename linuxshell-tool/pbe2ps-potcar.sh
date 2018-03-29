#Author: Yue-Wen FANG
#Purpose: Change PBE to PS for POTCAR used in VASP
sed -i 's/LEXCH  = PE/LEXCH  = PS/' POTCAR
echo 'LEXCH in POTCAR chaged to PS'
head 10 POTCAR
