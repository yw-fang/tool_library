#This shell will generate the file and folder hierarchy for you in mac OS system
#Author: Y.-W.FANG 2018 Setepmber 19th
find ./ -print | sed -e 's;[^/]*/;|--->;g;s;--->|; |;g' > ./hierarchy.txt
