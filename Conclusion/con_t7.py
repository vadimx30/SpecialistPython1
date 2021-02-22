""" 7. В банкомате есть купюры 5000, 2000, 1000, 500, 100 рублей.
    Количество купюр каждого номинала ограничено.
    Каждый кортеж в списке - это номинал и количество.
    Напишите функцию, которая будет рассчитывать количество купюр,
    которыми можно будет выдать запрошенную пользователем сумму и
    возвращать ее в виде словаря, ключами в котором будут номиналы банкнот.
    Если пользователь запросил некорректную сумму(больше, чем можно выдать,
    нужно вывести дружественное сообщение об ошибке.
    Результат работы функции вывести на экран(номинал и количество купюр)
"""
def calc_banknotes(amount, bank):
    result = {}
    a = 0
    if amount // 5000:
        if (amount // 5000) > bank[5000]:
            a = bank[5000]
        else:
            a = amount // 5000
        result[5000] = a
        amount -= (a * 5000)
    if amount // 2000:
        if (amount // 2000) > bank[2000]:
            a = bank[2000]
        else:
            a = amount // 2000
        result[2000] = a
        amount -= (a * 2000)
    if amount // 1000:
        if (amount // 1000) > bank[1000]:
            a = bank[1000]
        else:
            a = amount // 1000
        result[1000] = a
        amount -= (a * 1000)
    if amount // 500:
        if (amount // 500) > bank[500]:
            a = bank[500]
        else:
            a = amount // 500
        result[500] = a
        amount -= (a * 500)
    if amount // 100:
        if (amount // 100) > bank[100]:
            a = bank[100]
        else:
            a = amount // 100
        result[100] = a
        amount -= (a * 100)
    if amount > 0:
        result = []
    return result

nominals = ((5000, 5), (2000, 10), (1000, 15), (500, 20), (100, 50))
bankomat = dict(nominals)
a = int(input('Сколько хотите снять: '))
while a % 100:
    print('Введите сумму кратную 100')
    a = int(input('Сколько хотите снять: '))
if calc_banknotes(a, bankomat):
    print(f'Выдача банкнот: {calc_banknotes(a, bankomat)}')
else:
    print('Недостаточно средств')
