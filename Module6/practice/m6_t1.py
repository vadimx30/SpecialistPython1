"""
Написать программу для подсчета размера всех .py файлов в текущей папке.
"""

import os
a = os.listdir(os.curdir)
b = 0
for i in a:
    b += os.path.getsize(i)
print(f'{b} bytes')
