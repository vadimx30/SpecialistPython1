"""
Дана последовательность символов, не более 9 символов,имеющая следующий вид:
p1*p2*p3*....*pn, где pi - цифра. Вычислите значение выражения.
Пример:
In: 5*3*2
Out: 30
"""

a = [i for i in input('Введите последовательность типа a*b*c не более 9 символов')]
while len(a) >= 9:
    a = [i for i in input('Введите последовательность типа a*b*c не более 9 символов')]
nach = a.copy()
a.append('*')
b = ''
c = []
for i in range(len(a)):
    if a[i] != '*':
        b += a[i]
    else:
      c.append(b)
      b = ''
for k in range(len(c)):
    c[k] = int(c[k])
result = 1
for g in range(len(c)):
    result *= c[g]
print('Значение выражения', *nach, '=', result)
