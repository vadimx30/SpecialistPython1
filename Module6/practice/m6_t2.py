"""
Написать программу, которая находит все файлы заданного расширения и
переносит их в подпапку backup, которую нужно создать.
"""


import glob
import shutil

def backupf(dirf,ex):
    os.chdir(dirf)
    path = os.path.join(dirf,'backup')
    if not os.path.exists(path):
        os.mkdir(path)
    for f in glob.glob('*.'+ex):
        newp = os.path.join(path,f)
        shutil.copyfile(f,newp)
# 

backupf(os.getcwd(),'py')
