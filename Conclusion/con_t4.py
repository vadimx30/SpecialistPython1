""" 4. Напишите программу для слияния нескольких словарей в один.
    4.1 Отсортировать полученный словарь по значениям
    4.2 Измените полученный словарь так, чтобы значение стали ключами,
    а ключи значениями
"""    
dict_a = {1:15, 2:21}
dict_b = {3:13, 4:54}
dict_c = {5:75, 6:68}
dict_a.update(dict_b)
dict_a.update(dict_c)
print(f'Общий словарь: {dict_a}')
val = list(dict_a.values())
val.sort()
dict_d = {}
for i in val:
    for key, value in dict_a.items():
        if i == value:
            dict_d[key] = i
print(f'Отсортировано по значениям: {dict_d}')
dict_e = {}
for key, value in dict_d.items():
    dict_e[value] = key
print(f'Словарь значение:ключ {dict_e}')
