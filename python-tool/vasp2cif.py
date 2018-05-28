import pymatgen as mg
import os
import re

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "May 1, 2018"


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
# ####################################################


filelist.sort(key=natural_keys)
# print(filelist)

for file in filelist:
    file_vasp = file + '.vasp'
    structure = mg.Structure.from_file(file_vasp)
    file_cif = file + '.cif'
    file_cif_P1 = file + '_P1.cif'
# export symmetried CIF, symprec controls the tolerance
    mg.io.cif.CifWriter(structure, symprec=0.1).write_file(file_cif)
# export CIF with P1 symmetry
    structure.to(filename=file_cif_P1)
