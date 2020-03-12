#!/usr/bin/env python

import sys
import os
import re
import numpy as np
import pandas as pd
from optparse import OptionParser

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "March 12th, 2020"
__revision_date__ = "XX XXth, 2020"

############################################################
__version__ = "1.0"
############################################################

def find_bxsf_files(bxsf_file):
    try:
        file = open(bxsf_file, 'r')
    except IOError:
        print('%s may not exist!' % bxsf_file)
        sys.exit()

def band_energis_from_bxsf(infile='wannier90.bxsf'):
    find_bxsf_files(bxsf_file=infile)

    outcar=[]
    for line in open(infile):
        if line.strip():
            outcar.append(line)
    print(type(outcar))
    # print(outcar[0:1])

    band = []
    headernames=['col1', 'col2','col3','col4','col5','col6']
    data = pd.read_csv(infile, header=None, delim_whitespace=True,skiprows=14,names=headernames)
    # data_list = data.values.tolist()
    # print(type(data_list))
    # print(data_list[0])
    # print(data['col1'])

    print(data.tail(1))
    print('hello')
    data.drop(data.tail(2).index, inplace=True) #drop last n rows
    print(data.tail(1)['col4'])
    print('hello-1')
    print(type(data.tail(1)['col4']))

    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    band_energies = []

    for columns in data:
        for i in data[columns].values.tolist():
            if isfloat(i):
                 band_energies.append(float(i))
    print(len(band_energies))
    print(band_energies[-1])

    E_F = 3.65 # eV
    carrier_kpoint = 0
    for energy in band_energies:
        if energy <= E_F:
            carrier_kpoint = carrier_kpoint + 1
    # stricktly, the value of len(band_energies) should be same to Kx * Ky * Kz in Wannier calcultions
    kx = 51
    ky = 51
    kz = 51
    kgrid_number_from_wannier = kx * ky * kz
    print("electron-number: ", 2*carrier_kpoint/kgrid_number_from_wannier)
    hole_number = 2*(kgrid_number_from_wannier-carrier_kpoint)/kgrid_number_from_wannier
    print('hole-number: ', hole_number)


############################################################
def command_line_arg():
    usage = "usage: %prog [options] arg1 arg2"
    par = OptionParser(usage=usage, version= __version__)

    par.add_option('-f', '--file',
            action='store', type="string",
            dest='filename', default='wannier90.bxsf',
            help='location of bxsf file')
    return  par.parse_args( )

def main():

    opts, args = command_line_arg()
    band_energies = band_energis_from_bxsf(opts.filename)


############################################################
if __name__ == '__main__':
    main()
