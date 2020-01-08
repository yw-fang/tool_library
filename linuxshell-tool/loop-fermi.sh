#author: Y.-W.Fang
#creation_date: 2019 July 21th
#revised_date: 2020 Jan 8, comment out the tar command, remove soft-link 
declare -a arr=("F-P1-Q1-L" "G-F"  "G-P-Z"  "L-Z"  "Z-Q-G")

for i in "${arr[@]}"
do
  cd $i
#  tar -zcvf vasprun.tar.gz vasprun.xml; 
  cp -r ../fermi_vasprun.sh .
  ./fermi_vasprun.sh 3.6661 linux  # 3.6661 and linux can be revised by users
cd ../
done
