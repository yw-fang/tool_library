# from pymatgen.io.vasp import Poscar
# import pandas as pd
import os
import re
"""
Purpose: This script prints the magnetization for user's quick preview.
Read: POSCAR and OUTCAR
Pattern-1: position of ions in fractional coordinates (direct lattice)

Supported vasp 5.xx, vasp 4.xx is not tested.
SOC and non-SOC both implemented.
"""
__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "October 17th, 2018"

# yourfile = input('Choose a file: ')
# p = Poscar.from_file(yourfile)

workingpath = './'
workingfiles = ['OUTCAR', 'POSCAR']


def file_existence(filelist, filepath):
    for f in filelist:
        if f in os.listdir(filepath):
            # print(f, 'does exist')
            pass
        else:
            print(f, 'not found')


file_existence(workingfiles, workingpath)

def match_mag(fname):
    pattern = r"\smagnetization\s"
    with open(fname, 'r') as f:
        contents = f.read()
        magnetization = re.findall(pattern, contents)
        return(magnetization)

magnetization = match_mag(workingfiles[0])
print(magnetization)
# p = Poscar.from_file('./POSCAR')
# f =
#
# structure_summary = p.structure
# natoms_list = p.natoms
# sum_natoms = sum(natoms_list[0:len(natoms_list)])
