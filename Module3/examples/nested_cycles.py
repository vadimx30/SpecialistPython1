# for i in range(5):
#     for j in range(7):
#         print(f"{i} {j} {i + j}", end='*|*')
#     print()
#     for char in 'hello':
#         print(char.upper(), end=' ')
#     print()
#     print(f'Внешний цикл отработал {i} итерацию')
    
    
example = [[1, 2], [3, 5, 6], [3, 8, 9], [4, 0, 9, 8, 100]]
count = 0
for lst in example:
    for item in lst:
        if item == 9:
            count += 1
            
print('result: ', count)