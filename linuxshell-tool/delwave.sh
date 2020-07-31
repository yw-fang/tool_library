#!/bin/bash
for i in `find -name "WAVECAR" `
do
rm $i
done
for i in `find -name "CHG*" `
do
rm $i
done
for i in `find -name "PROCAR" `
do
rm $i
done
for i in `find -name "OUTCAR" `
do
gzip $i
done
for i in `find -name "vasp*xml" `
do
gzip $i
done
for i in `find -name "DOSCAR" `
do
rm $i
done
