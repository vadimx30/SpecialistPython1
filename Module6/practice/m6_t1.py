"""
Написать программу для подсчета размера всех .py файлов в текущей папке.
"""
import os
import glob

from pprint import pprint
a = glob.glob('*.py')
for i in a:
    print(f'{os.path.getsize(i)} КБ')
