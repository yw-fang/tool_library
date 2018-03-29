#Author: Yue-Wen FANG
#Purpose: Change PS to PBE for POTCAR used in VASP
sed -i 's/LEXCH  = PS/LEXCH  = PE/' POTCAR
echo 'LEXCH in POTCAR chaged to PE'
head 10 POTCAR
