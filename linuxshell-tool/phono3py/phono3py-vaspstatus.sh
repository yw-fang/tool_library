#!/bin/bash
for i in $(seq -s " " -f %05g 1 146);
do
cd  disp-${i};
if grep -q 'Voluntary' OUTCAR
then
    true
else
    echo 'failure, $i'
fi
cd ../
done

