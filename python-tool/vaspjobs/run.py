import os

path = os.getcwd()
for root, dirs, files in os.walk("Ex"):
    if ("intermediate" not in root) and (root != "Ex"):
        updated = False
        items = os.scandir(root)
        for each in items:
            if each.name == 'intermediate':
                updated = True
                break
        if updated:
            os.chdir(root)
            os.popen("qsub job.sh")
            os.chdir(path)
        if not updated:
            print(root)
