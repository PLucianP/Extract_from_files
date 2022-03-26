# The program is writting in a txt file all spotdata and max gun force data
import os
from datetime import datetime

orig_dir = os.getcwd()

# Change the directory to the oldest folder where the backups are stored in
os.chdir("d:\Bremen_N293 (Mandorf)\Backups\TVHR\\")
path = os.getcwd()
folders = os.listdir(path)
latest_file = max(folders, key=os.path.getctime)
os.chdir("{}\{}".format(path, latest_file))

now = datetime.now()
date = now.strftime("%Y%m%d")
myfile = open(os.path.join(orig_dir, "Spot data {}_{}.txt".format(path.split('\\')[-1], date)), "w")

for root, dirs, files in os.walk('.', topdown=True):
    for file in files:
        if file.endswith('MVT.mod') or file.endswith('MOC.cfg'):
            path = os.path.join(root,file)
            f = open(path,'r')
            f1 = f.readlines()
            exists = 0
            for line in f1:
                if ' PERS spotdata' in line:
                    if exists == 0:
                        myfile.write(root.split('\\')[1].split('_')[2] + "\n")
                        exists += 1
                    if '!' not in line:
                        myfile.write(line)
                elif '-max_gun_force' in line:
                    myfile.write(line.split()[2:4][0] + " " + line.split()[2:4][1] + "\n\n") 
            f.close
myfile.close()