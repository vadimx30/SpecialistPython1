"""
Написать программу для подсчета размера всех .py файлов в текущей папке.
"""

def FindPytonFiles(dir):
    os.chdir(dir) 
    c,s = 0,0        
    for f in glob.glob('*.py'):
       s = s + os.path.getsize(f)
       c += 1
    print(f'in {dir} find {c} files. Total {s} Bytes')
        
FindPytonFiles(os.getcwd())
