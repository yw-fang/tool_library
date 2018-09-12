from pymatgen.io.vasp import Poscar
# from numpy import sqrt
# from numpy import arccos  # dot # pi
# from numpy.linalg import norm
# import numpy as np

yourfile = input('Choose a file: ')
p = Poscar.from_file(yourfile)

# Lattice constants
lattice_vector_R = p.structure.lattice.matrix
# lattice_a = lattice_vector_R[0][0]/sqrt(2)
lattice_c = lattice_vector_R[2][2]/2
# ca_ratio = lattice_c/lattice_a
# print(lattice_a)
print(lattice_c)
# print(ca_ratio)


# Ti disp at the top layer
Ti1 = p.structure.frac_coords[7]
# print(Ti1)
O1_Ti = p.structure.frac_coords[18]
# print(O1_Ti)


# Ti disp at the bottom layer
Ti2 = p.structure.frac_coords[4]
O2_Ti = p.structure.frac_coords[12]
# print(O2_Ti)
disp1 = (Ti1 - O1_Ti)*lattice_c
disp2 = (Ti2 - O2_Ti)*lattice_c
vector_sum_along_z = (disp1 + disp2)/2

print('disp1: ', disp1)
print('disp2: ', disp2)
print('vector_sum_disp_z: ', vector_sum_along_z)


print(lattice_vector_R)

# high_symmetry= np.array([0.5, 0.5, 0.5])
# relative_disp_frac = Ti1-high_symmetry[0]
# relative_disp_cart = relative_disp_frac[1]*lattice_c_hexagonal
# print(relative_disp_cart,' angstrom')
