import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from pandas import DataFrame

"""
__Author__: Yue-Wen FANG
__Date__: 2018 July 14th
"""

mpl.style.use('classic')
mpl.rcParams['figure.facecolor'] = '1'
# if choose the grey backgroud, use 0.75
mpl.rcParams['figure.figsize'] = [9, 6]
mpl.rcParams['lines.linewidth'] = 2.2
mpl.rcParams['legend.fancybox'] = True
mpl.rcParams['legend.fontsize'] = 19
mpl.rcParams['legend.scatterpoints'] = 1  # scatterpoints,
# it's the numer of maker points in the legend when
# creating a legend entry for a scatter plot
mpl.rcParams["axes.formatter.useoffset"] = False
# turn off the axis offset-values.
# If on. the axis label will use a offset value by the side of axis
mpl.rcParams["axes.linewidth"] = 1.5  # change the boarder width
# plt.rcParams["axes.edgecolor"] = "0.15"  # change the boarder color

ticklabel_size = 19
mpl.rcParams['xtick.labelsize'] = ticklabel_size
mpl.rcParams['ytick.labelsize'] = ticklabel_size


data = pd.read_csv('./Pmmm-P4mmm-allmode.dat', names=['Energy'])
df1 = data[1::2]  # only the energy data was kept
df2 = df1.sort_index(axis=0, ascending=False)
df2_remove_maximum = df2.drop([21])
df = df1.append(df2_remove_maximum)
array1 = np.linspace(-1, 1, 21)
round_array1 = array1.round(decimals=1)  # decimals is important for floatings
lambda_list = round_array1.tolist()
df['lambda'] = lambda_list
# df.reset_index(drop=True)  # drop the original index
df.set_index('lambda', inplace=True)  # use lambda column as new index
df['Energy_meV'] = (df['Energy'] + 59.40780538)*1000
# print(df)

fig = plt.figure()  # Create matplotlib figure

ax = fig.add_subplot(111)  # Create matplotlib axes
# ax2 = ax.twinx()  # Create another axes that shares the same x-axis as ax.

df.Energy_meV.plot(ax=ax, color={'r'}, alpha=0.9,
                   kind='line', marker='o', markersize=12,
                   mark_right=False,
                   label="Energy profile")
# df.BaOP4mm.plot(ax=ax,color={'b'},alpha=0.9,
#                 kind='line', marker='o',markersize=12,mark_right=False,
#                 label='Ba-O')
# ax.legend(loc="upper center")
# df.caratio.plot(ax=ax2,color={'b'}, alpha=0.9, kind='line', marker='s',
#                 markersize=10,mark_right=False, label='$\Gamma$')
# ax.legend(loc="best")

ax.set_xlabel(r'Nomalized displacement $\lambda$', fontsize=20)
ax.set_ylabel(r'$E$ (meV/10-atom)', fontsize=20)
# ax2.set_ylabel('c/a', fontsize=20)

# ax.annotate('', (1.1, 179), (5, 179),
#             arrowprops=dict(facecolor='r', shrink=0.1))
# arrowstyle="<-" ax.annotate('', (10, 174), (6, 174),
# arrowprops=dict(facecolor='b',shrink=0.1)) # arrowstyle="<-"
# ax.annotate('', (9.8, 0.065), (9.1, 0.065),
# arrowprops=dict(facecolor='g',shrink=0.1)) # arrowstyle="<-"
#    plt.xticks(np.arange(0, 13, 2))
plt.tight_layout()
ax.grid()

# plt.show()
plt.savefig('Pmmm-P4mmm-allmode.pdf')
