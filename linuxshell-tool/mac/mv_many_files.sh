#In mac, when I wanted to use 'mv' several thouand files with extension of tar.lzma
#to other folder, I got an error of 'mv argument list too long' error.
#hence, I created this script to move them.
#author: Yue-Wen FANG
find . -name 'mp-*.tar.lzma' -exec mv {} phonon-database \;
