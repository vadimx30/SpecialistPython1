'''
Задача №2. Шахматная доска
Вход: размер шахматной доски, от 0 до 20
Выход: вывести на экран эту доску, заполняя поля нулями и единицами

Пример:
Вход: 4
Выход:
    0 1 0 1
    1 0 1 0
    0 1 0 1
    1 0 1 0
'''

def main():
    z = input('Размер шахматной доски (от 0 до 20): ')
    while z.isdigit() == False or (int(z) > -1) == False or (int(z) < 21) == False:
        z = input('Размер шахматной доски (от 0 до 20): ')  
    z = int(z)
    
    result = {}
    line_even = []
    line_odd = []
    
    for i in range(z):
        if i % 2:
            line_even.append(0)
            line_odd.append(1)
        else:
            line_even.append(1)
            line_odd.append(0)
   
    for i in range(z):
        if i % 2:
            result[i+1] = line_even
        else:
            result[i+1] = line_odd
    
    for value in result.values():
        print(*value)
  
  
if __name__ == '__main__':
    main()
