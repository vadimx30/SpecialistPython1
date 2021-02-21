""" 4. Напишите программу для слияния нескольких словарей в один.
    4.1 Отсортировать полученный словарь по значениям
    4.2 Измените полученный словарь так, чтобы значение стали ключами,
    а ключи значениями
"""    
dict_a = {1:15, 2:21}
dict_b = {3:13, 4:54}
dict_c = {5:75, 6:68}


dict_a = {1:15, 2:21}
dict_b = {3:13, 4:54}
dict_c = {5:75, 6:68}

newd = {**dict_a,**dict_b,**dict_c}
newdsrt = {}
newdinvert = {}
d = list(newd.values())
d.sort()
for i in d:
    for key,value in newd.items():
        if value == i:
            newdsrt.update({key:value})
            newdinvert.update({value:key})

print(newd,newdsrt,newdinvert)
