structure = StructureData(cell=cell)
for i, scaled_position in enumerate(scaled_positions):
    structure.append_atom(position=np.dot(scaled_position, cell).tolist(),
                          symbols=symbols[i])


# Machine
machine_dict = {'resources': {'num_machines': 1,
                              'parallel_env': 'mpi*',
                              'tot_num_mpiprocs': 16},
                'max_wallclock_seconds': 3600 * 10,
                }


# PHONOPY settings
ph_settings = ParameterData(dict={'supercell': [[2, 0, 0],
                                                [0, 2, 0],
                                                [0, 0, 2]],
                                  'primitive': [[0.0, 0.5, 0.5],
                                                [0.5, 0.0, 0.5],
                                                [0.5, 0.5, 0.0]],
                                  'distance': 0.01,
                                  'mesh': [20, 20, 20],
                                  'symmetry_precision': 1e-5,
                                  'code': {'fc2': 'phonopy@boston-lab',  # this uses phonopy.phonopy
                                           'fc3': 'phono3py@boston-lab'},  # this uses phonopy.phono3py
                                  'machine': machine_dict
                                  })

code_to_use = 'VASP'
#code_to_use = 'QE'
#code_to_use = 'LAMMPS'

# VASP SPECIFIC
if code_to_use == 'VASP':
    incar_dict = {
        'NELMIN' : 5,
        'NELM'   : 100,
        'ENCUT'  : 400,
        'ALGO'   : 38,
        'ISMEAR' : 0,
        'SIGMA'  : 0.01,
        'GGA'    : 'PS'
    }

    settings_dict = {'code': {'optimize': 'vasp.boston@boston-lab',
                              'forces': 'vasp.boston@boston-lab',
                              'born_charges': 'vasp.boston@boston-lab'},
                     'parameters': incar_dict,
                     # 'kpoints_density': 0.5,  # k-point density (higher priority)
                     'kpoints_mesh': [2, 2, 2],  # k-point mesh (gamma centered)
                     #'kpoints_offset': [0.5, 0.5, 0.5],  # k-point offset
                     'pseudos_family': 'pbe_test_family',
                     'family_folder': '/home/ywfang/FANG/study/software/vasp-sourcecode/v54pot/aiida-pbe',
                     'machine': machine_dict
                     }

    # pseudos = ParameterData(dict=potcar.as_dict())
    es_settings = ParameterData(dict=settings_dict)


# QE SPECIFIC
if code_to_use == 'QE':
    parameters_dict = {
        'SYSTEM': {'ecutwfc': 30.,
                   'ecutrho': 200.,},
        'ELECTRONS': {'conv_thr': 1.e-6,}
    }

    settings_dict = {'code': {'optimize': 'pw6@boston-lab',
                              'forces': 'pw6@boston-lab'},
                     'parameters': parameters_dict,
                     'kpoints_density': 0.5,  # k-point density
                     'pseudos_family': 'pbe_test_family',
                     'machine': machine_dict
                     }

    es_settings = ParameterData(dict=settings_dict)


# LAMMPS SPECIFIC
if code_to_use == 'LAMMPS':
    # Silicon(C) Tersoff
    tersoff_si = {'Si  Si  Si ': '3.0 1.0 1.7322 1.0039e5 16.218 -0.59826 0.78734 1.0999e-6  1.7322  471.18  2.85  0.15  2.4799  1830.8'}

    potential ={'pair_style': 'tersoff',
                'data': tersoff_si}

    parameters = {'relaxation': 'tri',  # iso/aniso/tri
                  'pressure': 0.0,  # kbars
                  'vmax': 0.000001,  # Angstrom^3
                  'energy_tolerance': 1.0e-25,  # eV
                  'force_tolerance': 1.0e-25,  # eV angstrom
                  'max_evaluations': 1000000,
                  'max_iterations': 500000}

    settings_dict = {'code': {'optimize': 'lammps_optimize@boston-lab',
                              'forces': 'lammps_force@boston-lab'},
                     'parameters': parameters,
                     'potential': potential,
                     'machine': machine_dict
                     }

    es_settings = ParameterData(dict=settings_dict)

ThermalPhono3py = WorkflowFactory('phonopy.thermal')

# Chose how to run the calculation
run_by_deamon = True
if not run_by_deamon:
    result = run(ThermalPhono3py,
            structure=structure,
            es_settings=es_settings,
            ph_settings=ph_settings,
            # Optional settings
            # pressure=Float(0), # Pressure at which the optimization takes place (no effect if optimize = False)
            optimize=Bool(True),
            use_nac=Bool(True),
            chunks=Int(120),  # set the number of maximum simultaneous calculations
            initial_cutoff=Float(4.0),  # Initial cutoff in Angstrom
            step=Float(1.0),  # Step cutoff in Angstrom
            gp_chunks=Int(1)  # Number of computers in distributed phono3py calculation
            )
    print (result)
else:
    future = submit(ThermalPhono3py,
            structure=structure,
            es_settings=es_settings,
            ph_settings=ph_settings,
            # Optional settings
            # pressure=Float(0),
            optimize=Bool(True),
            use_nac=Bool(True),
            chunks=Int(120),  # set the number of maximum simultaneous calculations
            initial_cutoff=Float(4.0),  # Initial cutoff in Angstrom
            step=Float(1.0),  # Step cutoff in Angstrom
            gp_chunks=Int(1)  # Number of computers in distributed phono3py calculation
            )
    print('Running workchain with pk={}'.format(future.pid))
