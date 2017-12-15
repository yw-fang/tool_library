
## declare an array variable
declare -a arr=("allin" "co-all-in" "co-two-in" "I" "phi2")

## now loop through the above array
for i in "${arr[@]}"
do
   echo "$i"
    
   cp POSCAR $i
   cp ../c3/$i/KPOINTS $i
   cp ../c3/$i/job-v53.pbs $i
   cp ../c3/$i/INCAR $i
   cd $i
   ln -s ../POTCAR .
   qsub job-v53.pbs
   cd ..
   

   # or do whatever with individual element of the array
done

# You can access them using echo "${arr[0]}", "${arr[1]}" also
