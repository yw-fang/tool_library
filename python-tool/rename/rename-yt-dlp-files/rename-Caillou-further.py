#!/usr/bin/env python3
import glob, os
for filename in glob.glob('*.mp4'):
#    print(filename)
    first = filename.split('.')
#    print(first)
    second = first[0].split('-')
    print(second)
    number_list = [i for i in second[-1]]
    print(number_list)
    episode_number = ''.join(number_list[-2:])
    print(episode_number)
    episode_name = '-'.join(second[:-1])
    print(episode_name)
    full_name_number = episode_number+'-'+episode_name+'.mp4'
    print(full_name_number)
    os.rename(filename, full_name_number)
