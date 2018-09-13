from pymatgen.io.vasp import Poscar
import pandas as pd
# Purpose: This script is similar to the 'vn POSCAR' command
# The difference is that I sort the coordinates along the b direction
__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "September 13th, 2018"

# yourfile = input('Choose a file: ')
# p = Poscar.from_file(yourfile)

p = Poscar.from_file('./SrTiO3-BiBaTi2O6.vasp')

structure_summary = p.structure
natoms_list = p.natoms
sum_natoms = sum(natoms_list[0:len(natoms_list)])
coordinates = p.structure[0:sum_natoms]


fractional_coord_list = []
for i in coordinates:
    fractional_coord_list.append(i.frac_coords)
    

df = pd.DataFrame({'frac_coordinates':fractional_coord_list,'number': range(1,sum_natoms+1)},index = range(1,sum_natoms+1))

#split the 'frac_coordinates' column into three columns of 'x', 'y', and 'z'
df[['x','y','z']] = pd.DataFrame(df.frac_coordinates.values.tolist(), index=df.index) 

df1 = df.copy()
df2 = df1.sort_values(by=['y'], ascending=False)
number = df2.number

# In this mode, every ABO3 layer contains 5 atoms
# hence I group them by every 5 atoms
for i,j,k,l,m in zip(*[iter(number)]*5): 
#     print(i,j,k,l,m)
    print("{}+{}+{}+{}+{}".format(str(i),str(j), str(k), str(l), str(m)))