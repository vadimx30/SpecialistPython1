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


a = 0
while a < 5:
    a += 1
    d = {'Up':0,'Low':0,'Spec':0,'Num':0}
    string = input('Enter password: ')
    for char in string:
        if str.isdigit(char):
            d['Num'] += 1
        if str.islower(char):
            d['Low'] += 1
        if str.isupper(char):
            d['Up'] += 1
        if not str.isalnum(char):
            d['Spec'] += 1
    a += 1
    if len(string) > 7 and len(string) <16 and not 0 in d.values():
        print(f'Password <{string}> is right')
        break
    error_str = ''
    if len(string) < 8 or len(string) > 15:
        error_str = error_str +'Need 8-15 simbols. '
    if d['Up'] == 0:
         error_str = error_str +'Need one or more upper simbols. '
    if d['Low'] == 0:
         error_str = error_str +'Need one or more lower simbols. '
    if d['Spec'] == 0:
         error_str = error_str +'Need one or more spec simbols. '
    if d['Num'] == 0:
         error_str = error_str +'Need one or more numeric. '
    print(f'Try {a}: Password <{string}> incorrect. {error_str}Try again')
else:
    print('!!! No more try. Access denied !!!')
