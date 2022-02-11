env GZIP=-9 tar -zcvf $1.tar.gz $1
# file $1.tar.gz
echo "in some cases when extracting file, 'tar -xvf' does not work, in that case"
echo "irst mv file.tar.gz to file.tar.xz, then use untarxz.sh to extract"
