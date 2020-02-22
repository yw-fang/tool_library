import os
from optparse import OptionParser

############################################################
__version__ = "0.1"
############################################################

def find_vasp_files(vasp_file):
    try:
        file = open(vasp_file, 'r')
    except IOError:
        print('%s may not exist!' % vasp_file)
        sys.exit()

def update_fermi_outcar(infile,e_fermi):
    # print(e_fermi)
    find_vasp_files(vasp_file=infile)
    outcar = [line for line in open(infile) if line.strip()]
    for ii, line in enumerate(outcar):
        if 'E-fermi' in line:
            print(ii)
            print(line)



############################################################
def command_line_arg():
    usage = "usage: %prog [options] arg1 arg2"
    par = OptionParser(usage=usage, version= __version__)

    par.add_option('-e',
            action='store', type="float",
            dest='fermi_energy',
            help='The value of Fermi energy')

    return par.parse_args( )

############################################################
def main():
    opts, args = command_line_arg()
    e_fermi = opts.fermi_energy
    print(e_fermi)
    infile='OUTCAR'
    update_fermi_outcar(infile=infile,e_fermi=e_fermi)


if __name__ == '__main__':
    main()
