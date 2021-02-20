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
while True:
    name = input('Наименование товара:')
    if name.isalnum():
        break
    if not(name.isalnum()):
        name = input('Наименование товара:')
        
try:
    quantity = int(input('Количество:'))
except(ValueError):
    quantity = int(input('Количество:'))
    
while True:
    surname = input('Фамилия получателя:')
    if surname.isalpha():
        break
    if not(surname.isalpha()):
        surname = input('Фамилия получателя:')
        
while True:
    try:
        phone = int(input('Контактный телефон (10 цифр):'))
        a = str(phone)
        if len(a) == 10:
            break
        if len(a) < 10 and len(a) > 10:
            phone = int(input('Контактный телефон (10 цифр):'))
    except(ValueError):
        print('Not a number')
        
print('Адрес')
while True:
    try:
        index = int(input('Индекс (6 цифр):'))
        b = str(index)
        if len(b) == 6:
            break
        if len(b) < 6 and len(b) > 6:
            index = int(input('Индекс (6 цифр):'))
    except(ValueError):
        print('Not a number')
        
while True:
    city = input('Город:')
    if city.isalpha():
        break
    if not(city.isalpha()):
        city = input('Город:')
        
while True:
    street = input('Улица:')
    if street.isalpha():
        break
    else:
        street = input('Улица:')

while True:
    try:
        haus = int(input('Номер дома:'))
        break
    except(ValueError):
        print('Not a number')
        
while True:
    try:
        kw = int(input('Квартира:'))
        break
    except(ValueError):
        print('Not a number')
        
print('\nВаш заказ принят')
print(f'Наименование товара: {name}')
print(f'Количество: {quantity}')
print(f'Фамилия покупателя: {surname}')
print(f'Контактный телефон: {phone}')
print(f'Адрес:{index}, город {city}, улица {street}, дом {haus}, квартира {kw}')
