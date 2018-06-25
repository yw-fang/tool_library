import ase.io.vasp as aiv
cell = aiv.read_vasp("POSCAR.vasp")
aiv.write_vasp("POSCAR.222.ase", cell*(1,2,1), label='222supercell',
               direct=True,
               sort=True
               )
