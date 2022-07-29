#Yuewen Fang; this script is used to list the folders including many files 
#reference: https://askubuntu.com/questions/316027/find-directories-with-lots-of-files-in
#!/bin/bash

if [ $# -ne 1 ];then
  echo "Usage: `basename $0` DIRECTORY"
  exit 1
fi

echo "Wait a moment if you want a good top of the bushy folders..."

find "$@" -type d -print0 2>/dev/null | while IFS= read -r -d '' file; do 
    echo -e `ls -A "$file" 2>/dev/null | wc -l` "files in:\t $file"
done | sort -nr | head -n 50 | awk '{print NR".", "\t", $0}' #list the top folders

exit 0
