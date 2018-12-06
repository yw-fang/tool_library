from pymatgen.io.cif import CifParser
import os
import re

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "Dec. 6, 2018"

"""
This script converts a group of cif files to POSCAR files
"""
path = "./"

# Read every file with extension of '.vasp' in directory
filelist = []
for filename in os.listdir(path):
    name, file_extension = os.path.splitext(filename)
    boolean_value = file_extension == '.cif'
    if boolean_value:
        filelist.append(name)

# #################define functions##################
def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    or
    https://stackoverflow.com/questions/5967500/
    how-to-correctly-sort-a-string-with-a-number-inside?
    utm_medium=organic&utm_source=google_rich_qa&utm_campai
    gn=google_rich_qa
    '''
    return [atoi(c) for c in re.split('(\d+)', text)]
# ####################################################


filelist.sort(key=natural_keys)
# print(filelist)

i=0
for file in filelist:
    i=i+1
    file_cif = file + '.cif'
    structure_parser = CifParser(file_cif)
    print(structure_parser)
    structure = structure_parser.get_structures()
    print(structure)
    structure[0].to(filename='POSCAR')
    for filename in os.listdir("."):
        if filename=='POSCAR':
            os.rename(filename, filename+'_'+str(i))


# filename = input('input the cif file: ')
# structure_parser = CifParser(filename)
# print(structure_parser)
# structure = structure_parser.get_structures()
# print(structure)
# structure[0].to(filename='POSCAR')
