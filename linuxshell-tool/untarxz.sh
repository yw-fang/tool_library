echo "Note that if file extension is tar.gz, you may need change it to tar.xz"
echo "Input file is "$1
tarfile=$1
#echo "${x%.*}" # becomes file.tar
echo "The file name is "
echo "${tarfile%.*.*}" # becomes file
filename="${tarfile%.*.*}"
unxz -k $filename".tar.xz"
tar -xvf $filename".tar"
rm -rf $filename".tar"
