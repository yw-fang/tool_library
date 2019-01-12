from pymatgen.io.vasp import Poscar
from optparse import OptionParser
# from pymatgen import *
# Purpose: generate supercell from POSCAR
__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "March 18th, 2018"
__revision_date__ = "Jan 7th, 2019"

"""
This script can be used to generate supercell from POSCAR file
Available and unavailable SELECTIVE DYNAMICS tags
have been both implemented, 2019 Jan 7th.

Usage: python generate_supercell.py -i filename -s 2 2 2
By default, filename is 'POSCAR'; the supercell size is 3*3*3
"""

def readpos(file):
    p = Poscar.from_file(file)
    sd = p.selective_dynamics
    if sd:
        for x in sd:
            for y in sd:
                if y[0] == 'False' or 'F':
                    y[0] = 'True'
                    # print(y[0])
                if y[1] == 'False' or 'F':
                    y[1] = 'True'
                if y[2] == 'Flase' or 'F':
                    y[2] = 'True'
        return(p)
    else:
        print('No selective dynamics')
        return(p)




############################################################
def command_line_arg():
    usage = "usage: %prog [options] arg1 arg2"
    par = OptionParser(usage=usage)

    # par.add_option('-f', '--file',
    #         action='store', type="string",
    #         dest='filename', default='OUTCAR',
    #         help='location of OUTCAR')
    par.add_option('-s', '--supercellsize', nargs=3,
            action='store', type="int", dest='supercellsize',
            default=(3, 3, 3),
            help='supercell size')


    par.add_option('-i', '--inputfile',
            action='store', type="string",
            dest='inputfile', default='POSCAR',
            help='location of POSCAR')

    return par.parse_args()
    # print(c.structure.to(fmt="poscar"))


def make_supercell(supercellsize, filename):
    c = readpos(filename)
    c.structure.make_supercell(supercellsize)
    c.natoms.append(1)
    return(c)


if __name__ == '__main__':
    opts, args = command_line_arg()
    filename = opts.inputfile
    print(filename)
    print(list(opts.supercellsize))
    supercellsize = list(opts.supercellsize)
    supercell_structure = make_supercell(supercellsize, filename)
#    print(supercell_structure)
    supercell_structure.structure.to(filename='POSCAR.supercell')
