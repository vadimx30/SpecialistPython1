# Задача №2
# Среди заданных чисел a, b, c, d, e найти
# количество положительных и количество отрицательных чисел

a = int(input('Введите целое число "а": '))
b = int(input('Введите целое число "b": '))
c = int(input('Введите целое число "c": '))
d = int(input('Введите целое число "d": '))
pos = 0
neg = 0
zero = 0

if a > 0:
    pos += 1
elif a < 0:
    neg += 1
else:
    zero += 1

if b > 0:
    pos += 1
elif b < 0:
    neg += 1
else:
    zero += 1

if c > 0:
    pos += 1
elif c < 0:
    neg += 1
else:
    zero += 1

if d > 0:
    pos += 1
elif d < 0:
    neg += 1
else:
    zero += 1

print('Количество положительных чисел:', pos)
print('Количество отрицательных чисел:', neg)
print('Количество чисел, равных нулю:', zero)
