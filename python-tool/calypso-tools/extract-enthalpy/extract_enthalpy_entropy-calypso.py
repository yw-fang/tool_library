#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] ./extract_enthalpy_entropy.py
# [Purpose] Extract enthalpy and entropy from the VASP calculation for CrySPY structures
#          History
#  HISTORY
#     2022/08/11 : Script creation
#     2022/08/12 : Use pymatgen to read OSZICAR and OUTCAR
# ------------------------------------------------------------------

import argparse
import pickle
# analyze space group of POSCAR using pymatgen
import numpy as np
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.io.vasp.outputs import Oszicar, Outcar
from pymatgen.core import Structure
# use pandas to read the data/cryspy_rslt_energy_asc_after1250struct
import pandas as pd
import os

# remind the user to prepare the files for reading in
print("Please prepare the Analysis_Output-revised-revised.dat, and the DFT folders 1-N including")
print("OUTCAR/POSCAR/OSZICAR files")

crys_rslt_file = 'Analysis_Output-revised.dat' # obtained by removing the () for the ID
# read crys_rslt_file with pandas, columns are separated with spacing
col_names = ['preliminary_order', 'No', 'E_eV_atom', 'spg_symbol_tol_0.1', 'spg_symbol_tol_0.2']
df = pd.read_csv(crys_rslt_file, skiprows=[0], names=col_names, delim_whitespace=True, usecols=[0,1,2])

# select the first 100 structures with lowest energy
df_100 = df.sort_values(by=['E_eV_atom'])[:3]
df_100['Spg_num_opt'] = np.nan
df_100['Spg_sym_opt'] = np.nan
df_100['Entropy_eV_cell'] = np.nan
print(df.head(10))

# read the CONTCAR in the folders 1 to 3
# and extract the enthalpy and entropy from the OUTCAR/OSZICAR files
for dir_name in range(1,4):
    dir_name = str(dir_name)
    opt_struct = Structure.from_file(dir_name + '/' + "CONTCAR")
    # analyze the space group using SpacegroupAnalyzer, if RuntimeError or TypeError happens, raise the error
    try:
        spg_sym_opt = SpacegroupAnalyzer(opt_struct, symprec=.1).get_space_group_symbol()
    except RuntimeError:
        print("RuntimError: Space group analysis failed for structure " + dir_name)
        spg_sym_opt = "None"
        continue
    except TypeError:
        print("TypeError: Space group analysis failed for structure " + dir_name)
        spg_sym_opt = "None"
        continue
    # save spg_sym_opt to the column Spg_sym_opt in the df_100
    # df_100.loc[df_100['preliminary_order'] == dir_name, 'Spg_sym_opt'] = spg_sym_opt
    df_100.loc[df_100['preliminary_order'] == float(dir_name), 'Spg_sym_opt'] = spg_sym_opt
    print("*****")
    print(spg_sym_opt)
    try:
        spg_number_opt = SpacegroupAnalyzer(opt_struct, symprec=.1).get_space_group_number()
    except RuntimeError:
        print("Space group analysis failed for structure " + dir_name)
        spg_number_opt = "None"
        continue
    except TypeError:
        print("Space group analysis failed for structure " + dir_name)
        spg_number_opt = "None"
        continue
    #         df_100.loc[df_100['id'] == cid, 'Entropy_eV_cell'] = round(entropy, 8)
    print("*****")
    print(spg_number_opt)
    # df_100.loc[df_100['preliminary_order'] == float(dir_name), 'Spg_num_opt'] = spg_number_opt
    df_100.loc[df_100['preliminary_order'] == float(dir_name), 'Spg_num_opt'] = spg_number_opt

    # how many atoms in the opt_struct
    # n_atoms = opt_struct.num_sites
    n_atoms = 1
    # print(spg_symbol_opt)

    try:
        oszicar = Oszicar(dir_name + '/' + "OSZICAR")
        E0 = oszicar.final_energy
        E0_per_atom = round(E0 / n_atoms, 8)  # enthalpy eV normalized to per atom
        # save E0_per_atom in the column E_eV_atom of df_100
        df_100.loc[df_100['preliminary_order'] == float(dir_name), 'E_eV_atom'] = E0_per_atom
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
        df_100.loc[df_100['preliminary_order'] == float(dir_name), 'Entropy_eV_cell'] = round(EENTRO, 8)
        print('Pymatgen: EENTRO is ', EENTRO)
    except:
        raise FileNotFoundError('OUTCAR does not exist in the folder ' + dir_name)