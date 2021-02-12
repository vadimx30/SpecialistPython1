import sys

"""
Файлы

Файлы открываются функцией open( file_name, mode ). Функция возвращает объект.

file_name - [путь до файла]имя файла

mode - режим работы с файлом:

    'r': только чтение (default)
    'w': запись ”с ноля” (содержимое файла будет стерто)
    'x': создать (если файл существует, будет выброшено исключение)
    'a': запись в конец файла
    'b': «бинарный» режим
    't': «текстовый режим» (default)
    '+': доступ и на запись, и на чтение.

У объекта file есть следующие методы:

    read( size ) - прочитать содержимое файла размером size байтов/символов
    readline() - прочитать строку и передвинуть указатель на следующую
    readlines() - вернуть список строк
    write() - запись в файл, функция возвращает количество прочитанных символов
    seek(offset, whence) - перемещает указатель файла на offset байт в
    зависимости от позиции whence:
            0 - от начала, 1 - от текущей позиции, 2 - с конца файла.
            Offset может быть отрицательным.
    tell() - возвращает текущую позицию в байтах, от начала файла
    truncate(bytes) - сократить размер файла до bytes байт

! Файл закрывается методом close().

!! Рекомендуется использовать конструкцию with ... as ...:
   так как он закрывает файл автоматически, после отработки блока with ... as
"""

f = open('file4test.txt', 'w')

for _ in range(10):
    f.write('Hello world!\n')
f.writelines(['hello\n', 'Python'])
f.close()

# ## Используем функцию print с файловым идентификатором
file_p = open('examples_file.txt', 'a')
print('Hello Python', file=file_p)
print(f'Our version is {sys.version}')
file_p.write('this is just a text\n')
file_p.close()

# cur_dir = os.getcwd()
# path = os.path.join(cur_dir, 'examples_file.txt')
# ## Пример работы менеджера контекста
# with open(path) as read_file:
#     for line in read_file.readlines():
#         print(line)

# ## read_file.write('test') ## Ошибка, потому что файл закрыт


def func():
    with open('examples_file.txt', 'r') as f:
        for line in f.readlines():
            yield line


res = func()
# print(res)
# flag = True
# while flag:
#     flag = next(res, 0)
#     print(flag)

# ## Проходим по генератору, вычисляем значения и печатаем их
for line in res:
    print(line)

gen_example = (i ** 2 for i in range(10))
print(gen_example)
