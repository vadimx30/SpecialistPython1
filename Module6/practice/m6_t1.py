"""
Написать программу для подсчета размера всех .py файлов в текущей папке.
"""
import os
import glob
path = input ('Write path -> ')    
os.chdir(path)                            
dir_work = os.listdir(path)        
a = 1
b = 2
summ = 3
for file in glob.glob("*.txt"):
    print(file)
