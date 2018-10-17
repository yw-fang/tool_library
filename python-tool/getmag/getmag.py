from pymatgen.io.vasp import Poscar
import pandas as pd
"""
Purpose: This script prints the magnetization for user's quick preview.
Read: POSCAR and OUTCAR
Pattern-1: position of ions in fractional coordinates (direct lattice)

Supported vasp 5.xx, vasp 4.xx is not tested.
SOC and non-SOC both implemented.
"""
__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "October 17th, 2018"

# yourfile = input('Choose a file: ')
# p = Poscar.from_file(yourfile)

p = Poscar.from_file('./POSCAR')

structure_summary = p.structure
natoms_list = p.natoms
sum_natoms = sum(natoms_list[0:len(natoms_list)])
coordinates = p.structure[0:sum_natoms]

