#!/usr/bin/env python

from pymatgen.io.vasp import Poscar
import os.path
import pymatgen.symmetry.bandstructure as psb
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "July 18th, 2019"
__revision_date__ = "July 18th, 2019"

"""
This script can be used to generate K-path for different crystal structures.
The K-path follows the paper: https://doi.org/10.1016/j.commatsci.2010.05.010
At present, this script only prints the high symmetry points on the k-path
"""

#################READ FILE######################
def readpos(struct_file):
    if os.path.exists(struct_file):
        p = Poscar.from_file(struct_file)
        return(p)

#################REFORMAT PRIMITIVE CELL##########
"""
primtive cell is reformated to match Setyawan/Curtarolo convention
in order to work with the current k-path.     
"""
def reformat_prim(structure):
    sym = SpacegroupAnalyzer(structure.structure)
    prim = sym.get_primitive_standard_structure()
    return(prim)

#################GENERATE KPATH######################
structure = readpos('POSCAR')
prim = reformat_prim(structure=structure)
high_k_path = psb.HighSymmKpath(prim.get_primitive_structure())
high_k_points = high_k_path.kpath
high_k_points_frac_coord = high_k_points['kpoints']
#################WRITE TO SCREEN######################
for key in high_k_points_frac_coord.keys():
    print(key, high_k_points_frac_coord[key])
  
#################WRITE TO FILE######################
with open('high-kpoints', 'w') as f:
    for key in high_k_points_frac_coord.keys():
        f.write("{} {}\n".format(key, high_k_points_frac_coord[key]))
