#author: Yuewen Fang
#date: 2022 Feb 19
#Purpose of this file: append new files to an exsiting tar.gz file
echo "usage: append_tar name_of_tar.gz_file new_file1 new_file2 new_file3 .... "
gzip -d $1
echo $1
tar_file=`echo $1 | sed 's/.gz//g'`
echo $tar_file
#tar uvf $tar_file tarxz.sh
i=2
for arg do #using this loop, you can pass as many as arguments to this script
	if [ $arg != $1 ];then  # exclude the original tar.gz file 
		tar uvf $tar_file $arg #add file to the tar file
		printf "$arg was appended to $1 \n"
#	      printf '%s\n' "Arg $i: $arg"
        fi
  i=$((i + 1))
done
gzip -9 $tar_file  #compress the tar file to the tar.gz file using gzip -9
echo "Compressed done"

# uncompress the tar.gz : gzip -d backup.tar.gz
# add/update a file on the tar file : tar uvf backup.tar db_bkp_today.sql
# compress the tar (with maximum compression if you want) : gzip -9 backup.tar
