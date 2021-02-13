"""
Написать программу, которая находит все файлы заданного расширения и
переносит их в подпапку backup, которую нужно создать.
"""

import os
import glob
import shutil
import sys


ext = input('Введите расширение файла: ')
ext = '*.' + ext
files = glob.glob(ext)

if not files:
    print('Файлов с таким расширением нет')
    sys.exit()
if not os.path.exists('backup'):
    os.makedirs('backup')
for i in files:
    shutil.copy(i, "backup")
    os.remove(i)
