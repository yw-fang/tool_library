# import pymatgen as mg
import os
# import re
import numpy as np

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "July 4, 2018"

"""
Present implementation:
VECTR can be extracted from magnetization part in OUTCAR.
VECTR should be manually added to the vesta file to visulize
the spin configuration.
For time being, I only consider the collinear magnetism

The final goal:
This script aims to read the structure from POSCAR or CONTCAR,
and reads the magnetic moment for each ion from the OUTCAR
and output the file with file extension of 'vesta' directly.
"""

path = "./"

# Read every file with extension of '.yaml' in directory
filelist = []
for filename in os.listdir(path):
    boolean_value = filename == 'OUTCAR'
    if not boolean_value:
        print('OUTCAR not found')
    else:
        print('OUTCAR is found now')
# print(filelist)


# #################define functions##################

# for file in filelist:
#     file_yaml = file + '.yaml'
#     data = h5py.File(file_yaml)
#     print(file_yaml)
