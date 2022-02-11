env GZIP=-9 tar -zcvf $1.tar.xz $1
file $1.tar.xz
echo "use 'tar -xvf' to extract, if it doesn't work,use untarxz.sh to extract"
