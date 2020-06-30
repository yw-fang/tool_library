
## declare array variable
declare -a arr=("FM" "Neel" "Zigzag" "Stripy")
declare -a num=('0' '1' '1.5' '2' '3' '4' '5')

## now loop through the above array
for i in "${num[@]}"
do
for j in "${arr[@]}"
do
echo $i/$j
tail -52 $j/'u'$i/OUTCAR| head -4
done
done
