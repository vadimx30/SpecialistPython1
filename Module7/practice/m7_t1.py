"""
Написать функцию для сложения двух аргументов, в которую нужно
добавить обработку исключений для случаев сложения str с int, float и bool
"""

import random

class Str_a_Error(Exception):
    print('')
class Str_b_Error(Exception):
    print('')


def summary_func(a, b):
    '''суммирует аргументы a и b, если это не строка'''
    try:
        if type(a) == str:
            raise Str_a_Error("Аргумент a не может являться str")
        elif type(b) == str:
            raise Str_b_Error("Аргумент b не может являться str")
    except Str_a_Error as str_a_ex:
        print("Error! {0}".format(str_a_ex))
    except Str_b_Error as str_b_ex:
        print("Error! {0}".format(str_b_ex))
    else:
        print(f'Результат сложения двух заданнных аргументов: {a+b}')
        

def main():
    a = random.choice(['str', random.randint(0,100), random.uniform(0, 100),
                       random.random()])
    b = random.choice(['str', random.randint(0,100), random.uniform(0, 100),
                       random.random()])
    summary_func(a, b)


if __name__ == '__main__':
    main()
