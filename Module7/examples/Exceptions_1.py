# import sys
# ## Проверка знаменателя
# try:
#     val = int(input("input number: "))
#     if val < 0:
#         raise Exception("Some exception") ## go to string №13
#     tmp = 10 / val
#     print(tmp)
#
# except ValueError as ve:
#     print("ValueError! {0}".format(ve))
# except ZeroDivisionError as zde:
#     print("ZeroDivisionError! {0}".format(zde))
# except Exception as ex:
#     print("Error! {0}".format(ex))
# else:
#     print('Все хорошо')
# finally:
#     print('Finally code')
#
# print('Done')

# ## Пример работы с файлом
# with open('tmp.txt', 'w') as f:
#     print('some strings', file=f)

# ## Обработка ошибки открытия файла
# try:
#     f = open("tmp1.txt", "r")
#     for line in f:
#         print(line)
#     f.close()
# except Exception as e:
#     print(e)
#     flag = False
# else:
#     flag = True
#     print("File was readed")

# if not flag:
#     print('Plan B')
#
# import sys

# ## Обработка прерывания исполнения по нажатию Ctrl+C
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print('The end.')
#

# ## Функция sys.exc_info содержит информацию об исключениях
# try:
#     1 / 0
# except Exception as e:
#     print(e)
#     print('*' * 40)
#     errors = sys.exc_info()
#     for error in errors:
#         print(error)
