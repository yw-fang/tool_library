#author: Y.-W.Fang fyuewen@gmail.com
#Date: 2020 June 30
#This shell script accepts one input parameter and it will update the Fermi energy of OUTCAR
EF=$1
sed  -i 's/E-fermi\ \:\(.*\)XC/\ E-fermi\ \:\ '$1'\ \ \ XC/' OUTCAR
