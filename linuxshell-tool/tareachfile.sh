#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] tar every file in the current folder
#          History
#  HISTORY
#     2023/03/29 : Script creation
# ------------------------------------------------------------------
# compress each file in current directory using tar
#
for file in *; do tar -czvf "${file}.tar.gz" "$file"; done
