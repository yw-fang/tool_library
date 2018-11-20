# from pymatgen.io.vasp import Poscar
# import pandas as pd
from pymatgen.io.vasp.outputs import Outcar
import os
import re
"""
Purpose: This script prints the magnetization for user's quick preview.
Read: POSCAR and OUTCAR
Pattern-1: position of ions in fractional coordinates (direct lattice)

Supported vasp 5.xx, vasp 4.xx is not tested.
Both SOC and non-SOC are implemented.
"""
__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__revision_date__ = "Nov. 20th, 2018"

# yourfile = input('Choose a file: ')
# p = Poscar.from_file(yourfile)

workingpath = './'
workingfiles = ['OUTCAR', 'POSCAR']

def file_existence(filelist, filepath):
    for f in filelist:
        if f in os.listdir(filepath):
            return(True)
            pass
        else:
            print(f, 'not found')
            break


def match_soc(fname):
    pattern = r"\sLSORBIT\s=\s+T"  # SOC or not
    with open(fname, 'r') as f:
        contents = f.read()
        soc_flag_list = re.findall(pattern, contents)
        soc_flag_str = ''.join(map(str, soc_flag_list))
        if soc_flag_str:
            return(soc_flag_str[-1])
        else:
            return('F')


if file_existence(workingfiles, workingpath):
    outcar = Outcar("OUTCAR")
#    atomic_forces = outcar.read_table_pattern(
#                header_pattern=r"\sPOSITION\s+TOTAL-FORCE \(eV/Angst\)\n\s-+",
#                row_pattern=r"\s+[+-]?\d+\.\d+\s+[+-]?\d+\.\d+\s+[+-]?\d+\.\d+\s+([+-]?\d+\.\d+)\s+([+-]?\d+\.\d+)\s+([+-]?\d+\.\d+)",
#                footer_pattern=r"\s--+",
#                postprocess=lambda x: float(x),
#                last_one_only=False
#                )
#    print(atomic_forces)
    atomic_mag = outcar.magnetization
    for i in range(0,len(atomic_mag)):
        if(match_soc("OUTCAR")=='T'):  # for SOC
            magx,magy,magz = atomic_mag[i]['tot']
            print(i+1, magx, magy, magz)
        else:  # for non-SOC
            print(i+1, magx)
