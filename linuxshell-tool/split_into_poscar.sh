# Author: Yuewen Fang. 
# Date: Feb. 25 2022
split -d -l 35 --numeric-suffixes=1 pso_ini_13 POSCAR_ #pso_ini_13 is the output file in calypso storing a number of POSCARs. This script can split it into many POSCARs. --numeric-suffixes=1 means the new files will begin from POSCAR_01, if this tag removed, then it will begin from POSCAR_00

