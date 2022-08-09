#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
# [Usage] copy-links.sh
# [Purpose] copy files with symbolic link or folders including files with symbolic link to destination folder/file
# with hard link
#          History
#  HISTORY
#     2022/08/09 : Script creation
# ------------------------------------------------------------------
#copy follow symbolic links in SOURCE
cp -ral $1 $2