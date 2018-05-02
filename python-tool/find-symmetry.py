__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "April 27, 2018"

import pymatgen as mg
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
# pymatgen.symmetry.analyzer acts as an interface of 'spglib' for pymatgen
import os
import re


path = "./"

# Read every file with extension of '.vasp' in directory
filelist = []
for filename in os.listdir(path):
    name, file_extension = os.path.splitext(filename)
    boolean_value = file_extension == '.vasp'
    if boolean_value:
        filelist.append(name)
# print(filelist)


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
# ###################################################


filelist.sort(key=natural_keys)
# print(filelist)

for file in filelist:
    file = file + '.vasp'
    structure = mg.Structure.from_file(file)
#     print(structure.volume)
    symmetry = SpacegroupAnalyzer(structure, 0.001)
    print('The space group of', file, 'is {}'.
          format(symmetry.get_space_group_symbol()))
