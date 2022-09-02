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
import pandas as pd
import os



# remind the user to prepare the files for reading in
print("Please prepare the Analysis_Output-revised-revised.dat, and the DFT folders 1-N including")
print("OUTCAR/POSCAR/OSZICAR files")

crys_rslt_file = 'Analysis_Output-revised.dat' # obtained by removing the () for the ID
# read crys_rslt_file with pandas, columns are separated with spacing
col_names = ['preliminary_order', 'No', 'E_eV_atom', 'spg_symbol_tol_0.1', 'spg_symbol_tol_0.2']
df = pd.read_csv(crys_rslt_file, skiprows=[0], names=col_names, delim_whitespace=True, usecols=[0,1,2])

# select the first N structures with lowest energy

# count the number of folders whose names are alphabeta 1, 2, 3, ..., N
N = 0
for i in os.listdir():
    print(i)
    if os.path.isdir(i):
        # try if 'i' is a number, then N is increased by 1
        try:
            int(i)
            N += 1
        # raise an error to remind the user that there are folders whose names are not numbers
        except ValueError:
            print("Warning: this folder '{}' whose name is not a number, it's NOT included in analysis".format(i))
            print("and will not affect the results")
            continue

print("there are {} folders".format(N))
df_100 = df.sort_values(by=['E_eV_atom'])[:N]
df_100['Spg_num_opt'] = np.nan
df_100['Spg_sym_opt'] = np.nan
df_100['Entropy_eV_cell'] = np.nan
print(df.head(10))

# read the CONTCAR in the folders 1 to 3
# and extract the enthalpy and entropy from the OUTCAR/OSZICAR files
for dir_name in range(1,N+1):
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
    n_atoms = opt_struct.num_sites
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

df_100 = df_100.sort_values(by=['E_eV_atom'])
df_100.to_csv('df_100.csv', index=False, float_format='%.8f', sep = ' ')
