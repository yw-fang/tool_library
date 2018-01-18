#author: Y.-W. FANG
#tar files with excluding some patters
#here I tar a directory to a compressed file with exlcuing the files with nameof wav*, WAVEVAR...
env GZIP=-9 tar -caf $1.tar.lamz $1 --exclude=wav* --exclude=WACECAR --exclude=tot-DOS* --exclude=*.o* .

