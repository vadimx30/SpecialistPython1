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

# import DZ
# import sys
# a = [i for i in input('пароль: ')]
# result = DZ.proverka(a)
# for i in range(5):
#     if result == 'хороший':
#         print(result)
#         print('сохранено')
#         sys.exit()
#     else:
#         print(result)
#         if i != 4:
#             print(f'Осталось попыток: {4 - i}')
#         else:
#             print('Осталось попыток 0')
#             sys.exit()
#     a = [i for i in input('пароль: ')]
#     result = ZD.proverka(a)
# 
# 
#     # DZ
#     import string as st
# def proverka(a: list) -> str:
#     result = ''
#     N1 = [i for i in st.digits]
#     N2 = [i for i in st.ascii_lowercase]
#     N3 = [i for i in st.ascii_uppercase]
#     N4 = [i for i in st.punctuation]
#     p1 = 0
#     p2 = 0
#     p3 = 0
#     p4 = 0
#     if len(a) < 8 or len (a) > 15:
#         result = 'от 8 до 15 символов'
#         return result
#     for i in range(len(a)):
#         for k in range(len(N1)):
#             if a[i] == N1[k]:
#                 p1 += 1
#                 break
#         for l in range(len(N2)):
#             if a[i] == N2[l]:
#                 p2 += 1
#                 break
#         for m in range(len(N3)):
#             if a[i] == N3[m]:
#                 p3 += 1
#                 break
#         for n in range(len(N4)):
#             if a[i] == N4[n]:
#                 p4 += 1
#                 break
#     if p1 > 0 and p2 > 0 and p3 > 0 and p4 >0:
#         result = 'Хороший'
#         return result
#     result = 'Пароль должен содержать:'
#     if p1 == 0:
#         result += 'st.digits,'
#     if p2 == 0:
#         result += 'st.ascii_lowercase,'
#     if p3 == 0:
#         result += 'st.ascii_uppercase,'
#     if p4 == 0:
#         result += 'st.punctuation'
#     return result
