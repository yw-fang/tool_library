#!/usr/bin/env python
import pymatgen as mg
import pandas as pd


__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "2020"
__revision_date__ = "March 3, 2020"
"""
This script is used for creating the initial guess of polar/centrosymmetric structure for
nonpolar/noncentrosymmetric structure.
The input: POSCAR
The output: POSCAR-centro
"""

file = './POSCAR'
structure = mg.Structure.from_file(file)
# frac_coords = pd.DataFrame(structure.frac_coords)
# print(frac_coords)
# tmp_coords = frac_coords*(-1) + 1
# print(tmp_coords)
# print(type(tmp_coords))
print(structure)