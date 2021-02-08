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

import func_m5_t1_hw
import sys
a = [i for i in input('Введите пароль: ')]
result = func_m5_t1_hw.proverka(a)
for i in range(5):
    if result == 'Хороший пароль':
        print(result)
        print('Пароль сохранен')
        sys.exit()
    else:
        print(result)
        if i != 4:
            print(f'Осталось попыток ввода: {4 - i}')
        else:
            print('У вас не осталось попыток ввода. Попробуйте позже')
            sys.exit()
    a = [i for i in input('Введите пароль: ')]
    result = func_m5_t1_hw.proverka(a)

    
    # func_m5_t1_hw
    import string as st
def proverka(a: list) -> str:
    result = ''
    N1 = [i for i in st.digits]
    N2 = [i for i in st.ascii_lowercase]
    N3 = [i for i in st.ascii_uppercase]
    N4 = [i for i in st.punctuation]
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    if len(a) < 8 or len (a) > 15:
        result = 'Пароль должен содерждать от 8 до 15 символов'
        return result
    for i in range(len(a)):
        for k in range(len(N1)):
            if a[i] == N1[k]:
                p1 += 1
                break
        for l in range(len(N2)):
            if a[i] == N2[l]:
                p2 += 1
                break
        for m in range(len(N3)):
            if a[i] == N3[m]:
                p3 += 1
                break
        for n in range(len(N4)):
            if a[i] == N4[n]:
                p4 += 1
                break
    if p1 > 0 and p2 > 0 and p3 > 0 and p4 >0:
        result = 'Хороший пароль'
        return result
    result = 'Пароль должен содержать:'
    if p1 == 0:
        result += 'цифры, '
    if p2 == 0:
        result += 'строчные латинские буквы, '
    if p3 == 0:
        result += 'заглавные латинские буквы, '
    if p4 == 0:
        result += 'специальные символы'
    return result
    
