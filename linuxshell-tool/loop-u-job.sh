declare -a arr=("u1" "u2" "u3" "u4" "u5")
for i in "${arr[@]}"
do 
cd $i
rm -rf isym0
mkdir isym0
cp INCAR isym0/INCAR
cp aiida-submit.sh isym0/
cp CONTCAR isym0/POSCAR
cd isym0
ln -s ../POTCAR ./
sed -i 's/ISYM      = 2/ISYM      = 0/' INCAR
echo 'kmesh' > KPOINTS
echo '0' >> KPOINTS
echo 'G' >> KPOINTS
echo '8 8 4' >> KPOINTS
sed -i 's/#$ -l h_rt=80:00:00/#$ -l h_rt=120:00:00/' aiida-submit.sh
qsub aiida-submit.sh
cd ../../
done
