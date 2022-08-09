#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
# [Usage] collect-pwout.sh
# [Purpose] collect the scf_*.out files after running QE force calculations for supercells from SSCHA code
#          History
#  HISTORY
#     2022/08/09 : Script creation
# ------------------------------------------------------------------
mkdir pwout
pattern="scf_"
for _dir in *"${pattern}"*; do
    [ -d "${_dir}" ] && dir="${_dir}" && echo "${dir}"
    cp "${dir}"/scf_*.out pwout/
done
tar -zcvf pwout.tar.gz pwout
rm -rf pwout