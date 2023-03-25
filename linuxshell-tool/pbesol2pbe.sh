# created by yuewen fang at Jan 26, 2023
# The purpose is used for changing all the claculations from PBEsol to
# PBE.
 find . -name "POTCAR" -exec sed -i 's/LEXCH  = PS/LEXCH  = PE/' {} \;
 find . -name "INCAR" -exec sed -i '/GGA/ s/^/#/' {} +
