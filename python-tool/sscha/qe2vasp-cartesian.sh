#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
# [Usage] qe2vasp-cartesian.sh
# [Purpose] Convert QE to VASP format with cartesian coordinates
#          History
#  HISTORY
#     2022/08/09 : Script creation
# ------------------------------------------------------------------
echo "usege: qe2vasp-cartesian.sh <QE_folder> <VASP_folder>"
ase convert -i espresso-in -o vasp  pw.in POSCAR