import os

"""
This script is used for killing jobs
You can kill all the jobs of a use, or
you can just kill some jobs with their job IDs in
a certain range.
"""

for line in os.popen("squeue --user=ywfang").readlines():
    id_num = line.split()[0].strip()   # id_num is str
    if id_num.isdigit():
        os.popen("qdel "+id_num)
    print(id_num, 'was killed')
