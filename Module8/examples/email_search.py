import re

'''
цифра или буква -_..@название домена < 11 букв и/или '-'.название доменной зоны 4 символа
'''
ex_1 = '44onteassas.t. saethuss user@mail-mail.ru988,t'
ex_2 = '232323@toeuhann_1.tanm@web-mail.org_teuhnan'
ex_3 = '_maetch2112@aem.comnonetuhass'
ex_4 = ' aotan..ate..mail.1@mail.com.chsash'
ex_5 = ' Приветexamples4_.mail@mail.io_cuau**'
ex_6 = '   1@mail.ru      '
list_ex = [ex_1, ex_2, ex_3, ex_4, ex_5, ex_6]

pattern = r'[\w.-]+@[\w.-]+'

    
for i in range(6):
    match = re.search(pattern, list_ex[i])
    result = f'email: {match[0]}' if match else 'Nothing'
    print(result)
