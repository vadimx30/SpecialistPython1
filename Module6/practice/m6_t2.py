"""
Написать программу, которая находит все файлы заданного расширения и
переносит их в подпапку backup, которую нужно создать.
"""

import os
import glob
import shutil
import sys
rash = input('Введите расширение файла: ')
rash = '*.' + rash
a = glob.glob(rash)
if not a:
    print('файлов с таким расширением нет')
    sys.exit()
if not os.path.exists('backup'):
    os.makedirs('backup')
for i in a:
    shutil.copy(i, "backup")
    os.remove(i)
print('All done')
