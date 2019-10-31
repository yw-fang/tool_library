#!/usr/bin/env python
import numpy as np
import pandas as pd

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "Oct 31, 2019"

"""
This script can reads the magnetization from mcif file and convert it into MAGMOM 
"""

# The file has no headers naming the columns, so we pass header=None and provide the column names
data = pd.read_table('./Pb2CaOsO6_2K_difference_magnetic1-backup.mcif')
# data.index.values

i = 1
match_str = '_atom_site_moment.crystalaxis_z'
while data.loc[i].values[0] != match_str:
    #   print(i)
    i += 1
print(i)

# How many atoms with magnetic moments, revise it when you use this script
mag_num = 16

j = 1
for j in range(1, mag_num + 1):
    # Read the magmetization from the file
    line = i + j
    line_info = data.loc[line]
    atom_mag_str = line_info.values[0]
    mag_list = atom_mag_str[6:].split()
    mag_str_array = np.array(mag_list)
    mag_float_array = mag_str_array.astype(np.float)
    # print(mag_float_array)

    # prepare the MAGMOM, VASP suggestes 1.2-1.5 times of the exp mag moment
    times = 2  # here I use 2 times
    magmom_array = mag_float_array * 2
    # print(magmom_array)
    print(' '.join(map(str, np.round(magmom_array, 6))), end=" ")
