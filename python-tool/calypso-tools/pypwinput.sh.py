from pymatgen.core.structure import Structure
from pymatgen.io.vasp.sets import MITRelaxSet
from ase.io import read
from ase.build import sort
from ase.calculators.espresso import Espresso

def pwscf_to_poscar(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Extract lattice vectors and atom positions
    lattice_vectors = []
    atomic_positions = []
    element_counts = {}

    for line in lines:
        if "CELL_PARAMETERS" in line:
            for i in range(3):
                lattice_vectors.append(lines[lines.index(line) + i + 1].split())
        elif "ATOMIC_POSITIONS" in line:
            position_type = line.split()[1]
            for i in range(lines.index(line) + 1, len(lines)):
                if not lines[i].strip():
                    break
                atomic_positions.append(lines[i].split())
                element = atomic_positions[-1][0]
                element_counts[element] = element_counts.get(element, 0) + 1

    # Write the POSCAR file
    with open(output_file, 'w') as f:
        f.write("RbH{}\n".format(sum(element_counts.values())))
        f.write("1.0\n")
        for vector in lattice_vectors:
            f.write(" ".join(vector) + "\n")

        # f.write("Rb H\n")
        for element, count in element_counts.items():
            f.write("{} ".format(element))
        f.write("\n")
        for count in element_counts.values():
            f.write("{} ".format(count))
        f.write("\nDirect\n")

        for position in atomic_positions:
            f.write(" ".join(position[1:]) + "\n")


def gen_kpoints(file, kppvol):
    # use pymatgen to generate kpoints
    structure = Structure.from_file(file)
    mitparamset = MITRelaxSet(structure)
    kpoints = mitparamset.kpoints.automatic_density_by_vol(structure, kppvol)
    kpoints.write_file('KPOINTS')


# write a function to write a pwscf.in using ase
def gen_input():
    from ase.io import read

    # Read the POSCAR file
    structure = read('POSCAR')

    # Create the pw.x input file content
    pwscf_in = """&control
        calculation = 'vc-relax',
        prefix = 'RbH12',
        pseudo_dir = '/public5/home/sch8008/ywfang/vaspwork/RbH/RbH12/50GPa/pot',
        outdir = './',
        tprnfor = .true.,
        tstress = .true.,
        etot_conv_thr = 1.0e-5,
        forc_conv_thr = 1.0e-3,
     /
     &system
        ibrav = 0,
        nat = {natoms},
        ntyp = {ntypes},
        ecutwfc = 50.0,  ! Set your own value
        ecutrho = 400.0,  ! Set your own value
        occupations = 'smearing',
        degauss = 0.05,
     /
     &electrons
        conv_thr = 1.0e-7,
        mixing_beta = 0.5,
     /
     &ions
        ion_dynamics = 'bfgs',
     /
     &cell
        cell_dynamics = 'bfgs',
        press = 500,
     /
    ATOMIC_SPECIES
    H      1.00794 H.upf
    Rb     85.4678 Rb.upf
    """

    # Extract information from the structure
    natoms = len(structure)
    ntypes = len(set(structure.get_chemical_symbols()))
    species = []
    positions = []
    for symbol in set(structure.get_chemical_symbols()):
        species.append(f"{symbol}  1.0  /path/to/pseudopotential/{symbol}.pseudo.UPF")
#    for atom in structure:
#        positions.append(f"{atom.symbol}  {atom.scaled_position[0]:.6f}  {atom.scaled_position[1]:.6f}  {atom.scaled_position[2]:.6f}")

    # You may need to set the k-points based on your system
#    kpoints = "2 2 2 0 0 0"

    # Fill in the placeholders in the input file content
    pwscf_in = pwscf_in.format(natoms=natoms, ntypes=ntypes)

    # Write the input file
    with open('pwscf.in', 'w') as f:
        f.write(pwscf_in)

    print("PWSCF input file 'pwscf.in' created for relaxation.")

    # call bash shell command 'cat' to append pwscf_$i into pwscf.in
    import subprocess
    # use sed to print all contents in pwscf_1 to pwscf.in
    subprocess.call("sed -n '1,$p' pwscf_1 >> pwscf.in", shell=True)
    # print "K_POINTS automatic" into pwscf.in
    subprocess.call("echo 'K_POINTS automatic' >> pwscf.in", shell=True)
    # extract kgrid from the fourth line in KPOINTS and print it to pwscf.in with '0 0 0', for example, if you get 3 3 4 from KPOINTS, print 3 3 4 0 0 0 to pwscf.in
    subprocess.call("sed -n '4p' KPOINTS | awk '{print $1,$2,$3,0,0,0}' >> pwscf.in", shell=True)


if __name__ == "__main__":
    pwscf_to_poscar("pwscf_1", "POSCAR")
    kppvol=100
    gen_kpoints("POSCAR", kppvol)
    gen_input()
