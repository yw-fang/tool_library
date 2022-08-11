#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] ./extract_enthalpy_entropy.py
# [Purpose] Extract enthalpy and entropy from the VASP calculation for CrySPY structures
#          History
#  HISTORY
#     2022/08/11 : Script creation
# ------------------------------------------------------------------

import argparse
import pickle
# analyze space group of POSCAR using pymatgen
import numpy as np
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
# use pandas to read the data/cryspy_rslt_energy_asc_after1250struct
import pandas as pd
import os

# remind the user to prepare the data/cryspy_rslt_energy_asc* file, data/pkl_data/opt_struc_data.pkl, or
# data/pkl_data/init_struc_data.pkl, and the OUTCAR/POSCAR/OSZICAR files in the corresponding folder
print("Please prepare the data/cryspy_rslt_energy_asc* file, data/pkl_data/opt_struc_data.pkl, or")
print("data/pkl_data/init_struc_data.pkl, and the OUTCAR/POSCAR/OSZICAR files in the corresponding folder")

crys_rslt_file = 'data/cryspy_rslt_energy_asc_after1250struct'
# read crys_rslt_file with pandas, columns are separated with spacing
col_names = ['id', 'Gen', 'Spg_num', 'Spg_sym', 'Spg_num_opt', 'Spg_sym_opt',  'E_eV_atom', 'Magmom', 'Opt']
df = pd.read_csv(crys_rslt_file, skiprows=[0], names=col_names, delim_whitespace=True, usecols=[0,1,4,5,6])

# select the first 100 structures with lowest energy
df_100 = df.sort_values(by=['E_eV_atom'])[:2]
#size od df_100
#print(df_100.shape)
df_100['Entropy_eV_cell'] = np.nan
#print(df_100.head(10))

# extract the structure from data/pkl_data/opt_struc_data.pkl according to the id in df_100
with open('data/pkl_data/opt_struc_data.pkl', 'rb') as f:
    struc_data = pickle.load(f)
    # loop through the id in df_100
    for cid in df_100['id']:
        # print the structure with id cid
        # print(struc_data[cid])
        # print the space group of the structure with id cid
        spg_symbol = SpacegroupAnalyzer(struc_data[cid], symprec=.1).get_space_group_symbol()
        # print the space group number of the structure with id cid
        spg_number = SpacegroupAnalyzer(struc_data[cid], 0.1).get_space_group_number()
        # cd each folder str(cid)+'_'+str(spg_number)
        dir_name = str(cid)+'_'+str(spg_number)
        # print(dir_name)
        # read from CONTCAR using pymatgen
        from pymatgen.core import Structure
        opt_struct = Structure.from_file(dir_name + '/' + "CONTCAR")
        spg_symbol_opt = SpacegroupAnalyzer(opt_struct, symprec=.1).get_space_group_number()
        # how many atoms in the opt_struct
        n_atoms = opt_struct.num_sites
        # print(spg_symbol_opt)
        # read the final energy from OSZICAR if OSZICAR exists, otherwise raise error
        if os.path.isfile(dir_name + '/' + "OSZICAR"):
            with open(dir_name + '/' + "OSZICAR", 'r') as f:
                for line in f:
                    if 'E0=' in line:
                        E0 = float(line.split()[4])
                        # print(E0)
                        # preserve E0_per_atom having 8 decimal places
                        E0_per_atom = round(E0/n_atoms, 8) # enthalpy eV normalized to per atom
                        print("Warnning, implement save the enthalpy per atom into dataframe")
                        break
        else:
            # raise error that OSZICAR does not exist in the folder
            raise FileNotFoundError('OSZICAR does not exist in the folder ' + dir_name)
            # E0_per_atom = np.nan
        # grep the EENTRO from OUTCAR and save the value to the floating variable entropy using shell
        entropy = os.popen('grep "EENTRO" ' + dir_name + '/' + "OUTCAR").read().split()[-1]
        entropy = float(entropy)  # eV per cell; convert into floating
        print(float(entropy))
        # alternatively, we can use in shell
        # entropy = os.system('grep "EENTRO" '+dir_name+'/'+'OUTCAR'+' | tail -1 | awk \'{print $5}\'')
        # however, here, python's round will make the very small entropy into 0.00000000, so donot use it here.
        df_100.loc[df_100['id'] == cid, 'Entropy_eV_cell'] = round(entropy, 8)
print(df_100.head(2))

# save the df_100 to df_100.csv in which Entropy_eV_cell column has 8 decimal places, columns are separted with spacing
df_100.to_csv('df_100.csv', index=False, float_format='%.8f', sep = ' ')