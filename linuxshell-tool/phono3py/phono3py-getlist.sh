#!/bin/bash
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
  phono3py --cutoff-pair=$cutoff -d --dim="2 2 2" -c POSCAR-unitcell >> out.log
      for j in `ls POSCAR-0*|sed s/POSCAR-//`;do echo 'disp-'$j'/vasprun.xml' >> structure_list$i.dat;done

  done
