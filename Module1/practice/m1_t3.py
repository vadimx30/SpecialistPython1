a = int(input('Введите число:'))
numbone = a // 1000

b = a % 1000
numbtwo = b//100

c = a % 100
numbthree = c//10

numbfour = a % 10
print('Первое чило:', numbone, 'Второе число:', numbtwo, 'Третье число:', numbthree, 'Четвертое число:', numbfour)
