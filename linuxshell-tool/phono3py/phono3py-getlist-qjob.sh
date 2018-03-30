#!/bin/bash
#usage: before running this command, please make sure that you have these following files
#POSCAR-unitcell, aiidasubmit-phono3py.sh
rm -rf structure_list*.dat
phono3py --cutoff-pair=0.1 -d --dim="2 2 2" -c POSCAR-unitcell > out.log
phono3py-distance.sh disp_fc3.yaml > tmp.dat
rm -rf POSCAR-0*
lines=$(wc -l < tmp.dat) #note: don't cretea spacing at both sides of =
echo $lines
for((i=1;i<=$lines;i=i+1));
  do
#    sed -n "${i}p" tmp.dat
    cutoff=$(sed -n "${i}p" tmp.dat) 
    echo 'cutoff read'
    echo $cutoff
# if [ "$cutoff" = "0" ]; then
 cutoff="$cutoff+0.1"
 cutoff=`bc <<< $cutoff`
 echo $cutoff
# fi
  phono3py --cutoff-pair=$cutoff -d --dim="2 2 2" -c POSCAR-unitcell >> out.log
# cp disp_fc3.yaml disp_fc3_list$i.yaml 
  cp disp_fc3.yaml ../disp_fc3.yaml
      for j in `ls POSCAR-0*|sed s/POSCAR-//`;do echo 'disp-'$j'/vasprun.xml' >> structure_list$i.dat; done
  cp structure_list$i.dat ../structure_list$i.dat
  cp aiidasubmit-phono3py.sh .
  cd ../
  phono3py --cf3_file structure_list$i.dat
  mkdir $i
  mv FORCES_FC*  disp_fc3.yaml $i
  cd $i
  ln -s ../POSCAR-unitcell  .
  ln -s ../BORN .
  ln -s ../aiidasubmit-phono3py.sh .
  qsub  aiidasubmit-phono3py.sh
  cd ../
cd list
  done
rm -rf POSCAR-0*
