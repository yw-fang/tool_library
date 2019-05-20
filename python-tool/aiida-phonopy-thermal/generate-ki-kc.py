# import numpy as np
from numpy import absolute
import pandas as pd

ltc_mp149 = pd.read_csv('cutoff-ltc.csv',
                        header=None, delim_whitespace=True)

dataset2 = ltc_mp149[1].values
# print(dataset2)
# print('\n')
dataset2_nested = [dataset2[n:n+3] for n in range(len(dataset2)-2)]
# print(type(dataset2_nested))
for i in dataset2_nested:
    if absolute(absolute(i[0] - i[1])/i[1] - absolute(i[1] - i[2])/i[1]) <= 0.001:
#       print(i[1])
        list = ltc_mp149[1].tolist()
        convergence_index = list.index(i[1])
        convergence_cutoff = ltc_mp149[0][convergence_index]
        convergence_ltc = (ltc_mp149[1][convergence_index] + ltc_mp149[2][convergence_index]
                           + ltc_mp149[3][convergence_index])/3
#         print(convergence_index)
#        print(convergence_cutoff)
#        print(convergence_ltc)
        break

KL = ltc_mp149[1].iloc[-1]/3+ltc_mp149[2].iloc[-1]/3+ltc_mp149[3].iloc[-1]/3
print('K_convergence and K_0 are, ')
print(convergence_ltc)
print(KL)
