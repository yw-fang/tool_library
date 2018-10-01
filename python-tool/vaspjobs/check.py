# -*- coding: utf-8 -*-
import os

directory = "./Materials/"
name = "OUTCAR"
running = "RUNNING"
find = "switches"
for filename in os.listdir(directory):
    if os.path.isdir(directory + filename):
        for root, dirs, files in os.walk(directory + filename):
            if "RUNNING" in files:
                print(root + " RUNNING")
                break
            if name in files:
                path = os.path.join(root, name)
                path = path.replace("(", "\(")
                path = path.replace(")", "\)")
                output = os.popen("tail " + path).read()
                if output.find(find) < 0:
                    new_root = root.replace("(", "\(")
                    new_root = new_root.replace(")", "\)")
                    print(root + " unfinished")
#                    print("resubmitting...")
#                    print(os.popen("cd " + new_root +
#                                   ";vasp_update.pl;qsub job.sh;cd ../.."
#                                   ).read())
                break

            else:
                new_root = root.replace("(", "\(")
                new_root = new_root.replace(")", "\)")
                print("no " + name + " in " + root + " unsubmitted")
                # print(os.popen("cd " + new_root +
                #                ";qsub job.sh;cd ../..").read())
                break
