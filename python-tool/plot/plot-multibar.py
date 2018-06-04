import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#import pdf module
from matplotlib.backends.backend_pdf import PdfPages

fig1 = plt.figure()
ax1_1=fig1.add_subplot(1,1,1)

a0=pd.read_csv('./Kappa-pbe-pbesol-exp-comparison.csv', delim_whitespace=True)
a0.sort_values('pbe', inplace=True)
a0 = a0[a0.material != 'AlN']
a0 = a0[a0.material != 'BeSe']
a0 = a0[a0.material != 'ZnTe']

a1=a0.copy()


#a1.plot(x="material", y = ['pbe_error','pbesol_error'], kind='bar', label=['a','b'])
# ax1.plot(a1['material'],a1['pbe_error'],kind='bar', label = '${U=0}$ eV',alpha=1)

ax1_1.bar(a1['material'],a1['pbe_error'], label = 'PBE', width=0.2, color='green', alpha=0.6)
ax1_1.bar(a1['material'],a1['pbesol_error'], label = 'PBESol', width=0.2, color='black', alpha=0.6)
