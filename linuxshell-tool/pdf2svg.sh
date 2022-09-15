#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] pdf2svg.sh pdf_file
# [Purpose] using inkscape to convert a pdf file into svg file
#          History
#  HISTORY
#     2022/09/15 : Script creation
# ------------------------------------------------------------------

# 1. check the param
if [ $# -lt 1 ]; then
    echo "Usage: $0 pdf_file"
    exit 1
fi

# 2. get the file name
file_name=$(basename "$1")
file_name=${file_name%.*}

# 3. convert pdf to svg
inkscape -D -z --file="$1" --export-plain-svg="$file_name.svg"

# 4. check the result
if [ $? -ne 0 ]; then
    echo "Convert $1 to $file_name.svg failed!"
    exit 1
else
    echo "Convert $1 to $file_name.svg success!"
fi