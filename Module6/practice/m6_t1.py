"""
Написать программу для подсчета размера всех .py файлов в текущей папке.
"""

import os
import glob

files = glob.glob('*.py')

summ = 0
count = 0
for i in files:
    summ += os.path.getsize(i)
    
for i in files:
    print(f'{count+1}){i}: {os.path.getsize(i)} байт')
    count += 1

print(f'В текущей папке {len(files)} файлов,'
      f'общим объемом {summ//1024}Кб')
