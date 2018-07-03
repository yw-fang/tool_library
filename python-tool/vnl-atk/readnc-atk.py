# -*- coding: utf-8 -*-
from netCDF4 import Dataset

"""
This script read nc file generated by quantumwise VNL-ATK
Although nanolanguage in ATK is pythonic language, sometimes
you will find netive python is more flexible.

Author: Yue-Wen FANG
Date: 2018 July 3rd

I will not continue working on quantum transport problems
very recently, this script is prepared during the preparation
of a previous transport paper.
"""

dataset = Dataset('plusx.nc')
datakeys = dataset.dimensions.keys()
datavariables = dataset.variables.keys()

print(datakeys)
print(dataset.dimensions[
    'TransmissionSpectrum_gID001_transmission_upup_dim_0'])
print('\t')
print('***********************\n')
print(datavariables)
print('***********************\n')
print(dataset.variables[
    'TransmissionSpectrum_gID001_transmission_upup'])

t = dataset.variables['TransmissionSpectrum_gID001_transmission_upup']
print(list(t))
