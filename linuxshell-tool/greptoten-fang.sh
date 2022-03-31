#author: Yuewen Fang created at 2017
#modification date: 2022 March 31, add function to print the energy for pwscf and add more input parameters
echo "usage: greptoten-fang.sh arg1 arg2"
echo "arguments meaning: arg1 code (vasp/pw); arg2: file"
CODE=$1
file=$2
if [ $CODE == 'vasp' ]
then
        echo $CODE
	grep 'free  energy   TOTEN' $file
#grep TOTEN $1 | tail -3
elif [ $CODE == 'pw' ]
then
	echo $CODE
	grep '!    total energy' $file
done

