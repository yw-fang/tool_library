# -*- coding: utf-8 -*-
import ase.io.vasp as aiv

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "September 3, 2018"

cell = aiv.read_vasp("POSCAR.vasp")
aiv.write_vasp("POSCAR.222.ase", cell*(1, 2, 1), label='222supercell',
               direct=True,
               sort=True
               )
