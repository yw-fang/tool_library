#!/bin/bash
for(( i=1; i<=50; i++ ));
do
if [ -e $i/OUTCAR_5 ]
then
    grep entha $i/OUTCAR_5
    #echo $i
else
    :
fi
done
