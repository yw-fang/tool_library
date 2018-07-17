# This script can be used to delete directories
# which are indexed by enumarated numbers.
for(( i=1; i<=50; i++ ));
	# alternatively, we can also use
	# for i in $(seq 0 10 90)
do
  rm -rf $i/
done
