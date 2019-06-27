#Author: Yue-Wen FANG
#Purpose: Change LEXCH from PE to PS. i.e., PBE to PBEsol. Work for linux
sed -i 's/LEXCH  = PE/LEXCH  = PS/' $1  # if you want to use in Mac, refer to "pbe2pbesol-mac.sh
echo 'LEXCH in POTCAR chaged to PS, i.e., PBEsol'
grep LEXCH $1
