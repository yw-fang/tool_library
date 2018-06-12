import yaml
# import numpy as np
import h5py

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "June 12, 2018"

"""
This script read gruneisen.yaml and mesh.hdf5 files
and output the average gruneisen parameter

20180612
The present definition of average gruneisen parameter could be incorrect.
The weight of q-point can be read from the mesh.hdf5, or we can extract it
from the gruneisen.yaml. In gruneisen.yaml, the 'multiplicity' is extactly
same to weight
"""

with open('gruneisen.yaml', 'r') as f:
    data = yaml.load(f)
h5pydata = h5py.File('mesh.hdf5')

""" get weight of q """
weight = h5pydata['weight']
print('weight lenght is', len(weight))


print(list(data))
nqpoint = data['nqpoint']
print(nqpoint)
phonon = data['phonon']
# print(phonon[1])
gruneisen_list = []
gruneisen_for_band_list = []
for i in range(nqpoint):
    band = phonon[i]['band']
    band_length = len(band)
    for j in range(band_length):
        freq = band[j]['frequency']
        gruneisen_for_band = band[j]['gruneisen']
        gruneisen_for_band_list.append(gruneisen_for_band)
    gruneisen_q = sum(gruneisen_for_band_list[0:len(gruneisen_for_band_list)])/band_length
    gruneisen_list.append(gruneisen_q)
# print(gruneisen_list[:])
print(len(gruneisen_list))
# gruneisen_array = np.array(gruneisen_list)
# print(gruneisen_array)
# sum_gruneisen = sum(gruneisen_list[0:len(gruneisen_list)])

# average_gruneisen = sum_gruneisen/(nqpoint*band_length)
# average_gruneisen = sum_gruneisen/len(gruneisen_list)
# print(average_gruneisen)
# print(band[:])
# print(type(freq), type(gruneisen))
# new_gruneisen_list=[]
# for g in range(len(gruneisen_list)):
#    new_gruneisen_list[g] = gruneisen_list[g] * weight[g] / sum(weight)
# average_gruneisen = sum(new_gruneisen_list)
# print(average_gruneisen)
# print(sum(weight))
s = 0
for x, y in zip(gruneisen_list, weight):
    s += x * y
average = s / sum(weight)
print(average)
