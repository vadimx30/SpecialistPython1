"""
Написать программу, которая находит все файлы заданного расширения и
переносит их в подпапку backup, которую нужно создать.
"""
import os
import glob
import shutil

os.mkdir('backup')
ras = input('Введите раширение: ')
# print(ras)
from pprint import pprint
a = glob.glob(f'*{ras}')
# print(a)
for i in a:
    print(f'{os.path.getsize(i)} КБ')
    shutil.copy("{i}", "backup") //?????
