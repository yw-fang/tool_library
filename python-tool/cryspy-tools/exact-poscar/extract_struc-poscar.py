#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] ./extract_struc-poscar.py data/pkl_data/opt_struc_data.pkl -i 1 2
# [Purpose] Extract structures from pkl_data/opt_struc_data.pkl or pkl_data/init_struc_data.pkl
#          History
#  HISTORY
#     2022/08/09 : Script creation, export into POSCAR format
# ------------------------------------------------------------------

import argparse
import pickle
# analyze space group of POSCAR using pymatgen
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

if __name__ == '__main__':
    # ---------- argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all_id', help='flag for all structures', action='store_true')
    parser.add_argument('-i', '--index', help='structure ID', type=int, nargs='*')
    parser.add_argument('-s', '--symmetrized', help='flag for symmetrized structure', action='store_true')
    parser.add_argument('infile', help='input file')
    args = parser.parse_args()

    # ---------- load struc_data
    with open(args.infile, 'rb') as f:
        struc_data = pickle.load(f)

    # ---------- write POSCAR
    if args.index:
        for cid in args.index:
            # print(struc_data[cid].to(fmt='poscar'))
            print(struc_data[cid])
            # print(SpacegroupAnalyzer(struc_data[cid], symprec=.1).get_space_group_symbol())
            # print(SpacegroupAnalyzer(struc_data[cid], 0.1).get_space_group_symbol())
            print(SpacegroupAnalyzer(struc_data[cid], 0.1).get_space_group_number())
            spg_no =  SpacegroupAnalyzer(struc_data[cid], 0.1).get_space_group_number()
            # struc_data[cid].to(fmt='cif', filename='{}.cif'.format(cid))
            struc_data[cid].to(fmt='POSCAR', filename='{}.vasp'.format(str(cid)+'_'+str(spg_no)))
        raise SystemExit()