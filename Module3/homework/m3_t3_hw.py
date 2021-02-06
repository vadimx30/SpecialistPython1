"""
Дана последовательность символов, не более 9 символов,имеющая следующий вид:
p1*p2*p3*....*pn, где pi - цифра. Вычислите значение выражения.
Пример:
In: 5*3*2
Out: 30
"""

string = [i for i in input('Enter string: ').split('*')]
mn = 1
for mel in string:
    mn = mn*int(mel) #Нет проверки что произойдет ошибка
print('Result = ',mn)
