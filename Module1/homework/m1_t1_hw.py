# Задача № 1. Получить реверсную запись трехзначного числа
# Пример: 
# вход: 346, выход: 643
# вход: 100, выход: 001

number = int(input('Введите трехзначное число: '))
left = int(number / 100)
middle = int((number - left * 100) // 10)
right = int(number % 10)

result = (right * 100 + middle * 10 + left)

print('Реверсная запись трехзначного числа: ', result) ##не работает если 0 в разряде единиц


# Решение через создание списка объектов (list)
number = str(input('Введите трехзначное число: '))
left = int(number[-1])
middle = int(number[-2])
right = int(number[-3])

result = [left, middle, right]

print('Реверсная запись трехзначного числа: ', result[0], result[1], result[2]) #требуется форматирование


# Решение через метод join() у списков объектов (list)
number = str(input('Введите трехзначное число: '))
left = (number[-1])
middle = (number[-2])
right = (number[-3])

n_list = [left, middle, right]
result = ''.join(n_list)

print('Реверсная запись трехзначного числа: ', result)


# Решение через методы reverse()+join() у списков объектов (list)
number = str(input('Введите трехзначное число: '))
n_list = list(number)
n_list.reverse()

result = ''.join(n_list)

print('Реверсная запись трехзначного числа: ', result)


# Решение через срез
number = str(input('Введите трехзначное число: '))

result = number[::-1]

print('Реверсная запись трехзначного числа: ', result)
