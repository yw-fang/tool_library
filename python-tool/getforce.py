#!/usr/bin/env python

from pymatgen.io.vasp.outputs import Outcar
from optparse import OptionParser
import sys
import os.path

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "April 16th, 2019"
__revision_date__ = "April 17th, 2019"

"""
Get forces of atoms from OUTCAR file.
To do
"""

def read_outcar(outcar_file):
    if os.path.exists(outcar_file):
        f = Outcar(outcar_file)
#        with Outcar(outcar_file) as f:
#            print(f)
        forces = f.read_table_pattern(
            header_pattern=r"\sPOSITION\s+TOTAL-FORCE \(eV/Angst\)\n\s-+",
            row_pattern=r"\s+[+-]?\d+\.\d+\s+[+-]?\d+\.\d+\s+[+-]?\d+\.\d+\s+([+-]?\d+\.\d+)\s+([+-]?\d+\.\d+)\s+([+-]?\d+\.\d+)",
            footer_pattern=r"\s--+",
            postprocess=lambda x: float(x),
            last_one_only=False
        )
        return(forces)
    else:
        print("No OUTCAR file reads in, at least make sure you have '{}' by default".format(outcar_file),
              file=sys.stderr)

def command_line_arg():
    usage = "usage: %prog [options] arg1 arg2"
    par = OptionParser(usage=usage)

    par.add_option('-i', '--inputfile',
            action='store', type="string",
            dest='inputfile', default='OUTCAR',
            help='location of OUTCAR')

    return par.parse_args()

if __name__ == '__main__':
    opts, args = command_line_arg()
    filename = opts.inputfile
#    print(filename)
    forces = read_outcar(filename)
    atom_index = 0
    print('#################################################')
    print('atom_index', '###', 'TOTAL-FORCE (eV/Angst)')
    for i in forces:
        for j in i:
            atom_index = atom_index + 1
            print(atom_index,'###', j)
