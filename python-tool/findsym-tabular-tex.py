import pandas as pd


def get_skiprows(filename):
    linenumber = 0
    with open(filename) as fn:
        for line in fn:
            if 'Ba1' in line:
                print(line)
                break
            else:
                linenumber = linenumber + 1
    return linenumber


def data_load(filename):
    header_names = ["atom_type", "element", "multiplicity", "Wyckoff_label", "x", "y", "z", "occupancy", "symmform"]
    data = None
    with open(filename) as f:
        data = pd.read_csv(f, delim_whitespace=True, skiprows=get_skiprows(filename), names = header_names)
    return data

file='2-Cm-findsym.cif'
data = data_load(file)
data['Wyckoff_label_multi'] = data['multiplicity'] + data['Wyckoff_label']
del data['Wyckoff_label']
del data['multiplicity']
del data['occupancy']
del data['symmform']
data = data.dropna()
print(data)

# linenumber = get_skiprows(file)
# print(linenumber)
