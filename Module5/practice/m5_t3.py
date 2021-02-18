Задача №3
Вход: размер шахматной доски, от 0 до 20
Выход: вывести на экран эту доску с названиями полей.
Пример:
In: 4
Out:
a4 b4 c4 d4
a3 b3 c3 d3
a2 b2 c2 d2
a1 b1 c1 d1

import string as st

def main():
    z = input('Размер шахматной доски (от 0 до 20): ')
    while not z.isdigit() or not (int(z) > -1) or not (int(z) < 21):
        z = input('Размер шахматной доски (от 0 до 20): ')  
    z = int(z)
 
    result = {}
    columns = list(st.ascii_lowercase[:z])
    lines = [(i + 1) for i in range(z)]
  
    lines.reverse()




    result = {x: columns.copy() for x in lines}
    
    for key, value in result.items():
        for i in range(z):
             value[i] += str(key)

    for key, value in result.items():
        if int(key) > 9:
            print(" ".join(value))
        else:
            print("  ".join(value))

    
if __name__ == '__main__':
    main()  
