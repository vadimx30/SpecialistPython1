sum = float(input('Введите сумму от 100 до 1000000: '))
if sum < 100:
    print('Сумма слишком маленькая!')
    exit
elif sum > 1000000:
    print('Сумма слишком большая!')
    exit
else:
    compaund = float(input('Введите количество периодов начисления сложных процентов в год: '))
    procents = float(input('Введите годовой процент от 1% до 20%: '))
    if procents < 1:
        print('Процент слишокм маленький!')
        exit
    elif procents > 20:
        print('Процент слишокм большой!')
        exit
    else:
        years = float(input('Введите срок вклада от 1 года до 100 лет: '))
        if years < 1:
            print('Срок вклада слишокм маленький!')
            exit
        elif years > 100:
            print('Срок слишокм большой!')
            exit
        else:
            fsum = sum * (((1 + ((procents/100.0)/compaund)) ** (compaund*years)))
            fsum = round(fsum,2)
            print('Отлично!')
            print('Общая сумма составит:', fsum, 'за', years, 'лет')
