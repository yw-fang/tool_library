#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Author] Yue-Wen Fang [Email] fyuewen@gmail.com
#          Description
#   [usage] ./plot-degauss-convergence.py, this will save a plot as a pdf in the current directory
# [Purpose] Plot the energy in Ry as a function of degauss values. This is a convergence examination for QE.
#          History
#  HISTORY
#     2022/September/28 : Script creation
# ------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots(1,1)

# read the data
df = pd.read_csv('convergence.dat', sep='\s+', header=None, names=['degauss', 'energy'])
print(df)
print(type(df))
df.sort_values(by='degauss', inplace=True)
# plot the dataframe df in ax
# ax.plot(df['degauss'], df['energy'], 'o-')
df.plot(x='degauss', y='energy', ax=ax, marker='o', linestyle='-', color='b')
# set the x and y labels
ax.set_xlabel('Degauss')
ax.set_ylabel('Energy (Ry)')
# set the x and y limits
plt.xlim(0, 0.1)
# set the x and y ticks
# plt.xticks([0, 0.02, 0.04, 0.06, 0.08, 0.1])
plt.yticks([])
# set the x and y grid
plt.grid(True, which='both')
# save the figure
fig.savefig('convergence.pdf', dpi=72)
