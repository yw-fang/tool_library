# import pymatgen as mg
from pymatgen.io.vasp import Poscar
# import os
# import re
import numpy as np

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "July 26, 2018"

"""
This script read two files, i.e. PPOSCAR and BPOSCAR,
the output is the primitive axis that can be
used for phonopy or phono3py calculations.

https://atztogo.github.io/phonopy/setting-tags.html
When lattice parameters of unit cell (set by POSCAR)
are the column vectors of au, bu, and cu, those of supercell, ap, bp, cp,
are determined by,
(ap, bp, cp)=(au, bu, cu)Mp

In this script,
au, bu, cu are read from the BPOSCAR, ap, bp, cp are read from PPOSCAR
2018 July 26th
"""

print("Before using this script, please run 'phonopy --symmetry --tol=0.01' ")
print("BPOSCAR and PPOSCAR should exisit in current directory")

# uc_filename = input('input the structure: ')
# p = Poscar.from_file(uc_filename)
pc_file = Poscar.from_file('PPOSCAR')
uc_file = Poscar.from_file('BPOSCAR')
# Lattice constants for PPOSCAR and BPOSCAR in numpy array format
lattice_vector_pc = pc_file.structure.lattice.matrix
lattice_vector_uc = uc_file.structure.lattice.matrix
# print(type(lattice_vector_pc))  # array
# print(type(lattice_vector_uc))  # array
# Lattice constants for PPOSCAR and BPOSCAR in numpy matrix format
lattice_vector_pc = np.matrix(lattice_vector_pc)
lattice_vector_uc = np.matrix(lattice_vector_uc)
# print(type(lattice_vector_pc))  # matrix
# print(type(lattice_vector_uc))  # matrix
# print('lattice_vector_uc in nunpy matrix is', lattice_vector_uc)  # matrix

primitive_axis = np.linalg.solve(lattice_vector_uc.T, lattice_vector_pc.T)
print(primitive_axis)
