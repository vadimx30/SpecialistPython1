#Задача 1
a = int(input('Введите трехзначное число: '))
b = round(a//100)
c = round(a - a//10*10)
d = (a - b*100 - c)//10
print('первая цифра числа: ', b)
print('вторая цифра числа: ', d)
print('последня цифра числа: ', c)
