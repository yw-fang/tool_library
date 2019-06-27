#!/usr/bin/env python
import pymatgen as mg
import pandas as pd


__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "2018"
__revision_date__ = "June 23th, 2019"
"""
This script shift the fractional coordinates
along one axis in POSCAR
"""

file = './POSCAR'
structure = mg.Structure.from_file(file)
frac_coords = pd.DataFrame(structure.frac_coords)
print(frac_coords[2])
frac_coords[2]=frac_coords[2]+0.233467
print(frac_coords.values)
print(type(frac_coords))
