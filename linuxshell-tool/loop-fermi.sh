#author: Y.-W.Fang
declare -a arr=("F-P1-Q1-L" "G-F"  "G-P-Z"  "L-Z"  "Z-Q-G")

for i in "${arr[@]}"
do
  cd $i
  tar -zcvf vasprun.tar.gz vasprun.xml; 
  ln -s ../fermi_vasprun.sh .
  ./fermi_vasprun.sh 3.6661 linux  # 3.6661 and linux can be revised by users
cd ../
done
