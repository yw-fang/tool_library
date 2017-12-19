
## declare an array variable
declare -a arr=("allin" "co-all-in" "co-two-in" "I" "phi2")

## now loop through the above array
for i in "${arr[@]}"
do
   echo "$i"
    
   mkdir $i/u2
   cp POSCAR $i/u2
   cp ../c3/$i/u2/KPOINTS $i/u2/
   cp ../c3/$i/u2/job-v53.pbs $i/u2/
   cp ../c3/$i/u2/INCAR $i/u2
   cd $i/u2/
   ln -s ../POTCAR .
   qsub job-v53.pbs
   cd ../../
   

   # or do whatever with individual element of the array
done

# You can access them using echo "${arr[0]}", "${arr[1]}" also
