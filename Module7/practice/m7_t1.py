"""
Написать функцию для сложения двух аргументов, в которую нужно
добавить обработку исключений для случаев сложения str с int, float и bool
"""
try:
    a = int(input('enter:'))
    b = int(input('enter:'))
    c = a + b
    print(c)
except(ValueError, TypeError):
    print('Error')
