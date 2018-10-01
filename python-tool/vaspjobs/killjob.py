# -*- coding: utf-8 -*-
import os

__author__ = "Yue-Wen FANG"
__maintainer__ = "Yue-Wen FANG"
__email__ = "fyuewen@gmail.com"
__status__ = "Development"
__creation_date__ = "October 1, 2018"

"""
This script is used for killing jobs.
You can kill all the jobs of a user ('ywfang' is the username by default), 
or you can just kill some jobs with their job IDs in a range.

Pop menu when excuting it, delete all or just some jobs?
"""

for line in os.popen("squeue --user=ywfang").readlines():
    id_num = line.split()[0].strip()   # id_num is str
    if id_num.isdigit():
        os.popen("qdel "+id_num)
    print(id_num, 'was killed')
