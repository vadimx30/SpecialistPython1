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
print(dict_a)


list_values = list(dict_a.values())
list_values.sort()

result = {}
for i in list_values:
    for key,value in dict_a.items():
        if value == i:
            result.update({key:value})
print(result)

result = {}
for i in list_values:
    for key,value in dict_a.items():
        if value == i:
            result.update({value:key})
print(result)
