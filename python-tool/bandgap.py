#!/usr/bin/env python

from pymatgen.io.vasp.outputs import Vasprun

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "April 17th, 2019"
__revision_date__ = "April 17th, 2019"

"""
Calculating band gap for VASP calculations.
Usage: python bandgap.py
"""

"""
In pymatgen, there are several different ways to extracting band gap.
Here, I introduce two methods using "eigenvalue_band_properties"
and "get_band_structure".

About their differences:
The two methods define differently what is the band gap.
The eigenvalue_band_properties looks at occupations. Here there are partial occupations of your upper bands.
Therefore this depends on the smearing you use.
The Bandstructure.get_band_gap() looks at bands above and below fermi level.
Here there are bands crossing the fermi level. So the method considers it as a metal and gives you a zero band gap.
(see ref: https://github.com/materialsproject/pymatgen/issues/455)
In general, get_band_structure works better.
"""

"""
In addition to the two methods in pymatgen, here, I also provide third method
in which band gap was calculated from DOSCAR to have a cross-check.
"""

# Method 1 and 2 by using pymatgen
parse_vasprun = Vasprun('vasprun.xml')
print(parse_vasprun)

(gap, cbm, vbm, is_direct) = parse_vasprun.eigenvalue_band_properties
print('pymatgen, eigenvalue_band_properties')
print('gap,', "cbm,", "vbm,", "is_direct")
print(gap, cbm, vbm, is_direct)
print('\t')
print('pymatgen, get_band_structure')
bs = parse_vasprun.get_band_structure()
gap = bs.get_band_gap()
print(gap['energy'])

# Method 3 by calculating band gap from DOSCAR
"""
This was inspired by Jeffw Doak https://github.com/jeffwdoak/vasp_scripts/blob/master/vasp_scripts/bandgap.py
I implemented in a clear way for my understanding.
"""

## to do list ##
## 1. read DOSCAR
## 2. calculate band gap