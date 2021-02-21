import re 

# print(r'\n\t\r') ##out -> '\n\t\r'
# try:
#     pattern = r'\d{2}\D\d\d'
#     match = re.search(pattern, r'Телефон 123-12-12-19')
#     ## Функция search находит только первую подходящую подстроку
#     ## Если ничего не найдено, произойдет ошибка при обращении
#     print(type(match), match.group(), match.start(), match.end(), match.span())
#     # print(match[0] if match else 'Not found')  # -> 23-12
# except AttributeError:
#     print('Nothing')
# # # 
# pattern = '\d\d\D\d\d'
# match = re.search(pattern, 'Телефон 1231212') 
# print(match[0] if match else 'Not found')  # -> Not found 
#  
# ## Должно быть полное соответствие строки целиком
# match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
# # index = input("enter: ")
# # match = re.fullmatch(r'\d{6}', index)
# print('YES' if match else 'NO')  # -> YES
# 
# # ## Условие не выполнено, поэтому результат -> 'NO' 
# match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12') 
# print('YES' if match else 'NO')  # -> NO 
# # # 
# # ## Разделяет строку по шаблону и возращает список
# print(re.split(r'\W+', 'Где, скажите мне, мои очки??!')) 
# # # # -> ['Где', 'скажите', 'мне', 'мои', 'очки', '']
# print(re.split(r'\W+', 'Где, скажите мне, мои очки??!', 3))
# ### -> ['Где', 'скажите', 'мне', 'мои очки??!']
# # 
# # ## Находит все соответствия и возвращает список результатов
# print(re.findall(r'\d\d\.\d{2}\.\d{4}',
#                  r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# # # -> ['19.01.2018', '01.09.2017'] 
# ## 
# for m in re.finditer(r'\d\d\.\d\d\.\d{4}', '''Эта строка написана 19.01.2018,
# #                                              а могла бы и 01.09.2017'''): 
#      print('Дата', m[0], 'начинается с позиции', m.start()) 
# # # # -> Дата 19.01.2018 начинается с позиции 20 
# # # # -> Дата 01.09.2017 начинается с позиции 45 
# # # # 
# print(re.sub(r'\d\d\.\d\d\.\d{4}', 
#              r'DD.MM.YYYY', 
#              r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017', count=1)) 
# # # # -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY
# #
## Пример использования скобок
# string = 'Te [12xt for (1234 testing. [12345] is the phone number. 123-(123)-[678]'
# pattern = r'[\[(]\d{1,5}[0-9\])]'
# result = re.findall(pattern, string)
# print(result)

# # ## Использование дополнительных флагов в питоне
# print(re.findall(r'\d+', '12 + ٦٧')) 
# # # -> ['12', '٦٧'] 
# print(re.findall(r'\w+', 'Hello, мир!')) 
# # # # -> ['Hello', 'мир'] 
# print(re.findall(r'\d+', '12 + ٦٧', flags=re.ASCII)) 
# # # # -> ['12'] 
# print(re.findall(r'\w+', 'Hello, мир!', flags=re.ASCII)) 
# # # -> ['Hello']
# 
# print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя')) 
# # # -> ['ааааа', 'яяяя'] 
# print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя', flags=re.IGNORECASE)) 
# # # -> ['ОООО', 'ааааа', 'ЫЫЫЫ', 'яяяя']
# 
# # 
# text = r""" 
# Торт
# с вишней1
# вишней2.
# """ 
# print(re.findall(r'Торт.с', text)) 
# # # -> [] 
# print(re.findall(r'Торт.с', text, flags=re.DOTALL)) 
# # -> ['Торт\nс'] 
# print(re.findall(r'виш\w+', text, flags=re.MULTILINE)) 
# # -> ['вишней1', 'вишней2']
# 
# ## Символ ^ - это начало строки
# print(re.findall(r'^виш\w+', text, flags=re.MULTILINE))
# # -> ['вишней2']
# 
# ## Символ $ - это конец строки
# print(re.findall(r'виш\w+$', text, flags=re.MULTILINE)) 
# # -> ['вишней1']










