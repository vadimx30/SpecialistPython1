a, b, c, d = map(int, input('Введите 4 числа: ').split())
count = sum([a == 0, b == 0, c == 0, d == 0])
print('Количество чисел раных нулю', count)
