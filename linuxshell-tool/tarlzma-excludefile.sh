#author: Y.-W. FANG
#tar files with excluding some patters
#here I tar a directory to a compressed file with exlcuing the files with nameof wav*, WAVEVAR...

#Method-1: this doesn't work in my ubuntu 17 and mac os
#env GZIP=-9 tar -caf $1.tar.lamz $1 --exclude=wav* --exclude=WACECAR --exclude=tot-DOS* --exclude=*.o* .
#Method-2
env GZIP=-9 tar --exclude */WAVECAR --exclude */*/WAVECAR --exclude */*/*/WAVECAR --exclude */*/*/*/WAVECAR -caf c2.tar.lzma c2

