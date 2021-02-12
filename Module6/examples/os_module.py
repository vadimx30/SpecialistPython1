# import os
# import sys
# import platform
# import datetime
# import glob
# import shutil

# ## Переменные среды в виде словаря
# print(os.environ)

# ## Система, на которой мы работаем
# print(platform.system()) ## out -> 'Windows'
#
# print(os.name)  ## out -> 'nt'
# print(sys.platform) ## out -> 'win32'
#
# ## Папки,в которых питон ищет файлы
# print(sys.path)
#
# ## Текущая директория
# print(os.getcwd())
# ## Текущая директория
# print(os.curdir)  ## -> '.'
# ## Родительская директория
# print(os.pardir)  ## -> '..'
#
# ## Список файлов и директорий
# print(os.listdir(os.curdir))
#
# ## Смена директории
# os.chdir('..')
# print(os.getcwd())
#
# ## Формируем относительный путь из названий файлов и папок
# print(os.path.join('Day_4', 'Students'))
#
# ## Используем \\ для экранирования пути
# print(os.path.join('Day_4\\Students', 'test1\\test2'))
#
# working_dir = os.path.join('Course', 'Day_4', 'Students')
# print(working_dir)
# working_file = os.path.join(working_dir, 'some.py')
# print(working_file)
#
# ## Разделяет пусть на два элемента, конечный файл или директория
# ## и предшествующий пусть
# print(os.path.split(working_dir))
# print(os.path.split(working_file))
#
# print(os.path.basename(working_file))
# print(os.path.dirname(working_file))
#
# ## Получаем расширение файла
# print(os.path.splitext(working_file))
#
# ## Раскрывает переменные среды
# print(os.path.expandvars('$HOMEPATH\\temp'))
#
# ## Переменная - это абсолютный путь
# dir_full_path = 'C:\\Course\\Day_4\\Students'
#
# ## Проверяем, есть ли указанная папка или файл
# print(os.path.exists(dir_full_path))
#
# file_full_path = os.path.join(dir_full_path, 'some.py')
# print(os.path.exists(file_full_path))
#
# ## Проверяем это папка или это файл
# print(os.path.isdir(dir_full_path))
# print(os.path.isfile(file_full_path))
#
# ## Проверяет путь - абсолютный или относительный
# print(os.path.isabs(working_dir))
# print(os.path.isabs(dir_full_path))
#
# ## Определение размера файла
# print(os.path.getsize(file_full_path))
#
# # ## Информация о файле
# print(os.stat(file_full_path))
#
# ## Время создания файла
# creation_date = os.path.getctime(file_full_path)
# print(creation_date)
# # ## Преобразуем время в обычный формат
# normal_date = datetime.datetime.fromtimestamp(creation_date)
# print(normal_date)

# ## Переименование файла
# print(os.rename('oldfile.txt', 'newfile.txt'))
# ## Удаление файла
# print(os.remove('newfile.txt'))
#
# ## Создание директории
# os.mkdir('temp_1') ## Вернет ошибку, если такая папку уже существует
# os.rmdir('temp_1') ## Вернет ошибку, если такой папки не существует

# ## Создание вложенных папок
# os.makedirs('temp1/temp2/temp3')
# os.removedirs('temp1/temp2/temp3')
#
# ## Перемещение файла
# os.replace("new_file.txt", "folder/file.txt")
#
# ## Удаление папки с содержимым
# shutil.rmtree('temp1')

# ## Создание копии файла
# os.popen('copy new_file.txt new3_file.txt')
# shutil.copyfile('new_file.txt', 'dpaste.txt')
#
# ## Копирование в определенную папку с тем же именем файла
# shutil.copy("new_file.txt", "D:\\Course\\Day_4\\folder")
# ## Копирование в определенную папку, меняя имя файла
# shutil.copy2("new_file.txt", "D:\\Course\\Day_4\\folder\\test2.txt")


# ## Создаем список объектов DirEntry, которые возвращает os.scandir()
# with os.scandir('.') as my_dir:
#     for entry in my_dir:
#         print(entry.name, entry.is_file())

# ## Рекурсивно проходится по всем вложенным папкам и
# ## возвращает название папок и файлов
# print(os.getcwd())
# for dirpath, dirnames, filenames in os.walk("D:\\Course\Day_4\\"):
#     ## Идем по списку папок
#     print(dirnames)
#     for dirname in dirnames:
#         print("Каталог:", os.path.join(dirpath, dirname))
#     ## Идем по списку файлов
#     for filename in filenames:
#         print("Файл:", os.path.join(dirpath, filename))

# ## Поиск по шаблону
# from pprint import pprint
# pprint(glob.glob('*'))  ## * - это любое количество символов
# pprint(glob.glob('*.py'))
# print(glob.glob('file_ex.p?'))  ## ? какой-то один символ
# print(glob.glob('*.[a-z][a-z]')) ## [a-z] любая буква из диапазона
