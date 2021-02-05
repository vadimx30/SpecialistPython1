"""
Программа получает на вход последовательность целых чисел N(1-10).
Вам нужно определить вид последовательности:
 - возрастающая
 - убывающая
 - случайная
 - постоянная
В качестве ответа следуют выдать прописными латинскими буквами тип последовательности:
1. ASCENDING (строго возрастающая)
2. WEAKLY ASCENDING (нестрого возрастающая, то есть неубывающая)
3. DESCENDING (строго убывающая)
4. WEAKLY DESCENDING (нестрого убывающая, то есть невозрастающая)
5. CONSTANT (постоянная)
7. RANDOM (случайная)
Примеры входных и выходных данных:
In: 9 4 2 -1  Out: DESCENDING
In: 3 8 8 11  Out: WEAKLY ASCENDING
In: 2 -1 7    Out: RANDOM
In: 5 5 5 5   Out: CONSTANT
"""

text = input('Введите последовательность целых чисел: ').split()
import sys
try:
    sequence = [int(_) for _ in text]
except ValueError:
    print('Введите числа')
    sys.exit()

if all(sequence[i] == sequence[i+1] for i in range(len(sequence)-1)):
    print(f'In: {" ".join(text)} \nOut: CONSTANT')

elif all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1)):
    if all(sequence[i] < sequence[i+1] for i in range(len(sequence)-1)):
        print(f'In: {" ".join(text)} \nOut: ASCENDING')
    else:
        print(f'In: {" ".join(text)} \nOut: WEAKLY ASCENDING')

elif all(sequence[i] >= sequence[i+1] for i in range(len(sequence)-1)):
    if all(sequence[i] > sequence[i+1] for i in range(len(sequence)-1)):
        print(f'In: {" ".join(text)} \nOut: DESCENDING')
    else:
        print(f'In: {" ".join(text)} \nOut: WEAKLY DESCENDING')

else:
    print(f'In: {" ".join(text)} \nOut: RANDOM')
