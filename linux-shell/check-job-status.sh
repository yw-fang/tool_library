#author: Y.-W.FANG
#contact: fyuewen@gmail.com
#!/bin/bash

for(( i=1; i<=100; i++ ));
do

  the_world_is_flat=`tail -1 $i/OUTCAR | awk '{print ($1)}'`
#the_world_is_flat=Voluntary
if [ "$the_world_is_flat" != Voluntary ]; then
#	    echo $i
#	    echo 'Be careful this calculation is not finished!'
	    cp job-comet-continue.pbs  $i/
	    cd $i
	    qsub job-comet-continue.pbs
	    cd ../
fi
 
done
	  
  
