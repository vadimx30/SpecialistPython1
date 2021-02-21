import re

text = r'''100 PYTHON1 Первый_модуль
200 PYTHON2    Второй_модуль
300 PYTHON3  Третий_модуль'''

# print(re.split('\s+', text))
# print(re.findall('\d+', text))
# res = re.search('\d+', text)
# print(res.group()) ## Результат поиска
# print(res.start(), res.end())  ## индексы результата
# 
# ## Ищет только в начале строки 
# res2 = re.match('\d+', text)
# print(res2)
# 
# ## создается компилированной объект шаблона поиска, но выигрыш небольшой 
# regex = re.compile('\s+')
# print(regex, type(regex))
# print(regex.sub(' ', text))
# # # 
# # # # убрать все пробелы кроме символа новой строки  
# regex = re.compile('((?!\n)\s+)')
# print(regex.sub(' ', text))
# # 
# # 
# # ## Группы регулярных выражений
# # # извлечь все номера курсов  
# print(re.findall('[0-9]{3}', text))
# # 
# # # # извлечь все коды курсов (для латиницы [A-Z])
# print(re.findall('[A-Z]{6}[0-9]', text))
# # 
# # # # извлечь все названия курсов
# print(re.findall('[а-яА-ЯёЁ_]{4,}', text))
# # # # 
# # # # создайте группы шаблонов текста курса и извлеките их
# course_pattern = '([0-9]+)\s+([A-Z]{6}[0-9])\s+([а-яА-ЯёЁ_]{4,})'  
# print(re.findall(course_pattern, text))
# 
# courses_p = r'(?P<code>[0-9]+)\s+(?P<name>[A-Z]{6}[0-9])\s+(?P<comment>[а-яА-ЯёЁ_]{4,})'
# for item in text.split('\n'):
#     courses = re.search(courses_p, item)
#     if courses is not None:
#         print(courses.group('code'), end=' ')
#         print(courses.group('name'), end=' ')
#         print(courses.group('comment'))
#     else:
#         print('Nothing')

# # 
# text = "<body>Пример жадного соответствия регулярных выражений</body>"  
# print(re.findall('<.*>', text)) ## Максимально подходящая строка
# 
# ## Ленивое соотвествие
# print(re.findall('<.*?>', text)) ## Минимально подходящая строка
# 
# ## если только одно соотвествие то используем re.search()
# print(re.search('<.*?>', text).group())
# ## поиск шаблона с новой строки
# print(re.match('<.*?>', text)[0])



