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
from pymatgen.io.vasp.outputs import Oszicar, Outcar
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
        spg_symbol_opt = SpacegroupAnalyzer(opt_struct, symprec=.1).get_space_group_symbol()
        spg_number_opt= SpacegroupAnalyzer(opt_struct, symprec=.1).get_space_group_number()
        # update the Spg_num_opt column in df_100 using spg_number_opt
        df_100.loc[df_100['id'] == cid, 'Spg_num_opt'] = spg_number_opt
        df_100.loc[df_100['id'] == cid, 'Spg_sym_opt'] = spg_symbol_opt
        # how many atoms in the opt_struct
        n_atoms = opt_struct.num_sites
        # print(spg_symbol_opt)
        # read the final energy E0 from OSZICAR if OSZICAR exists using pymatgen, otherwise raise error
        try:
            oszicar = Oszicar(dir_name + '/' + "OSZICAR")
            E0 = oszicar.final_energy
            E0_per_atom = round(E0/n_atoms, 8) # enthalpy eV normalized to per atom
            # save E0_per_atom in the column E_eV_atom of df_100
            df_100.loc[df_100['id'] == cid, 'E_eV_atom'] = round(E0_per_atom, 8)
        except:
            raise FileNotFoundError('OSZICAR does not exist in the folder ' + dir_name)

        # read the final EENTRO (i.e. free energy TOTEN) from OUTCAR using pymatgen if OUTCAR exists,
        # otherwise raise error
        try:
            outcar = Outcar(dir_name + '/' + "OUTCAR")
            EENTRO = outcar.data['EENTRO'] # this is a nested list of EENTRO from OUTCAR
            # get the last item in EENTRO and convert it into float
            EENTRO = float(EENTRO[-1][0])
            # final_fr_energy = outcar.data['final_energy'] # free energy TOTEN
            # save EENTRO in the column Entropy_eV_cell of df_100
            df_100.loc[df_100['id'] == cid, 'Entropy_eV_cell'] = round(EENTRO, 8)
            print('Pymatgen: EENTRO is ', EENTRO)
        except:
            raise FileNotFoundError('OUTCAR does not exist in the folder ' + dir_name)
        # alternatively, we can use in shell
        # EENTRO = os.system('grep "EENTRO" '+dir_name+'/'+'OUTCAR'+' | tail -1 | awk \'{print $5}\'')
        # however, here, python's round will make the very small entropy into 0.00000000, so do not use it here.
print(df_100.head(2))

# save the df_100 to df_100.csv in which Entropy_eV_cell column has 8 decimal places, columns are separted with spacing
df_100.to_csv('df_100.csv', index=False, float_format='%.8f', sep = ' ')