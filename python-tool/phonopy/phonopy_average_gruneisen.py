import yaml
import numpy as np

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "June 12, 2018"

"""
This script read gruneisen.yaml files
and output the average gruneisen parameter
"""

with open('gruneisen.yaml', 'r') as f:
    data = yaml.load(f)

print(list(data))
nqpoint = data['nqpoint']
print(nqpoint)
phonon = data['phonon']
# print(phonon[1])
gruneisen_list = []
for i in range(nqpoint):
    band = phonon[i]['band']
    band_length = len(band)
    for j in range(band_length):
        freq = band[j]['frequency']
        gruneisen = band[j]['gruneisen']
        gruneisen_list.append(gruneisen)
# print(gruneisen_list[:])
gruneisen_array = np.array(gruneisen_list)
# print(gruneisen_array)
sum_gruneisen = sum(gruneisen_list[0:len(gruneisen_list)])
average_gruneisen = sum_gruneisen/nqpoint
print(average_gruneisen)
# print(band[:])
# print(type(freq), type(gruneisen))
