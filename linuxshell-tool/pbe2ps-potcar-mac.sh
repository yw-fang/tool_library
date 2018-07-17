#Author: Yue-Wen FANG
#Purpose: Change PBE to PS for POTCAR used in VASP
#Status: This cannot work for time being
#sed  "s/LEXCH  = PS/LEXCH  = PS/g" << $1
echo 'usage: run pbe2ps-potcar.sh directly'
echo 'make sure you have a POTCAR in current dir'
sed -i '' 's/LEXCH  = PS/LEXCH  = PS/g' POTCAR
echo 'LEXCH in POTCAR chaged to PS'
head -10 POTCAR
