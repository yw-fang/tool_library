import os
import numpy as np

filename = "OUTCAR"
pwd = os.popen("pwd").read()
counter = 0
cat1, cat2, name = [], [], []
for root, dirs, files in os.walk("Materials"):
    if (root != "Materials") and ("intermediate" not in root) and ('(' not in root):
        data_list = []
        data = []
        path = os.path.join(pwd.strip(), root.strip(), filename)
        flag = False
        start = 0
        end = 0
        try:
            with open(path, 'r') as f:
                for line in f.readlines():
                    if "MACROSCOPIC STATIC DIELECTRIC TENSOR" in line:
                        if start > 0:
                            flag = True
                        else:
                            start += 1
                    if flag:
                        if "PIEZOELECTRIC TENSOR" in line:
                            if end > 0:
                                break
                            end += 1
                        line = line.strip()
                        data_list.append(" ".join(line.split()))
        except:
            print("fail: " + root)
            continue
        else:
            if not flag:
                print(path, "no tensor")
                continue
            for line in data_list:
                temp = []
                str_list = line.split(" ")
                for s in str_list:
                    try:
                        number = float(s)
                    except ValueError:
                        continue
                    else:
                        temp.append(number)
                if len(temp) > 0:
                    temp = np.asarray(temp)
                    data.append(temp)
            if len(data) != 6:
                print("warning!")
            matrix1 = np.asarray(data[:3]).flatten()
            matrix2 = np.asarray(data[3:]).flatten()
            if (matrix1[0] > 20) or (matrix1[3] > 20):
                print(root, matrix1)
            matrix1 = np.expand_dims(matrix1, 0)
            matrix2 = np.expand_dims(matrix2, 0)
            cat1.append(matrix1)
            cat2.append(matrix2)
            name.append(root.split("/")[-1].strip())
            counter += 1
#np.save("macro.npy", np.concatenate(cat1, 0))
#np.save("piezo.npy", np.concatenate(cat2, 0))
#np.save("name.npy", np.asarray(name))
print(counter)
