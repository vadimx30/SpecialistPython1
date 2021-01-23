# Задача №3
# Найти каждую цифру четырехзначного числа.

import math
number = int(input('Введите четырехзначное число: '))
left = int(number / 1000)
right1 = int(number % 100)
middle = int(number - (left * 1000))
right2 = int(number % 10)

print ('Первая цифра:',left,
       '\nВторая цифра:',middle // 100,
       '\nТретья цифра:',right1 // 10,
       '\nЧетвертая цифра:',right2)
