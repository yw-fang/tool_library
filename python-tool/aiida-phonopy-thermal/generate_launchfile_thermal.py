# This file is used to generate input launch file for thermal conductivity calculations using VASP
# Yue-Wen FANG, created in Feb. 8, 2018
# version 0.0.1 Feb. 9, 2018
# use python 3
# usage: python generate_launchfile_thermal.py

#usage: python generate_launchfile_thermal.py
#make sure you have sampe.py and POSCAR in the current folder.


#import the modules needed to run this script
import os
from os.path import exists
import numpy as np
import ase.units
from ase.utils import basestring

#define spaces: four spaces == indent_N (N=1,2,3..)
indent_1, indent_2, indent_3, indent_4 = (' '*4, ' '*8, ' '*12, ' '*16)

title = input("Enter the title for the output python script: ")
if title.endswith('.py'): #TRUE if input file has a file extension of .py
    pass
else:
    title = title + '.py'
#Remove spaces from the title.
title = title.replace(" ", "_")
print(title,'\n')

#Ask whether to overwirte it if file exists
if  exists(title):
    overwrite = input("The file has been already existed. Overwrite it? y=yes, n=no\n")
    if overwrite.lower() == 'n':
        print('Program exits because you donnot want to overwrite it')
        exit(1)
    else:
        pass



#Read scale, lattice vectors, atomic coordinates from POSCAR
def read_vasp(filename='POSCAR'):
    from ase import Atoms
    from ase.constraints import FixAtoms, FixScaled
    from ase.data import chemical_symbols
    #    import numpy as np
    if isinstance(filename, basestring):
        f = open(filename)
    else:  # Assume it's a file-like object
        f = filename
    """
    By default I think you are using the POSCAR with the format
    that comes with vasp.5.x, in that case, the headline in POSCAR
    is useless, and the 6th line lists elements. 
    
    In case you are using POSCAR in vasp.4.x that does not include
    the element in the sixth line, we also provide the solution in this code.
    In that case, the headline usually shows the elements information
    """
    #read the first two lines of POSCAR
    poscar_headline = f.readline()
    print(poscar_headline)
    scale = float(f.readline().split()[0])
    """
    I put .split() here in case there could be typo errors in the
    second line of POSCAR
    """
    print(scale)
    # Read lattice vectors
    scaled_lattice_vector = []
    for ii in range(3):
        string_vect = f.readline().split()
        float_vect=list(map(float, string_vect))
        """
        an alternative way of converting string_vect to float_vect is
        float_vect=[(float(string_vect(0)), float(string_vect(1)),
        float(string_vect(2))]
        """
        scaled_lattice_vector.append(float_vect)
    print(scaled_lattice_vector)
    lattice_vector = scale * np.array(scaled_lattice_vector)
    """
    it should be mentioned that, in some python library like ase, the
    lattice_vector in my code is defined as 'basis vector', but it's wrong.
    They are two different concepts, in POSCAR, lattice vectors are used.
    """
    print(lattice_vector)

    """
    In future, I may remove the feature supporting vasp.4.x
    At that time, I will pass the elements to atom_symbols directly
    """
    #This part is four future use if only vasp.5.x is supported
    #read elements and the numbers of atoms.
    """
    atom_symbols = f.readline().split()
    print(atom_symbols)
    str_num_of_atom_list = f.readline().split()
    int_num_of_atom_list = list(map(int, str_num_of_atom_list))
    total_num_of_atoms=sum(int_num_of_atom_list)
    print(total_num_of_atoms)
    
    """

    """
    Currently I still support the feature of vasp.4.x.
    Here, the code will check which format we have.
    If the format is vasp.5.x, the 6th line will be atomic symbols
    It it is vasp.4.x format, the 6th line will be number of atoms
    """
    atom_symbols = []
    str_num_of_atom_list = f.readline().split()

    vasp5 = False
    try:
        int(str_num_of_atom_list[0])
        #if it's vasp.5, str_num_of_atom_list[0] must be a str, can
        #cannot be converted into integer
    except ValueError:
        vasp5 = True
        atom_symbols = str_num_of_atom_list
        print(atom_symbols)
        str_num_of_atom_list = f.readline().split()
        int_num_of_atom_list = list(map(int, str_num_of_atom_list))
        total_num_of_atoms = sum(int_num_of_atom_list)
        print(total_num_of_atoms)
