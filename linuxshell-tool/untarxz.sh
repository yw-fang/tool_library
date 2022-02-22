echo "Note that if file extension is tar.gz, you may need change it to tar.xz"
echo "In some cases, if it doesn't work, use gunzip first, then change the extracted tar to tar.xz, then use unxz file.tar.xz to get file.tar, finally use tar -xvf file.tar"
echo "Input file is "$1
tarfile=$1
#echo "${x%.*}" # becomes file.tar
echo "The file name is "
echo "${tarfile%.*.*}" # becomes file
filename="${tarfile%.*.*}"
unxz -k $filename".tar.xz"
tar -xvf $filename".tar"
rm -rf $filename".tar"
