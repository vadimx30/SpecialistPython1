"""
Написать программу для подсчета размера всех .py файлов в текущей папке.
"""

import os
import glob

files = glob.glob('*.py')
print(files, type(files))
summ = 0
for i in files:
    summ += os.path.getsize(i)
    
print(f' В текущей папке {len(files)} файлов,'
      f'общим объемом {summ//1024}Кб')
