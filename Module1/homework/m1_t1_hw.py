num1 = int(input("Введите целое число: "))
num2 = 0
if num1 < 1000 and num1 > 99:
    while num1 > 0:
        digit = num1 % 10
        num1 = num1 // 10
        num2 = num2 * 10
        num2 = num2 + digit
        print('"Обратное" ему число:', num2)
else:
    print('Число неверно!')
