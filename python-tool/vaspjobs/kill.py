import os

for line in os.popen("squeue --user=ywfang").readlines():
    id_num = line.split()[0].strip()
    if id_num.isdigit():
        os.popen("qdel "+id_num)
    print(id_num)