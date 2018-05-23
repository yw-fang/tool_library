import os
import fileinput

string_from_1 = "--partition=compute"
string_to_1 = "--partition=shared"
string_from_2 = "--ntasks-per-node=24"
string_to_2 = "--ntasks-per-node=12"
filename = "job.sh"
pwd = os.popen("pwd").read()
for root, dirs, files in os.walk("Materials"):
    if (root != "Materials") and ("intermediate" not in root):
        with fileinput.FileInput(
                os.path.join(pwd.strip(), root.strip(), filename),
                inplace=True,
                backup='.bak') as f:
            for line in f:
                print(line.replace(string_from_2, string_to_2), end='')
