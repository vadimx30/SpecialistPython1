'''
Задача №1
Вход:
Пользователь должен ввести правильный пароль, состоящий из цифр, букв латинского алфавита(строчные и прописные) и специальных символов  _!@#$%^&*.
Всего 4 набора различных символов.
В пароле обязательно должен быть хотя бы один символ из каждого набора.
Длина пароля от 8(мин) до 15(макс) символов.
Количество попыток ввода ненравильного пароля не больше 5.
Каждый раз выводим номер попытки.
Желательно выводить пояснение, почему пароль не принят и что нужно исправить.

Выход:
Написать, что ввели правильный пароль и вывести его

Пример: 
хороший пароль -> o58anuahaunH!
плохой пароль -> saucacAusacu8  -> нет
'''

import string as st
import sys

def main(): 
    TRY = 5
    password = input('Пароль: ')
    final = check(password)
    
    for i in range(TRY):
        if final == 'Вы ввели правильный пароль':
            print(final)
            print(f'Ваш пароль: {password}')
            sys.exit()
        else:
            print(final)
            if (i + 1) != TRY:
                print(f'Номер попытки: {(i + 1)}')
                print(f'Осталось попыток: {TRY - (i + 1)}')
            else:
                print('Попыток ввода не осталось')
                sys.exit()
        password = input('Пароль: ')
        final = check(password)
    

def check(password: str) -> str:
    '''Проверка пароля на соответствие требованиям'''
    message = ''
    flag_lengs = False
    flag_digits = False
    flag_lowercase = False
    flag_uppercase = False
    flag_punct = False
       
    if any(password[i] in st.digits for
           i in range(len(password))):
        flag_digits = True
    else:
        message = 'Пароль должен содержать цифры'
    
    if any(password[i] in st.ascii_lowercase for
           i in range(len(password))):
        flag_lowercase = True
    else:
        message = 'Пароль должен содержать строчные буквы'
    
    if any(password[i] in st.ascii_uppercase for
           i in range(len(password))):
        flag_uppercase = True
    else:
        message = 'Пароль должен содержать прописные буквы'
          
    if any(password[i] in st.punctuation for
           i in range(len(password))):
        flag_punct = True
    else:
        message = 'Пароль должен содержать специальные символы'
          
    if len(password) > 7 and len(password) < 16:
        flag_lengs = True
    else:
        message = 'Длина пароля должна быть от 8 до 15 символов'
           
    
    if (flag_lengs and flag_digits and flag_lowercase and
        flag_uppercase and flag_punct):
        return 'Вы ввели правильный пароль'
    else:
        return message

if __name__ == '__main__':
    main()
