""" 5. Напишите программу, которая из заданного списка выводит только те числа,
    у которых сумма цифр четна и останавливается, если встречает число 237.
    Порядок элементов не менять!
"""
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
]

numbers = [    
386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
]
list1 = []
for i in numbers:
    if (i % 10 + i // 100 + ((i % 100) // 10)) % 2 == 0:
        list1.append(i)
    if i == 237:
        break
print(list1)
