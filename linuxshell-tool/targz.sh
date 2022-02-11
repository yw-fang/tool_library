env GZIP=-9 tar -zcvf $1.tar.gz $1
file $1.tar.gz
echo "if the file format is tar.xz, first mv file.tar.gz to file.tar.xz, then use untarxz.sh to extract"
