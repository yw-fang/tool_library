import numpy as np
import pandas as pd

__author__ = 'Yue-Wen FANG'
__email__ = 'fyuewen@gmail'
##usage: python J_for_MPS3.py
##This script is used for extracting the Heisenberg exchange for MPS3 (such FePS3)

####Heisernberg equations references########
#ref1: https://pubs.rsc.org/en/content/articlehtml/2020/ra/c9ra09030d#cit47

data = pd.read_csv('./toten.dat', delim_whitespace=True)

S = np.average(data['moment'])

if 'meV-5atom' in data.columns:
    del data['meV-5atom']
else:
    pass
min_energy = data['eV-20atom'].min()
lowest_ordering = data['config'][data['eV-20atom']==min_energy]
print('lowest-E ordering is', lowest_ordering.values)

data['meV-5atom'] = (data['eV-20atom'] - min_energy)*1000/4
FM = data['meV-5atom'][0]
Neel = data['meV-5atom'][1]
Zigzag = data['meV-5atom'][2]
Stripy = data['meV-5atom'][3]

J1 = (FM - Neel + Zigzag - Stripy)/(8*S**2)
J2 = (FM + Neel - Zigzag - Stripy)/(16*S**2)
J3 = (FM - Neel - 3*Zigzag + 3*Stripy)/(24*S**2)

print("J1 = %.3f meV, J2 = %.3f meV, J3 = %.3f meV" % (J1, J2, J3))
