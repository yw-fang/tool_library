import cellconstructor as CC
import cellconstructor.Phonons
dyn = CC.Phonons.Phonons("dyn") #if you have dyn1, then just put dyn between " "
structure=dyn.structure
print(structure.unit_cell)
print(structure.coords)
structure.save_scf('scf.in')
