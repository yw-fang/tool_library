import numpy as np

"""
This scirpt is used for generating input files for quantum espresso,
it's in developping.
This script was based on https://github.com/eveshower/qediy
"""

def bohr():
    return 0.52917720859

def Ry():
    return 13.6056925250

def read_finalcoord(fnam='structure-relaxed.dat',nat=1000, vc_relax=True,cell=[(),(),()]):
    ''' read in final coordinate of Quantum-ESPRRESO pw.x vc-relax output,
        you can get it from get_final_coordinates.sh

        example:
CELL_PARAMETERS (alat= 12.21140000)
  -0.500000000   0.000000000   0.500000000
   0.000000000   0.500000000   0.500000000
  -0.500000000   0.500000000   0.000000000
ATOMIC_POSITIONS (crystal)
Cd       0.000000000   0.000000000   0.000000000
Te       0.250000000   0.250000000   0.250000000
    '''
    from ase import Atoms, Atom
    fileobj=open(fnam)
    line = fileobj.readline()
    if line[0]=='C':
        pass
    elif line[0]=='A':
        raise NotImplementedError
        exit
    else:
        raise AssertionError
        exit

    line = line.replace(")", " ) ")
    data=line.split()

    lattice=Atoms(pbc=True)
    alat=float(data[2])*bohr()

    if vc_relax:
        for i in range(3):
            line = fileobj.readline()
            data=line.split()
            cell[i]=(alat*float(data[0]),alat*float(data[1]),alat*float(data[2]))

        lattice.set_cell(cell,scale_atoms=False)
        line=fileobj.readline()
        line=fileobj.readline()
    else:
        lattice.set_cell(cell,scale_atoms=False)

    atoms_pos = []
    for i in range(nat):
        line=fileobj.readline()
        entries = line.split()
        if len(entries) == 0 or (entries[0] == 'End'):
            break
        symbol = entries[0]
        x = float(entries[1])
        y = float(entries[2])
        z = float(entries[3])
        atoms_pos.append((x,y,z))
        lattice.append(Atom(symbol=symbol))
    lattice.set_scaled_positions(atoms_pos)

    return lattice

def cell_redefine(lattice):
    '''Re-define unit cell to have the x-axis parallel with a surface vector and z perpendicular to the surface

    lattice: Atoms object
        The cell is rotated.
    '''
    from numpy.linalg import norm
    a1, a2, a3 = lattice.cell
    lattice.set_cell([a1, a2, np.cross(a1, a2) * np.dot(a3, np.cross(a1, a2)) /norm(np.cross(a1, a2))**2])

    a1, a2, a3 = lattice.cell
    lattice.set_cell([(norm(a1), 0, 0),
                      (np.dot(a1, a2) / norm(a1),
                      np.sqrt(norm(a2)**2 - (np.dot(a1, a2) / norm(a1))**2), 0),
                      (0, 0, norm(a3))],
                      scale_atoms=True)

def rh2hex(lattice):
    """ return Atomic objects with 3 times volume hexgonal cell of the input rhombohedral cell
        exist slightly different cut vectors, see ITC vol. A
    """
    from ase.utils.geometry import cut
    re=cut(lattice, (1.0, -1.0, 0.0), (0.0, 1.0, -1.0), (1.0, 1.0,1.0), origo=(0,0,0))

    return re

def get_at_pos_tag(lattice,cell_redefine=False, is_ibrav0=False,cell_unit='bohr',constrain=None):
    """generate tag ATOMIC_POSITIONS CELL_PARAMETERS in PWscf input file
    """
    at_pos=""
    at_cell=""

    at_pos+='ATOMIC_POSITIONS (crystal)\n'
    pos=lattice.get_scaled_positions()

    aug=np.zeros(lattice.get_number_of_atoms(),dtype=[('symbol','S10'),('z','float32')])

    for i in range(lattice.get_number_of_atoms()):
        aug[i]=(lattice[i].symbol,lattice[i].position[2])

    ind=np.argsort(aug,order=('symbol','z'))

    for na in range(lattice.get_number_of_atoms()):
        i=ind[na]
        if constrain is None:
            at_pos+='%3s %15.9lf %15.9lf %15.9lf\n' % (lattice[i].symbol, pos[i][0], pos[i][1], pos[i][2])
        else:
            at_pos+='%3s %15.9lf %15.9lf %15.9lf %d %d %d\n' % (lattice[i].symbol, pos[i][0], pos[i][1], pos[i][2], constrain[i][0],constrain[i][1],constrain[i][2])
    if is_ibrav0:
        if cell_unit=='bohr' :
            scale=bohr()
        elif cell_unit=='angstrom' :
            scale=1.0
        elif cell_unit=='alat' :
            scale=np.sqrt(np.sum(lattice.get_cell()[0]**2))
        elif cell_unit[:16]=='alat= 1.88972613':
            scale=1.0
        else:
            print('unknown cell unit \'%s\'' % cell_unit)
            raise AssertionError

        at_cell+= 'CELL_PARAMETERS {%s}\n' % (cell_unit)
        for i in range(3):
            for j in range(3):
                at_cell+="  %15.9lf" % (lattice.get_cell()[i][j]/scale)
            at_cell+="\n"

    return (at_pos,at_cell)

def get_at_pp(lattice):
    """get atomic pseudopotential lines for PWscf input
    """
    raise NotImplementedError


def inp_to_file(fnam, inp_tags):
    """ write PWscf input file 'fnam', work with inp_tags
    """
    inp_file=open(fnam,'w')
    inp_file.write(inp_tags)

