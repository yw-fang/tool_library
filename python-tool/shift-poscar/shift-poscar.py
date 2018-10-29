import pymatgen as mg
import pandas as pd

file = './POSCAR'
structure = mg.Structure.from_file(file)
frac_coords = pd.DataFrame(structure.frac_coords)
print(frac_coords[2])
frac_coords[2]=frac_coords[2]+0.233467
print(frac_coords.values)
print(type(frac_coords))

