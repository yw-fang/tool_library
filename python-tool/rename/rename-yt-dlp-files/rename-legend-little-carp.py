#!/usr/bin/env python3
import glob, os
for filename in glob.glob('*.mp4'):
    print(filename)
    first = filename.split('.')
    print(first)
    second = first[0].split(' ')
    print(second)
    third = '小鲤鱼历险记-'+second[1]+'-'+second[2]+'.mp4'
    print(third)
    os.rename(filename, third)
