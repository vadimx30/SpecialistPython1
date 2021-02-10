"""
Написать функцию и оформить решение в виде модуля.
Входные аргументы функции: количество бутылок от 0 до 200.
Функция должна вернуть количество и слово бутылк<?> с правильным окончанием.
Пример :
In: 5
Out: 5 бутылок
    
In: 1
Out: 1 бутылка
    
In: 22
Out: 22 бутылки
"""

def bottles_ending(z: int) -> str:
    '''корректно склоняет слово "бутылка"'''
    ka = 0
    ki = 0
    ok = 0
        
    if (z % 100) > 10 and (z % 100) < 16:
        ok = 1
    else:    
        if (z % 10) == 1:
            ka = 1
        elif (z % 10) == 2 or (z % 10) == 3 or (z % 10) == 4:
            ki = 1
        else:
            ok = 1
        
    ending = {"ка": ka, "ки": ki, "ок": ok}
    for key, value in ending.items():
        if value:
            return key


def main():
    z = input('Введите количество бутылок (от 0 до 200): ')
    while z.isdigit() == False or (int(z) > -1) == False or (int(z) < 201) == False:
        z = input('Введите количество бутылок (от 0 до 200): ')  
    z = int(z)   
    
    print(f'{z} бутыл{bottles_ending(z)}')

            
if __name__ == '__main__':
    main()
