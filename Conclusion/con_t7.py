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
nominals = ((5000, 5), (2000, 10), (1000, 15), (500, 20), (100, 50))
bankomat = dict(nominals)

def calc_banknotes(amount):
    # ваш код здесь
    return {}


assert total_sum == sum([banknote * count for banknote, count in nominals])




nominals = ((5000, 5), (2000, 10), (1000, 15), (500, 20), (100, 50))
bankomat = dict(nominals)
def calc_banknotes(amount):
    # ваш код здесь
    vost = {}
    ost = amount
    for kup,kol in bankomat.items():
        osttek = int(ost/kup)
        if kol < osttek:
            osttek = kol
        if osttek>0:
            ost -= osttek*kup
            bankomat.update({kup:kol-osttek})
            vost.update({kup:osttek})
    try:
        vsego = sum([banknote * count for banknote, count in vost.items()])
        assert amount == vsego
    except:
        return(f'no such nominals. Vsego: {vsego}')
    return vost

print(calc_banknotes(6500))
