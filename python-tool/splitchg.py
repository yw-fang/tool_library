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
__creation_date__ = "June 29th, 2020"
__revision_date__ = "June 29th, 2020"

"""
Usage: splitchg.py
This script is used for splitting CHGCAR/PARCHG from VASP calculations.

"""

############################################################
__version__ = "1.0"
############################################################

def find_chg_files(chg_file):
    try:
        file = open(chg_file, 'r')
    except IOError:
        print('%s may not exist!' % chg_file)
        sys.exit()

def band_energis_from_chg(infile='CHGCAR'):
    find_chg_files(chg_file=infile)

    outcar=[]
    for line in open(infile):
        if line.strip():
            outcar.append(line)
    print(type(outcar))
#
#     band = []
#     headernames=['col1', 'col2','col3','col4','col5','col6']
#     data = pd.read_csv(infile, header=None, delim_whitespace=True,skiprows=14,names=headernames)
#
#
#     print(data.tail(1))
#     print('hello')
#     data.drop(data.tail(2).index, inplace=True) #drop last n rows
#     print(data.tail(1)['col4'])
#     print('hello-1')
#     print(type(data.tail(1)['col4']))
#
#     def isfloat(value):
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False
#


############################################################
def command_line_arg():
    usage = "usage: %prog [options] arg1 arg2"
    par = OptionParser(usage=usage, version= __version__)

    par.add_option('-f', '--file',
            action='store', type="string",
            dest='filename', default='CHGCAR',
            help='location of CHGCAR/PARCHG file')
    return  par.parse_args( )

def main():

    opts, args = command_line_arg()
    band_energies = band_energis_from_chg(opts.filename)


############################################################
if __name__ == '__main__':
    main()
