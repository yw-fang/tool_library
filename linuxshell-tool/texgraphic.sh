#!/bin/bash
# -*- coding: utf-8 -*-
#
# the original name texsize was written by François-Xavier Coudert at 2014-05-12
# revised a little bit by Yuewen FANG
#
# purpose:  list graphics file included in latex doc, and their size
#

if [ $# -ne 1 ] ; then
  echo "Usage: file-name-without-file-extension"
  exit 1
fi

if ! ( [ -e "$1.log" ] && [ -e "$1.pdf" ] ) ; then
  echo "Error: '$1.log' and '$1.pdf' should exist"
  exit 1
fi

function filesize {
  # This is ugly, and portable
  wc -c < $1
  # GNU stat variant
  #stat -Lf '%z'
  # BSD stat variant
  #stat -Lc '%s'
}

function humansize {
  awk "BEGIN{sum=$1;
	hum[1024**3]=\"GB\";hum[1024**2]=\"MB\";hum[1024]=\"kB\"; 
	for (x=1024**3; x>=1024; x/=1024){ 
		  if (sum>=x) { printf \"%5.1f %s\",sum/x,hum[x];break }
		}}"
}

# Find list of included files
LC_ALL=C
inc=`tr '\n' '#' < $1.log \
       | sed -e 's/#//g' -e 's/</#</g' | tr '#' '\n' \
       | grep '<' | sed -e 's/>.*//' -e 's/<//' \
       | egrep -v '(pfb|cmap)$' | egrep -v '^use ' \
       | sed -e 's/,.*//' | grep -v ' ' | sed -e 's@^\./@@' \
       | sort | uniq `

# Only those that exist (same false positives otherwise)
files=""
for i in $inc ; do
  if [ -e "$i" ]; then
    files="$files $i"
  fi
done

# Check that we have at least one file
if [ "x$files" = "x" ]; then
  echo "No figure included in this document"
  exit 1
fi

sorted=`ls -lLrS $files | sed 's/.* //'`
pdfsize=`filesize $1.pdf`

sum="0"
echo "List of included figures sorted by ascending size:"
for i in $sorted ; do
  s=`filesize $i`
  sum=`echo "$sum + $s" | bc -l`

  printf "% 40s : " $i
  humansize $s
  printf " (%.1f%%)\n" `echo "100.0 * $s / $pdfsize" | bc -l`
done

echo "-------------------------------------------------------------"
echo    "       Total PDF size: $pdfsize /" `humansize $pdfsize`
echo -n "  Total graphics size:" `humansize $sum`
printf " (%.1f%%)\n" `echo "100.0 * $sum / $pdfsize" | bc -l`

exit 0

