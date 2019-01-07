from pymatgen.io.vasp import Poscar
# from pymatgen import *
# import ase
# Purpose: generate supercell from POSCAR
__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "March 18th, 2018"

"""
current implementation requires POSCAR must
comtain the SELECTIVE DYNAMICS tags.
In future, I will further implemente the one
without this tag.
"""


p = Poscar.from_file('POSCAR')
sd = p.selective_dynamics
if sd:
    print(sd)  # start to consider the implementation of no sleective dynamics
else:
    print('No selective dynamics')
# for x in sd:
#     for y in sd:
#         if y[0] == 'False' or 'F':
#             y[0] = 'True'
#             # print(y[0])
#         if y[1] == 'False' or 'F':
#             y[1] = 'True'
#         if y[2] == 'Flase' or 'F':
#             y[2] = 'True'
# c = p
# c.structure.make_supercell([2, 2, 3])
# c.natoms.append(1)
# 
# c.structure.to(filename='S223POSCAR')
# # print(c.structure.to(fmt="poscar"))