def get_k(lattice,kspacing=0.05):
    rc=lattice.get_reciprocal_cell()
    b1 = np.sqrt(np.dot(rc[0],rc[0]))
    b2 = np.sqrt(np.dot(rc[1],rc[1]))
    b3 = np.sqrt(np.dot(rc[2],rc[2]))
    kpts = (max(1,int(np.ceil(b1/kspacing))), max(1,int(np.ceil(b2/kspacing))), max(1,int(np.ceil(b3/kspacing))) )

    return kpts

def get_ntyp(lattice):
    return len(set(lattice.get_chemical_symbols()))

def get_atomic_weight(at):
    sym_wt={'H': 1.00794, 'He': 4.00260, 'Li': 6.941, 'Be': 9.01218, 'B': 10.811,
        'C': 12.0107, 'N': 14.00674, 'O': 15.9994, 'F': 18.99840, 'Ne': 20.1797,
        'Na': 22.98977, 'Mg': 24.3050, 'Al': 26.98154, 'Si': 28.0855, 'P': 30.97376,
        'S': 32.066, 'Cl': 35.4527, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078,
        'Sc': 44.95591, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.93805,
        'Fe': 55.845, 'Co': 58.93320, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.39,
        'Ga': 69.723, 'Ge': 72.61, 'As': 74.92160, 'Se': 78.96, 'Br': 79.904,
        'Kr': 83.80, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585, 'Zr': 91.224,
        'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98.0, 'Ru': 101.07, 'Rh': 102.90550,
        'Pd': 106.42, 'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.710,
        'Sb': 121.760, 'Te': 127.60, 'I': 126.90447, 'Xe': 131.29, 'Cs': 132.90545,
        'Ba': 137.327, 'La': 138.9055, 'Ce': 140.116, 'Pr': 140.90765, 'Nd': 144.24,
        'Pm': 145.0, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25, 'Tb': 158.92534,
        'Dy': 162.50, 'Ho': 164.93032, 'Er': 167.26, 'Tm': 168.93421, 'Yb': 173.04,
        'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207,
        'Os': 190.23, 'Ir': 192.217, 'Pt': 195.078, 'Au': 196.96655, 'Hg': 200.59,
        'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.98038, 'Po': 209.0, 'At': 210.0,
        'Rn': 222.0, 'Fr': 223.0, 'Ra': 226.0, 'Ac': 227.0, 'Th': 232.0381,
        'Pa': 231.03588, 'U': 238.0289, 'Np': 237.0, 'Pu': 244.0, 'Am': 243.0,
        'Cm': 247.0, 'Bk': 247.0, 'Cf': 251.0, 'Es': 252.0, 'Fm': 257.0,
        'Md': 258.0, 'No': 259.0, 'Lr': 262.0, 'Rf': 261.0, 'Db': 262.0,
        'Sg': 266.0, 'Bh': 264.0, 'Hs': 277.0, 'Mt': 268.0}
    return str(sym_wt[at])

def get_ATOMIC_SPECIES(lattice, upf_filenames=None):
    str="ATOMIC_SPECIES\n"
    species=set(lattice.get_chemical_symbols())
    if upf_filenames is None:
        for i in species:
            str=str+' '+i+' '+get_atomic_weight(i)+' '+i+'.UPF\n'
    else:
        raise(NotImplementedError)
    return str


def inp_tags(lattice, ATOMIC_SPECIES, calculation='scf',pseudo_dir='./',
             outdir='OUT', forc_conv_thr=5.0e-4,  ecutwfc=50.0, ecutrho=500.0,
             Apply_E_Field=None, kpts=(-1,-1,-1)):
    """make PWscf input file tags

    default values, see PWscf documents
     Apply_E_Field:  None | float
         None, if not None, set to 'eamp' the value of electric field

     kpts: tuple of 3 int
         (6,6,1) , automatic k mesh
    """

    CONTROL = """&CONTROL
   calculation='%s',
   pseudo_dir='%s',
   outdir='%s',
   forc_conv_thr=%lf,
   disk_io='low',
   prefix='pwscf',
   verbosity='high',
   tprnfor=.true.
   tstress=.true.
/
""" % (calculation, pseudo_dir, outdir, forc_conv_thr)

    SYSTEM="""&SYSTEM
   ibrav = 0,
   celldm(1) = 1.8897261328856432, ! a.u. to Angst
   nat= %d,
   ntyp= 2,
   occupations = 'smearing',
   smearing = 'gauss',
   degauss = 1.0d-8
   ecutwfc = %.1lf,
   ecutrho = %.1lf,
   nosym = .true.,
/
""" % (len(lattice), ecutwfc, ecutrho)

    ELECTRONS="""&ELECTRONS
   electron_maxstep = 100,
   conv_thr = 1.0d-9,
   mixing_mode = 'plain',
   mixing_beta = 0.5d0,
   mixing_ndim = 8,
   diagonalization = 'david',
/
&IONS
   ion_dynamics='bfgs',
/
"""

    if Apply_E_Field != None:
        CONTROL = CONTROL.split('\n/')[0] + "\n   tefield = .true.\n   dipfield = .true.\n/\n"
        SYSTEM = SYSTEM.split('\n/')[0] + """
   edir = 3,
   eamp = %lf,
   emaxpos=0.99,
   eopreg=0.01,
/
""" % (Apply_E_Field)

    if kpts[0]<0:
        kpts=get_k(lattice)

    K_POINTS="""K_POINTS {automatic}
 %d %d %d 0 0 0
""" % (kpts[0],kpts[1],kpts[2])

    at_pos, at_cell=get_at_pos_tag(lattice, is_ibrav0=True,cell_unit='alat= 1.88972613')

    return CONTROL + SYSTEM + ELECTRONS + ATOMIC_SPECIES + at_pos + K_POINTS + at_cell
