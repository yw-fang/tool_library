from pymatgen.io.cif import CifParser

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "Nov. 1, 2018"

"""
This script converts the cif to vasp
Note that the output POSCAR will overwirte the former POSCAR.
"""

filename = input('input the cif file: ')
structure_parser = CifParser(filename)
print(structure_parser)
structure = structure_parser.get_structures()
print(structure)
structure[0].to(filename='POSCAR')
