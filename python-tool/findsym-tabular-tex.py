import numpy as np
import pandas as pd



def data_load(filename):
    data = None
    with open(filename) as f:
        data = pd.read_csv(f, delim_whitespace=True, skiprows=36)
    return data

file='2-Cm-findsym.cif'
data = data_load(file)
print(data)
