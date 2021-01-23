a = int(input('расстояние в км: '))
b = int(input('расход в литрах: '))
c = 48
r = float(b*a/100)
s = round(r*c, 2)
print('Стоимость: ', s, 'рубля ')
