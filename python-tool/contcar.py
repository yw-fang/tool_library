# update 2010.6.21
# update 2010.10.26
# update 2011.03.24
# update 2013.08.07
import re
def icontcar(caldir):
    contcar = []
    atom = False
    lat = False
    f = open(caldir + '/CONTCAR')
    for i in range(0, 2):
        line = f.readline()
        contcar.append(line)
    for i in range(2, 5):
        line = f.readline()
        tmp = line.split()
        if len(tmp) != 3:
            lat = True
        for item in tmp:
            try:
                llldot = float(item)
            except:
                lat = True
        contcar.append(line)
    line = f.readline()
    try:
        natom = sum(map(int, line.split()))
    except:
        line = f.readline()
        natom = sum(map(int, line.split()))
    contcar.append(line)
    line = f.readline()
    contcar.append(line)
    for i in range(0, natom):
        line = f.readline()
        if line.split()[-1] == 'F' or line.split()[-1] == 'T':
            if len(line.split()) != 6:
                line = '0.1   0.1   0.1 \n'
                atom = True
            else:
                line = line.replace('T', '').replace('F', '')
        else:
            if len(line.split()) != 3:
                line = '0.1   0.1   0.1 \n'
                atom = True
        linetmp1 = line.split()
        linetmp = map(float, linetmp1[:3])
        for j in range(0, 3):
            if linetmp[j] < 0.:
                linetmp[j] += 1.
                line = str(linetmp[0])+' '+str(linetmp[1])+' '+str(linetmp[2])+'\n'
        contcar.append(line)
    f.close()
    if lat == True:
        for i in range(2, 5):
            contcar[i] = '1.0   1.0   1.0 \n'
    #if atom == True or lat == True:
    ff = open(caldir + '/CONTCAR', 'w')
    for i in range(0, len(contcar)):
        ff.write(contcar[i])
    ff.close()
if __name__ == '__main__':
    icontcar('./')
