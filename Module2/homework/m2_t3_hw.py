# Задача №3
# Дано натуральное число N. Если число N двузначное,
# то найти сумму цифр числа. Если число N трехзначное,
# то найти произведение ненулевых цифр числа
n = [int(i) for i in input('Enter N: ')]
if len(n) < 2 or len(n) > 3:
    print('Do nothing.')
else:
    if len(n) == 2:
        print('Result (+): ',n[0]+n[1])
    else:
        n = [i for i in n if i != 0]
        if len(n) == 0:
            p = 0
        else:
            p = 1
        for i in n:
            p = p*i
        print('Result (*):',p)