#        numofatoms = f.readline().split()
    if not vasp5:
        atom_symbols = poscar_headline.split()
        int_num_of_atom_list = list(map(int, str_num_of_atom_list))
        total_num_of_atoms  = sum(int_num_of_atom_list)
        print(total_num_of_atoms)

    #Now, we check whether Selective dynamics is in POSCAR
    #and read the type of coordinates
    sd = f.readline()
    selective_dynamics = sd[0].lower()=='s'
    print(sd, selective_dynamics)

    if selective_dynamics:
        coordinate_type = f.readline()
        print(coordinate_type)
    else:
        coordinate_type = sd
        print(coordinate_type)
    #check the readed coordinates is in Direct or Cartesian
    cartesian = coordinate_type[0].lower()=='c' or  coordinate_type[0].lower()=='k'
    #initialize the array for atomic coordiantes
    atomic_coordinates =  np.empty((total_num_of_atoms, 3))

    if selective_dynamics:
        #initialize the array for selective flags
        selective_flags = np.empty((total_num_of_atoms, 3), dtype=bool)
    #read atomic coordinates and the selective_flags
    for atom in range(total_num_of_atoms):
        ac = f.readline().split()
        atomic_coordinates[atom] = (float(ac[0]), float(ac[1]), float(ac[2]))
        if selective_dynamics:
            flag_list = []
            for flag in ac[3:6]:
                flag_list.append(flag == 'T')
            selective_flags[atom] = flag_list
    print(selective_flags)

    if isinstance(filename, basestring):
        f.close()
    if cartesian:
        atomic_coordinates *= scale
    else:
        pass
#    print(atomic_coordinates)
    #POSCAR finished reading.

    atomic_coordinates = atomic_coordinates.tolist()
    atomic_coordinates = tuple(map(tuple, atomic_coordinates))
    print(atomic_coordinates)
    print(type(atomic_coordinates))
#    for ii in atomic_coordinates:
#        for jj in ii:
#            jj.tolist()
#    print(list(atomic_coordinates))


    #match the definitions
    cell = lattice_vector
    posinfo={'cell': cell, 'symbol': atom_symbols, 'scaled_positions': atomic_coordinates,
             'tot_num': total_num_of_atoms}
    return posinfo





with open(title,'wt') as f:
    f.write('#############################################################\n')
    f.write('# This script is for generating the launch scirpt used for  #\n')
    f.write('# calculating the thermal conductivity using VASP.          #\n')
    f.write('#############################################################\n')
    f.write('\n'*2)
    f.write('from aiida import load_dbenv, is_dbenv_loaded\n')
    f.write('if not is_dbenv_loaded():\n')
    f.write(indent_1 + 'load_dbenv()\n')
    f.write('\n')
    f.write('from aiida.orm import CalculationFactory, DataFactory, WorkflowFactory, load_node\n')
    f.write('from aiida.work.run import run, submit\n')
    f.write('from aiida.orm.data.structure import StructureData\n')
    f.write('from aiida.orm.data.base import Str, Float, Bool, Int\n')
    f.write("KpointsData = DataFactory('array.kpoints')\n")
    f.write("ParameterData = DataFactory('parameter')\n")
    f.write("import numpy as np\n")
    f.write("# Define structure\n")
#    POSCAR = open('POSCAR', 'rt', encoding='utf-8')
    posinfo = read_vasp()
    print(posinfo,'\n')
#    f.write(posinfo['cell']), f.write can only print strings
    print('cell=[', list(posinfo['cell'][0]), ',', list(posinfo['cell'][1]),
          ',', list(posinfo['cell'][2]), ']', file=f)
    print('symbols = ', posinfo['symbol'], file = f)
    print('scaled_positions = [', file = f)
#    posinfo['scaled_positions'] = posinfo['scaled_positions'].split(',')
#    posinfo['scaled_positions'] = tuple(posinfo['scaled_positions'])
#    print(posinfo['scaled_positions'])
    count=0
    for iii in posinfo['scaled_positions']:
        count = count+1
        if count < posinfo['tot_num']:
            print(iii,',', file=f)
        else:
            print(iii,']', file=f)

    with open('sample.py') as f2:
        for linef2 in f2:
            f.write(linef2)
