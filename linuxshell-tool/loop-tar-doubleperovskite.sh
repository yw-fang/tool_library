## declare an array variable
#declare -a arr=("allin" "twoin" "onein" "twoin-path4" "co-all-in" "co-two-in" "co-one-in" "co-twoin-path4" "I-x" "I-z" "phi2")
declare -a arr=("allin" "twoin" "onein" "twoin-path4" "co-all-in" "co-two-in" "co-one-in" "co-twoin-path4" "I-x" "I-z" "FM" "FM-noSOC" "I-x-noSOC" "I-z-noSOC" "allin-noSOC" "co-all-in-noSOC" "co-one-in-noSOC" "co-two-in-noSOC" "co-twoin-path4-noSOC" "onein-noSOC" "twoin-noSOC" "twoin-path4-noSOC")
## now loop through the above array
for i in "${arr[@]}"
do
   #echo "$i"
   cd $i
   tarlzma.sh DOSCAR; sleep 1s; rm -rf DOSCAR
   rm -rf CHG
   rm -rf CHGCAR
   rm -rf REPORT vasprun.xml EIGENVAL
   cd ../
done
