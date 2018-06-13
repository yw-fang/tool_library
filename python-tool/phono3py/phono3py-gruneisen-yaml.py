# import pymatgen as mg
import h5py
import os
import re
import numpy as np

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "June 11, 2018"

"""
This script read *.yaml files
and output the life time
"""

path = "./"

# Read every file with extension of '.yaml' in directory
filelist = []
for filename in os.listdir(path):
    name, file_extension = os.path.splitext(filename)
    boolean_value = file_extension == 'gruneisen.yaml'
    if boolean_value:
        if 'kappa' in name:
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
    file_yaml = file + '.yaml'
    data = h5py.File(file_yaml)
    # print(list(data))
    # ltc_300K = data['kappa'][30]
    print(file_yaml)
    #print(list(data))
    # print(ltc_300K)
    #g = data['gamma'][30]
    #g = np.where(g > 0, g, -1)
    #lifetime = np.where(g > 0, 1.0 / (2 * 2 * np.pi * g), 0)
    #print(lifetime)
