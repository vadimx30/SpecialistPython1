"""
Сформировать данные для отправки заказа из
магазина по накладной и записать в файл:
1) Наименование товара.
2) Количество
3) ФИО покупателя
4) Контактный телефон (10 цифр)
5) Адрес(индекс(ровно 6 цифр), город, улица, дом, квартира)

Эти данные не могут быть пустыми.
Проверить правильность заполнения полей, используя исключения.
"""

def pr1(a: str) -> str:
    b = ''
    try:
        1 / len(a)
        b = 'Принято'
    except ZeroDivisionError:
        b = 'Вы ничего не ввели'
    return b
def pr2(a: str) -> str:
    b = ''
    try:
        int(a)
        a = int(a)
        if a <= 0:
            raise Exception('Some exception')
        b = 'Принято'
    except ValueError:
        b = 'Количество должно быть целым числом.'
        return b
    except Exception:
        b = 'Количество должно быть целым числом.'
        return b
    else:
        return b
def pr3(a: list) -> str:
    b = ''
    c = []
    try:
        if len(a) < 2:
            raise Exception('Some exception')
        b = 'Принято'
    except Exception:
        b = 'Введено недостаточно данных'
        return b
    return b
def pr4(a: str, c: int) -> str:
    b = ''
    try:
        int(a)
        if len(a) != c or int(a) <= 0:
            raise Exception('Some exception')
        b = 'Принято'
    except ValueError:
        b = 'Недостаточно данных'
        return b
    except Exception:
        b = 'Недостаточно данных'
        return b
    return b
     
tovar = input('Введите наименование товара: ')
while pr1(tovar) == 'Вы ничего не ввели':
    print(pr1(tovar))
    tovar = input('Введите наименование товара: ')
kolvo = input('Введите количество товара: ')
while pr2(kolvo) == 'Количество должно быть целым числом.':
    print(pr2(kolvo))
    kolvo = input('Введите количество товара: ')
fio = [i for i in input('Введите ФИО полностью: ').split()]
while pr3(fio) == 'Введено недостаточно данных':
    print(pr3(fio))
    fio = [i for i in input('Введите ФИО полностью: ').split()]
tel = input('Введите номер телефона: ')
while pr1(tel) == 'Вы ничего не ввели' or pr4(tel, 10) == 'Недостаточно данных':
    print('Номер должен содержать 10 цифр без пробелов и скобок')
    tel = input('Введите номер телефона: ')
print('Принято')
print('Введите адрес')
ind = input('Введите индекс: ')
while pr1(ind) == 'Вы ничего не ввели' or pr4(ind, 6) == 'Недостаточно данных':
    print('Индекс должен содержать 6 цифр')
    ind = input('Введите индекс: ')
city = input('Введите город: ')
while pr1(city) == 'Вы ничего не ввели':
    print(pr1(city))
    city = input('Введите город: ')
street = input('Введите улицу: ')
while pr1(street) == 'Вы ничего не ввели':
    print(pr1(street))
    street = input('Введите улицу: ')
home = input('Введите номер дома: ')
while pr1(home) == 'Вы ничего не ввели':
    print(pr1(home))
    home = input('Введите номер дома: ')
kv = input('Введите номер квартиры: ')
while pr1(kv) == 'Вы ничего не ввели' or pr4(kv, len(kv)) == 'Недостаточно данных':
    print('Введены некорректные данные')
    kv = input('Введите номер квартиры: ')
print('Проверьте верность верность введенных данных:')
print(f' Наименование товара: {tovar}\n Количество: {kolvo}\n ФИО покупателя: ', *fio, f'\n Контактный телефон: {tel}\n Адрес: {ind}, {city}, {street}, {home}, {kv}')
result = input('Данные верны?: y/n ')
while result != 'y' or result != 'n':
    if result == 'y':
        print('Заказ принят')
        break
    elif result == 'n':
        print('Заказ отменен')
        break
    else:
        result = input('Данные верны?: y/n ')
