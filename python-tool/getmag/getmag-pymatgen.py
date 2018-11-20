# from pymatgen.io.vasp import Poscar
# import pandas as pd
import pymatgen as mg
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
__creation_date__ = "Nov. 20th, 2018"

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



