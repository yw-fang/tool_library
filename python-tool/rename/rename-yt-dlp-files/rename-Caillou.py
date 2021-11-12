#!/usr/bin/env python3
import glob, os
for filename in glob.glob('*.mp4'):
#    print(filename)
    first = filename.split('.')
#    print(first)
    second = first[0].split('_')
#    print(second[0])
#    print(second[1])
    third = second[0].split('-')
#    print(third[1])
    four = third[1].split(' ')
#    print(four)
    episode_number_w_bracket = four[-2]
    print(episode_number_w_bracket)
    # number_list = episode_number_w_bracket.split()
    number_list = [i for i in episode_number_w_bracket]
    episode_number = ''.join(number_list[1:-1])
#    print(number_list[1:-1])
    print(episode_number)
    episode_list = four[1:-3]
    episode_name = '-'.join(episode_list)
    print(episode_name)
    full_name_number = episode_name+'-'+episode_number+'.mp4'
    print(full_name_number)
    os.rename(filename, full_name_number)
    print("******")
