#Author: Yue-Wen FANG
#Purpose: Change LEXCH from PE to PS. i.e., PBE to PBEsol.  Work for Mac
#If you want to use this script for linux, please refer to pbe2pbesol-linux.sh
sed  -i '' 's/LEXCH  = PE/LEXCH  = PS/g' $1 
echo 'LEXCH in POTCAR chaged to PS, i.e., PBEsol'
grep LEXCH $1
