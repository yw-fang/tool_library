#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
# [Usage] vasp2qe-cartesian.sh
# [Purpose] Convert POSCAR to QE format with cartesian coordinates
#          History
#  HISTORY
#     2022/08/09 : Script creation
# ------------------------------------------------------------------
ase convert -i vasp -o espresso-in POSCAR pw.in