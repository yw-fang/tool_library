#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] tar every folder in the current folder
#          History
#  HISTORY
#     2022/09/26 : Script creation
# ------------------------------------------------------------------
# compress each folder in current directory using tar
#
  for i in `ls -d */`
  do
    j=${i::-1} # remove the last character '/'
echo $j
    tar -zcvf $j.tar.gz $j
  done
