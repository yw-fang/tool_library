env GZIP=-9 tar -zcvf $1.tar.gz $1
# file $1.tar.gz
echo "in some cases when extracting file, 'tar -xvf' does not work because of the lacking in xz Utils, in that case"
echo "irst mv file.tar.gz to file.tar.xz, then use untarxz.sh to extract"

####XZ Utils installation method #### Note the latest version can be obtained here: https://tukaani.org/xz/
# wget https://tukaani.org/xz/xz-5.2.4.tar.gz
# tar xvfz xz-5.2.4.tar.gz
# cd xz-5.2.4
# ./configure --prefix=/usr/local/xz/5_2_4
# make
# make install
