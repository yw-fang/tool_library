from pymatgen.io.vasp import Poscar
# from pymatgen import *
# from numpy import pi
# from numpy import arccos, dot  # pi
# from numpy.linalg import norm
# import numpy as np

yourfile = input('Choose a file: ')
p = Poscar.from_file(yourfile)


coordi = p.structure.frac_coords[:]
print(coordi)

# lattice_vector_R = p.structure.lattice.matrix
# print(lattice_vector_R)
