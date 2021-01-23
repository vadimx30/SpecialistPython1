rast = int(input('Расстояние (50 - 10000 км): '))
rash = int(input('Расход (5-25 литров на 100 км): '))
Benz = 48
stoim = int(rast * rash / 100 * 48)
print('Cтоимость поездки в рублях :', stoim)
