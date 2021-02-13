"""
Написать программу для подсчета размера всех .py файлов в текущей папке.
"""

import os
import glob
a = glob.glob('*.py')
b = 0
summ = 0
for i in a:
    b = os.path.getsize(i)
    summ += os.path.getsize(i)
    print(f'File: {i} - {b} bytes')
print(f'AllFile: {summ} bytes')

