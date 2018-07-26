# import pymatgen as mg
from pymatgen.io.vasp import Poscar
import os
import re
import numpy as np

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "July 26, 2018"

"""
This script read a structure file (e.g. POSCAR),
and DIM, the output is the primitive axis that can be
used for phonopy or phono3py calculations.

https://atztogo.github.io/phonopy/setting-tags.html
When lattice parameters of unit cell (set by POSCAR)
are the column vectors of au, bu, and cu, those of supercell, ap, bp, cp,
are determined by,
(ap, bp, cp)=(au, bu, cu)Mp

In this script, I plan to read
au, bu, cu  from the POSCAR, as for ap, bp, cp,
I want to use phonopy module to get them.
In that case, we can get Mp according to above euqation.
2018 July 26th, now it hasn't been finished.
"""

# uc_filename = input('input the structure: ')
# p = Poscar.from_file(uc_filename)
p = Poscar.from_file('POSCAR-EDIFFG-6')
c = p
# Lattice constants
lattice_vector_R = p.structure.lattice.matrix
print(lattice_vector_R)

c.structure.make_supercell([2
