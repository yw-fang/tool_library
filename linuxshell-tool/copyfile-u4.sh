
## declare an array variable
declare -a arr=("allin" "co-all-in" "co-two-in" "I" "phi2")

## now loop through the above array
for i in "${arr[@]}"
do
   echo "$i"
    
   mkdir $i/u4
   cp POSCAR $i/u4
   cp ../c3/$i/u4/KPOINTS $i/u4/
   cp ../c3/$i/u4/job-v53.pbs $i/u4/
   cp ../c3/$i/u4/INCAR $i/u4
   cd $i/u4/
   ln -s ../POTCAR .
   qsub job-v53.pbs
   cd ../../
   

   # or do whatever with individual element of the array
done

# You can access them using echo "${arr[0]}", "${arr[1]}" also
