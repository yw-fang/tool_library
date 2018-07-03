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
"""

with open('gruneisen.yaml', 'r') as f:
    data = yaml.load(f)
h5pydata = h5py.File('mesh.hdf5')

""" get weight of q """
weight = list(h5pydata['weight'])
print('weight lenght is', len(weight))


print(list(data))
nqpoint = data['nqpoint']
print(nqpoint)
phonon = data['phonon']
# print(phonon[1])
gruneisen_list = []
gruneisen_for_band_list = []
gruneisen_q_sum = 0
gruneisen_q = 0
gruneisen_for_band = 0
for i in range(nqpoint):
    band = phonon[i]['band']
    band_length = len(band)
    for j in range(band_length):
        freq = band[j]['frequency']
        gruneisen_for_band = gruneisen_for_band + band[j]['gruneisen']
    averagingband = gruneisen_for_band/6
    gruneisen_for_band_list.append(averagingband)
    # print(gruneisen_for_band_list)
print(gruneisen_for_band_list[-1])
print(len(gruneisen_for_band_list))

s = 0
for x, y in zip(gruneisen_for_band_list, weight):
    s += x * y
average = s / sum(weight)
print(average)
