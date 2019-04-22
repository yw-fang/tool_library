import pandas as pd
import numpy as np
import os
import re

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "Dec 19, 2018"

"""
This script can integrate the DOS, the obtained value is the number of electrons
Note that you must choose a proper energy window you are studying.
"""

def count_electron(file):
    data = pd.read_csv(file, names=['Energy', 'DOS'], skiprows=[0,1],
                       header=None, delim_whitespace=True)
    df_tmp = data[data['Energy'] >= -0.5]
    df = df_tmp[df_tmp['Energy'] <= 0.0]
    electron_number = np.trapz(df['DOS'], df['Energy'])
    return(electron_number)


path="./"
# Read every matched file
filelist = []
for filename in os.listdir(path):
    name, file_extension = os.path.splitext(filename)
    boolean_value = filename[0:7] == 'tot-DOS'
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
print(filelist)

# for filename in os.listdir(path):
for file in filelist:
    print(count_electron(file))
#    boolean_value = filename[0:6] == 'DOS_Ti'
#    if boolean_value:
#        print(filename)
#        print(count_electron(filename))
