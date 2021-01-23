cost = float(48.0)
distance = float(input('Введите расстояние:'))
liters = float(input('Введите расход:'))
b = liters * cost
ck = b / 100
finalcost = distance * ck
print('Стоимость поездки:', finalcost)
