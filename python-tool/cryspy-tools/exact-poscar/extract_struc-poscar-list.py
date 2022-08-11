#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] ./extract_struc-poscar.py data/pkl_data/opt_struc_data.pkl -i 1 2
# [Purpose] Extract structures from pkl_data/opt_struc_data.pkl or pkl_data/init_struc_data.pkl
#          History
#  HISTORY
#     2022/08/09 : Script creation, export into POSCAR format, and create folders for DFT local optimizations
# ------------------------------------------------------------------

import argparse
import pickle
# analyze space group of POSCAR using pymatgen
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
# use pandas to read the data/cryspy_rslt_energy_asc_after1250struct
import pandas as pd
import os

crys_rslt_file = 'data/cryspy_rslt_energy_asc_after1250struct'
# read crys_rslt_file with pandas, columns are separated with spacing
col_names = ['id', 'Gen', 'Spg_num', 'Spg_sym', 'Spg_num_opt', 'Spg_sym_opt',  'E_eV_atom', 'Magmom', 'Opt']
df = pd.read_csv(crys_rslt_file, skiprows=[0], names=col_names, delim_whitespace=True, usecols=[0,1,4,5,6])
# print(df.head(10))

# select the first 100 structures with lowest energy
df_100 = df.sort_values(by=['E_eV_atom'])[:10]
#size od df_100
print(df_100.shape)
# extract the structure from data/pkl_data/opt_struc_data.pkl according to the id in df_100
with open('data/pkl_data/opt_struc_data.pkl', 'rb') as f:
    struc_data = pickle.load(f)
    # loop through the id in df_100
    for cid in df_100['id']:
        # print the structure with id cid
        print(struc_data[cid])
        # print the space group of the structure with id cid
        spg_symbol = SpacegroupAnalyzer(struc_data[cid], symprec=.1).get_space_group_symbol()
        # print the space group number of the structure with id cid
        spg_number = SpacegroupAnalyzer(struc_data[cid], 0.1).get_space_group_number()
        # export the structure with id cid to POSCAR format
        struc_data[cid].to(fmt='POSCAR', filename='{}.vasp'.format(str(cid)+'_'+str(spg_number)))
        # create a folder for each structure with id cid and spg_number if the folder does not exist
        if not os.path.exists(os.path.join(str(cid)+'_'+str(spg_number))):
            os.mkdir(str(cid)+'_'+str(spg_number))
        os.rename(str(cid)+'_'+str(spg_number)+'.vasp', str(cid)+'_'+str(spg_number)+'/POSCAR')
        # copy all the files in ./input/ to the each folder with POSCAR
        os.system('cp -r ./input/* {}'.format(str(cid)+'_'+str(spg_number)+'/'))
        # cd each folder with POSCAR and sbatch the job script
        os.system('cd {} && sbatch job-calypso-greene.sh'.format(str(cid)+'_'+str(spg_number)))
        # cd ../ to go back to the parent folder
        os.system('cd ../')
