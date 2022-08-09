#!/bin/bash
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
# [Usage] run-QE-force-for-SSCHA.sh
# [Purpose] Run QE force calculations for supercells from SSCHA code
#          History
#  HISTORY
#     2022/08/09 : Script creation
# ------------------------------------------------------------------
for x in ./*.in; do
  mkdir "${x%.*}" && cp "$x" "${x%.*}"
  cp job.sh job_tmp.sh
  echo "mpirun -np 20 \$PWEXE -npool 4 < ${x%.*}.in > ${x%.*}.out" >> job_tmp.sh
  echo "touch done" >> job_tmp.sh
  mv job_tmp.sh "${x%.*}/job.sh"
  cd "${x%.*}"
  sbatch job.sh
  cd ../
done