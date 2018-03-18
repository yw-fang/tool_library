#Purpose: generate supercell from POSCAR
#Author: Yue-Wen FANG
#Date: 2018 March 18th
from pymatgen.io.vasp import Poscar
from pymatgen import *
import ase

p = Poscar.from_file('POSCAR')
sd = p.selective_dynamics
for x in sd:
    for y in sd:
        if y[0]=='False' or 'F':
            y[0]='True'
            #print(y[0])
        if y[1]=='False' or 'F':
            y[1]='True'
        if y[2]=='Flase' or 'F':
            y[2]='True'
c = p
c.structure.make_supercell([2,2,3])
c.natoms.append(1)

c.structure.to(filename='S223POSCAR')
#print(c.structure.to(fmt="poscar"))
